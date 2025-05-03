# Usar a imagem base do Python 3.11
FROM python:3.11-slim

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libmagic1 \  # Para análise de tipos de arquivo
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Criar usuário sem privilégios
RUN adduser --disabled-password --gecos '' appuser

# Definir o diretório de trabalho
WORKDIR /app

# Primeiro copiar apenas requirements para aproveitar cache de camadas
COPY requirements.txt /app/

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos restantes do projeto
COPY . /app/

# Garantir que os arquivos têm as permissões corretas
RUN chown -R appuser:appuser /app && \
    mkdir -p /app/media /app/staticfiles && \
    chmod -R 755 /app/media /app/staticfiles

# Mudar para o usuário sem privilégios
USER appuser

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE aal_api.settings  # Ajuste para seu módulo de settings

# Executar collectstatic
RUN python manage.py collectstatic --noinput

# Expor a porta
EXPOSE 8080

# Healthcheck melhorado
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s \
    CMD curl -f http://localhost:8080/health/ || exit 1

# Comando Gunicorn otimizado
CMD exec gunicorn aal_api.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3 \
    --timeout 120 \
    --worker-class sync \
    --log-level info \
    --access-logfile -