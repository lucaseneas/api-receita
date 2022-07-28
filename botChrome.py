from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from conversor import data
from enviarEmail import enviarEmail

# uvicorn main:app --reload

# 36474098000166

# 2020 = 5
# 2021 = 6
# 2022 = 7

# Janeiro = 2
# Fevereiro = 3
# Março = 4
# Abril = 5
# Maio = 6
# junho = 7
# Julho = 8
# Agosto = 9
# Setembro = 10
# Outubto = 11
# Novembro = 12
# Dezembro = 13

class botChrome:
    def __init__(self, cnpj_recebido, ano_recebido, mes_recebido, email_recebido):
            self.cnpj_recebido = cnpj_recebido
            self.ano_recebido = ano_recebido
            self.mes_recebido = mes_recebido
            self.email_recebido = email_recebido

    def bot(self):
            conversor = data(self.mes_recebido, self.ano_recebido)

            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(options=chrome_options)

            driver.get('https://www8.receita.fazenda.gov.br/SimplesNacional/aplicacoes.aspx?id=19')
            driver.switch_to.frame("frame")

            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="cnpj"]').send_keys(self.cnpj_recebido)
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="continuar"]').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/ul[1]/li[2]/a').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '/html/body/div/section[3]/div/div/div/div/div/form/div/div/button').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH,
                                       '/html/body/div/section[3]/div/div/div/div/div/form/div/div/div/ul/li[' + conversor.converterAno() + ']').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '/html/body/div/section[3]/div/div/div/div/div/form/button').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="resumoDAS"]/table/tbody[' + conversor.converterMes() + ']/tr/td[1]/input').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="btnEmitirDas"]').click()
            time.sleep(2)
            elem = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/section[3]/div/div/div[1]/div/div/div[3]/div/div/a[1]').click()
            time.sleep(2)

            email = enviarEmail(self.cnpj_recebido, conversor.dataFormatada(), self.email_recebido)
            email.enviar()
            return "Download realizado com sucesso CNPJ: "+self.cnpj_recebido + " referente a " + conversor.dataFormatada() + ", o arquivo sera enviado ao email " + self.email_recebido


