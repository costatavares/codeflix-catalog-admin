#!/bin/bash

APP_NAME=$1
TARGET_DIR="./src/django_project"

# Verifica se o nome foi passado
if [ -z "$APP_NAME" ]; then
  echo "Uso: ./create_app.sh nome_da_app"
  exit 1
fi

# Cria a app no diretório atual
python manage.py startapp "$APP_NAME"

# Cria diretório de destino se não existir
mkdir -p "$TARGET_DIR"

# Move a app para o destino
mv "$APP_NAME" "$TARGET_DIR"

# Confirma
echo "App '$APP_NAME' criada e movida para '$TARGET_DIR/$APP_NAME'."
