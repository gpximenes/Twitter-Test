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
    input_email.send_keys(usuario)
    input_email.send_keys(Keys.RETURN)
    sleep(3)
    input_usuario = driver.find_element(By.NAME, "text")
    input_usuario.send_keys(email)
    input_usuario.send_keys(Keys.RETURN)
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
def desativar_conta():
    botao_desativar = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[6]').click()
    sleep(1)
    botao_desativar2 = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[11]/div').click()
    sleep(1)
    input_senha = driver.find_element(By.NAME,'current_password')
    input_senha.click()
    input_senha.send_keys('senha')
    sleep(1)
    botao_confirmar = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[5]/div').click()
    sleep(1)

logar()
acessar_configuracoes()
desativar_conta()
