# b2bflow-desafio-supabase
Este projeto foi proposto pela b2bflow como desafio. O objetivo é criar um código em Python capaz de ler cadastros no Supabase e enviar uma mensagem via Z-API.

# Na Supabase

(Atenção: os nomes dos campos devem estar escritos como abaixo, optei por usar Maiúsculo no inicio para melhor organização da tabela)

Nome da Tabela :"Contatos"   
Colunas : Nome e Número 

# No arquivo .env

Crie um arquivo .env na raiz do projeto:

Preencher conforme descrito

SUPABASE_URL=sua_url_aqui
SUPABASE_KEY=sua_key_aqui

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token

# Requisitos

Caso não tenha todas as bibliotecas, execute o código abaixo:
pip install -r requirements.txt

# Executar

Por fim, execute o arquivo main.py
