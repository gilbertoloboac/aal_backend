# Usar a imagem base do Python 3.11
FROM python:3.11-slim

# Instalar dependências necessárias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libmagic1 && \  # Para análise de tipos de arquivo
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Criar usuário sem privilégios
RUN adduser --disabled-password --gecos '' appuser

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para dentro do contêiner
COPY requirements.txt /app/

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos restantes do projeto para dentro do contêiner
COPY . /app/

# Garantir que os arquivos têm as permissões corretas
RUN mkdir -p /app/media /app/staticfiles && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app/media /app/staticfiles

# Mudar para o usuário sem privilégios
USER appuser

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE aal_api.settings

# Executar o collectstatic após copiar os arquivos
RUN python manage.py collectstatic --noinput

# Expor a porta 8080
EXPOSE 8080

# Verificar a saúde do contêiner
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s \
    CMD curl -f http://localhost:8080/health/ || exit 1

# Definir o comando para rodar o Gunicorn
CMD exec gunicorn aal_api.wsgi:application \
    --bind 0.0.0.0:8080 \
    --workers 3 \
    --timeout 120 \
    --worker-class sync \
    --log-level info \
    --access-logfile -