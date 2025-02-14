# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para dentro do container
COPY requirements.txt /app/

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do seu código para o container
COPY . /app/

# Defina o comando para rodar a aplicação
CMD ["python", "app.py"]

RUN pip install --no-cache-dir django && python -m django --version


RUN pip install --no-cache-dir -r requirements.txt