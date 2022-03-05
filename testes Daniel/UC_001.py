from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from datetime import date
driver = webdriver.Firefox()

def logar():
    driver.get("https://twitter.com/i/flow/login")
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    email = input("Digite seu email: ")
    sleep(2)
    driver.implicitly_wait(10)
    input_email = driver.find_element(By.NAME, "text")
    input_email.send_keys(email)
    input_email.send_keys(Keys.RETURN)
    sleep(3)
    input_usuario = driver.find_element(By.NAME, "text")
    input_usuario.send_keys(usuario)
    input_usuario.send_keys(Keys.RETURN)
    sleep(3)
    input_usuario = driver.find_element(By.NAME, "password")
    input_usuario.send_keys(senha)
    input_usuario.send_keys(Keys.RETURN)
    sleep(5)
    print("Login com sucesso")
def programar_tweet():
    data_atual = date.today()
    botao_programar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[5]/div').click()
    sleep(1)
    seletor_ano = driver.find_element(By.ID,'SELECTOR_3')
    sleep(1)
    seletor_ano.click()
    sleep(1)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/select/option[2]').click()
    sleep(2)
def verificar_teste():
    sleep(5)
    confirmacao = driver.find_element(By.XPATH,'//*[@id="DATE_INPUT_1_ERROR"]').text
    print(f"Resposta do sistema: {confirmacao}")
    if(confirmacao == "Não é possível programar um Tweet com mais de 18 meses de antecedência."):
        print("Teste Passou")
    else:
        print("Teste Falhou")
    sleep(0.5)
    driver.close()

try:
    logar()
    programar_tweet()
    verificar_teste()
except Exception as e:
    print("Elemento demorrou a carregar")
