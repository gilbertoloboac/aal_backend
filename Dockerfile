# Atualizado em 02/05
FROM python:3.11-slim



RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Criar usuário sem privilégios
RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN chown -R appuser /app

USER appuser

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s CMD curl -f http://localhost:8000/ || exit 1

CMD exec gunicorn aal_api.wsgi:application --bind 0.0.0.0:8000
