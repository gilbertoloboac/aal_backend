# Usar a imagem base do Python 3.11
FROM python:3.11-slim

# Instalar dependências necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libmagic1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Criar usuário sem privilégios
RUN adduser --disabled-password --gecos '' appuser

# Definir o diretório de trabalho
WORKDIR /app

# Copiar requirements primeiro para aproveitar cache de camadas
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação
COPY . .

# Configurar permissões
RUN mkdir -p /app/media /app/staticfiles && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app/media /app/staticfiles

# Mudar para usuário não privilegiado
USER appuser

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=aal_api.settings

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Porta de exposição
EXPOSE 8080

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s \
    CMD curl -f http://localhost:8080/health/ || exit 1

# Comando principal
CMD ["gunicorn", "aal_api.wsgi:application", \
    "--bind", "0.0.0.0:8080", \
    "--workers", "3", \
    "--timeout", "120", \
    "--worker-class", "sync", \
    "--log-level", "info"]