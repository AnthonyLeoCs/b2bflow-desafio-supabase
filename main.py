# Imports

from supabase import create_client
from dotenv import load_dotenv
import os
import requests

# Estabelecendo link com o .env

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Estabelecendo Link com o Zapi

inst_id = os.getenv("ZAPI_INSTANCE_ID")
z_token = os.getenv("ZAPI_TOKEN")
client_token = os.getenv("ZAPI_CLIENT_TOKEN")
Z_url = f"https://api.z-api.io/instances/{inst_id}/token/{z_token}/send-text"


# Coletando os dados

supabase = create_client(url, key)
response = supabase.table("Contatos").select("*").limit(2).execute()


# Enviando mensagem para os contatos

for contato in response.data:
    nome = contato["Nome"]
    numero = contato["Número"]

    print(nome)
    print(numero)

    msg = f"Olá, {nome} tudo bem?"

    dados = {
        "phone": numero,
        "message": msg
    }

    headers = {
        "Client-Token": client_token
    }

    resposta_zapi = requests.post(
        Z_url,
        json=dados,
        headers=headers
    )



