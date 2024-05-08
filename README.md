# Traduzo

Traduzo é uma aplicação de tradução de textos entre vários idiomas, desenvolvida utilizando Python com o framework Flask. Este projeto foi desenvolvido como parte de um desafio técnico para verificar habilidades em arquitetura de software, desenvolvimento web e integração com banco de dados não relacional.

## Funcionalidades

- Tradução de textos entre diferentes idiomas.
- Possibilidade de escolher o idioma de origem e destino da tradução.
- Histórico de traduções.
- Interface amigável para facilitar o uso.

## Como funciona

A aplicação utiliza uma arquitetura em camadas MVC (Model-View-Controller) para organizar o código. O backend é desenvolvido em Python utilizando Flask para criar a aplicação server-side. O banco de dados não relacional MongoDB é utilizado para armazenar idiomas, usuários e o histórico de traduções.

## Bibliotecas utilizadas

- Flask: Framework web para Python.
- Pymongo: Driver Python para MongoDB.
- GoogleTranslator: API para tradução de textos.

## Como acessar a aplicação

Para acessar a aplicação, siga as instruções abaixo:

### Pré-requisitos

- Python 3 instalado no seu sistema.
- Docker (opcional, apenas se desejar utilizar o ambiente Dockerizado).

### Passos para execução

1. Clone este repositório:
```
git clone git@github.com:ronaldocipriiano/traduzo.git
```

2. Navegue até o diretório do projeto:
```
cd traduzo
```

3. Crie um ambiente virtual e ative-o (opcional, mas recomendado):
```
python3 -m venv .venv
source .venv/bin/activate
```

4. Instale as dependências:
```
python3 -m pip install -r dev-requirements.txt
```

5. Escolha uma das opções abaixo para iniciar a aplicação:

- Opção A (Docker): Banco e Flask pelo Docker
```
docker compose up translate
```

- Opção B (Docker): Banco pelo Docker, Flask localmente pelo ambiente virtual
```
docker-compose up -d mongodb
python3 src/app.py
```

6. Acesse a aplicação em seu navegador web:

http://127.0.0.1:8000/

 7. Populando o Banco de Dados com Idiomas

Para garantir que a aplicação tenha acesso aos idiomas necessários para realizar as traduções, é importante popular o banco de dados antes de iniciar a aplicação. Você pode fazer isso executando o seguinte comando, dependendo da opção escolhida anteriormente para executar a aplicação:

- Opção A (Docker): Banco e Flask pelo Docker
```
docker compose exec -it translate python3 src/run_seeds.py
```

- Opção B (Docker): Banco pelo Docker, Flask localmente pelo ambiente virtual
```
python3 src/run_seeds.py
```

Agora você pode utilizar a aplicação para traduzir seus textos!

## Contribuição

Contribuições são sempre bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
