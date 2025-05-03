FROM python:3.11-slim

# Instala dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libmagic1 \
        curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Cria usuário e diretórios
RUN useradd -m appuser && \
    mkdir -p /app/media /app/staticfiles && \
    chown -R appuser:appuser /app

WORKDIR /app

# Instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Configura permissões
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app/media

USER appuser

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=aal_api.settings

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s \
    CMD curl -f http://localhost:8080/health/ || exit 1

CMD ["gunicorn", "aal_api.wsgi:application", \
    "--bind", "0.0.0.0:8080", \
    "--workers", "3", \
    "--timeout", "120", \
    "--worker-class", "sync"]