from fastapi import FastAPI
from botChrome import botChrome

app = FastAPI()

@app.get("/")
def home():
    return "API funcionando normalmente"

@app.get("/das/{cnpj_recebido}/{ano_recebido}/{mes_recebido}/{email_recebido}")
def recolherDas(cnpj_recebido: str, ano_recebido: str, mes_recebido: str, email_recebido: str):
    bot = botChrome(cnpj_recebido,ano_recebido,mes_recebido, email_recebido)
    return bot.bot()
