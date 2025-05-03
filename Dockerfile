# Use a imagem slim do Python 3.11
FROM python:3.11-slim

# 1. Instalação de dependências do sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libmagic1 \
        curl \
        # Adicionado para manipulação de imagens
        libjpeg-dev \
        zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 2. Configuração de usuário e diretórios
RUN useradd -m appuser && \
    mkdir -p /app/media /app/staticfiles && \
    chown -R appuser:appuser /app

WORKDIR /app

# 3. Instalação de dependências Python (com cache otimizado)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    # Limpeza para reduzir tamanho da imagem
    rm -rf /root/.cache/pip

# 4. Cópia do projeto (com .dockerignore configurado)
COPY . .

# 5. Configuração de permissões
RUN chown -R appuser:appuser /app && \
    chmod -R 755 /app/media && \
    # Garante que o usuário tem permissão de escrita
    chmod -R g+w /app/media

USER appuser

# 6. Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=aal_api.settings \
    # Adicionado para produção
    PYTHONHASHSEED=random

# 7. Coleta de arquivos estáticos
RUN python manage.py collectstatic --noinput --clear

EXPOSE 8080

# 8. Healthcheck melhorado
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s \
    CMD curl -f http://localhost:8080/health/ || exit 1

# 9. Comando de inicialização otimizado
CMD ["gunicorn", "aal_api.wsgi:application", \
    "--bind", "0.0.0.0:8080", \
    "--workers", "3", \
    "--timeout", "120", \
    "--worker-class", "sync", \
    "--access-logfile", "-", \
    "--error-logfile", "-", \
    "--capture-output"]