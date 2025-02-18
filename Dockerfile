FROM python:3.11-slim

# Configuração do diretório de trabalho
WORKDIR /app

# Copiar o arquivo de requisitos
COPY requirements.txt /app/

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos do projeto
COPY . /app/

# Definir o comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
