#!/bin/bash

# Cria o ambiente virtual
python3 -m venv venv

# Ativa o ambiente virtual
source venv/bin/activate

# Instala as dependências
pip install -r requirements.txt

# Define a porta padrão se $PORT não estiver definida
PORT=${PORT:-8000}

# Inicia o servidor
uvicorn api:app --host 0.0.0.0 --port $PORT