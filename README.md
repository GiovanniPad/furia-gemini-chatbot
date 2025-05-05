# Chatbot sobre o time de CS da Fúria, feito com Gemini

## Introdução

Este projeto é sobre um simples chatbot usando o gemini para que o usuário possa perguntar sobre o time de CS da organização Fúria.

## Considerações

- Este projeto tem o foco de ser mínimo, tendo como primeira versão uma aplicação mínima para funcionar.
- Este projeto utiliza para hospedá-lo, a plataforma Render e para responder os usuários a API do Gemini da Google.

## Instalação

Primeiramente você deve se certificar de possuir o [Python 3.13](https://www.python.org/downloads/) instalado e o uv instalado, para instalar o uv execute o comando a seguir:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Após ter instalado o projeto execute o comando a seguir para ter todas as dependências necessárias:

```bash
uv sync
```

A partir disso é possível executar e testar o projeto utilizando:

```bash
uv run uvicorn backend.main:app
```

Por fim, basta criar um arquivo `.env` e colocar a `GEMINI_API_KEY` dentro dele.

## Deployment

Para realizar o deploy desta aplicação foi utilizado o Render e como ele não possui um suporte nativo ao uv utilizado para gerenciar as dependências e o projeto, é necessário realizar o lock do `pyproject.toml` para `requirements.txt`, para isso utiliza-se o comando a seguir, dentro da pasta raiz:

```bash
uv pip compile pyproject.toml -o requirements.txt
```

O restante da configuração basta seguir o passo a passo imposto pelo Render, que tudo vai dar certo!