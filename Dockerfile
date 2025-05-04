# Etapa 1: imagem base oficial do Python
FROM python:3.11-slim

# Etapa 2: instalar dependências do sistema necessárias para o uv
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Etapa 3: instalar o gerenciador de pacotes uv
RUN curl -Ls https://astral.sh/uv/install.sh | bash

# Etapa 4: adicionar o uv ao PATH
ENV PATH="/root/.cargo/bin:$PATH"

# Etapa 5: criar diretório de trabalho e copiar os arquivos do projeto
WORKDIR /app
COPY . .

# Etapa 6: instalar dependências usando uv
RUN uv pip install .

# Etapa 7: expor a porta usada pelo Render (ex: 10000)
EXPOSE 10000

# Etapa 8: iniciar o servidor FastAPI com uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]
