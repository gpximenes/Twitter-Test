from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

def logar():
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    email = input("Digite seu email: ")
    driver.get("https://twitter.com/i/flow/login")
    sleep(10)
    input_email = driver.find_element(By.NAME, "text")
    input_email.send_keys(email)
    input_email.send_keys(Keys.RETURN)
    sleep(3)
    input_usuario = driver.find_element(By.NAME, "text")
    input_usuario.send_keys(Keys.RETURN)
    input_usuario.send_keys(usuario)
    sleep(3)
    input_usuario = driver.find_element(By.NAME, "password")
    input_usuario.send_keys(senha)
    input_usuario.send_keys(Keys.RETURN)
    sleep(5)
def acessar_configuracoes():
    botao_mais = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/div').click()
    sleep(2)
    botao_configurações = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[8]/a/div').click()
    sleep(1)

def mudar_idioma():
    botao_idioma_acessibilidade = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[1]/div[2]/div[2]/div[3]').click()
    sleep(1)
    botao_idiomas = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[1]/div[2]/div[2]/div[6]').click()
    sleep(1)
    idioma_de_exibicao = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[3]/div').click()
    sleep(1)
    botao_sair_sessoes = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/a[1]/div').click()
    sleep(1)
    botao_confirmar = driver.find_element(By.XPATH,'//*[@id="SELECTOR_1"]')
    botao_confirmar.click()
    botao_confirmar.send_keys('p')
    sleep(1)
    botao_confirmar.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[1]/div[1]/select/option[35]').click()
    sleep(1)
    botao_salvar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/div').click()

def verificar_teste():
    sleep(10)
    html = driver.find_element(By.XPATH,'/html')
    valor = html.get_attribute("lang")
    if(valor == "fa"):
        print('passou')
    else:
        print('falhou')
    sleep(1)
    driver.close()


logar()
acessar_configuracoes()
mudar_idioma()
verificar_teste()
