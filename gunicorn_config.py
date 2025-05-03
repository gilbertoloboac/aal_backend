bind = "0.0.0.0:8000"
module = "aal_api.wsgi:application"  # Corrigido para match com seu WSGI

workers = 4  # Número de workers (recomendado geralmente 2-4 x núcleos CPU)
worker_connections = 1000  # Máximo de conexões simultâneas por worker
threads = 4  # Número de threads por worker

# Configurações adicionais recomendadas para produção:
timeout = 120  # Segundos antes de considerar um worker como falho
keepalive = 5  # Segundos para manter conexões keep-alive
max_requests = 500  # Reiniciar worker após esta quantidade de requests
max_requests_jitter = 50  # Variação aleatória no max_requests

# Logging
accesslog = "-"  # Log para stdout (útil para Docker)
errorlog = "-"   # Log de erros para stdout
loglevel = "info"  # Nível de log (debug, info, warning, error, critical)

# Segurança
limit_request_line = 4094  # Tamanho máximo da linha de request
limit_request_fields = 100  # Número máximo de headers
limit_request_field_size = 8190  # Tamanho máximo de cada header