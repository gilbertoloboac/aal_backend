# Imagem oficial do Python
FROM python:3.11-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Definir diretório de trabalho
WORKDIR /app

# Copiar e instalar dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o projeto para dentro do container
COPY . /app/

# Variáveis de ambiente importantes
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expõe a porta 8000 para acesso
EXPOSE 8000

# Comando para rodar o servidor usando gunicorn
CMD ["gunicorn", "aal_api.wsgi:application", "--bind", "0.0.0.0:8000"]
