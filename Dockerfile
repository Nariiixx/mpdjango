# Usa Python 3.11 como base
FROM python:3.11

# Atualiza pacotes do sistema e instala dependências do MySQL (usando MariaDB)
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Atualiza pip antes de instalar dependências
RUN pip install --upgrade pip

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta (caso seja uma aplicação web)
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
