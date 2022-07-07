from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from conversor import date

class botChrome:
    def __init__(self, cnpj_recebido2, ano_recebido2, mes_recebido2 ):
            self.cnpj_recebido = cnpj_recebido2
            self.ano_recebido = ano_recebido2
            self.mes_recebido = mes_recebido2

    def bot(self):
            #36474098000166
            cnpj_do_cliente = self.cnpj_recebido

            ano = self.ano_recebido
            # 2020 = 5
            # 2021 = 6
            # 2022 = 7

            mes = self.mes_recebido
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

            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            driver = webdriver.Chrome(options=chrome_options)

            driver.get('https://www8.receita.fazenda.gov.br/SimplesNacional/aplicacoes.aspx?id=19')
            driver.switch_to.frame("frame")

            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="cnpj"]').send_keys(cnpj_do_cliente)
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="continuar"]').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="navbarCollapse"]/ul[1]/li[2]/a').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '/html/body/div/section[3]/div/div/div/div/div/form/div/div/button').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH,
                                       '/html/body/div/section[3]/div/div/div/div/div/form/div/div/div/ul/li[' + ano + ']').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '/html/body/div/section[3]/div/div/div/div/div/form/button').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="resumoDAS"]/table/tbody[' + mes + ']/tr/td[1]/input').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH, '//*[@id="btnEmitirDas"]').click()
            time.sleep(1)
            elem = driver.find_element(By.XPATH,
                                       '/html/body/div[1]/section[3]/div/div/div[1]/div/div/div[3]/div/div/a[1]').click()
            time.sleep(2)

            newDate = date(mes, ano)
            dataFormatando = newDate.formated()
            return "Download realizado com sucesso CNPJ: "+self.cnpj_recebido+" "+dataFormatando