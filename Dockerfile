FROM python:3.10-slim

# Instala dependências do sistema e sqlite3
RUN apt-get update && apt-get install -y \
    sqlite3 \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho
WORKDIR /code

# Copia os arquivos de dependência
COPY requirements.txt .

# Instala dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . .
