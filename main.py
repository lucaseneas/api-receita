from fastapi import FastAPI
from botChrome import botChrome

app = FastAPI()

@app.get("/")
def home():
    return "API no ar"

@app.get("/das/{cnpj_recebido}/{ano_recebido}/{mes_recebido}")
def pegar_mes2(cnpj_recebido: str, ano_recebido: str, mes_recebido: str):
    bot = botChrome(cnpj_recebido,ano_recebido,mes_recebido)
    return bot.bot()
