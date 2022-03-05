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
    sleep(2)
    input_usuario = driver.find_element(By.NAME, "text")
    input_usuario.send_keys(email)
    input_usuario.send_keys(Keys.RETURN)
    sleep(2)
    input_usuario = driver.find_element(By.NAME, "password")
    input_usuario.send_keys(senha)
    input_usuario.send_keys(Keys.RETURN)
    sleep(5)
def excluir_tweet_programado():
    botao_programar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]/div[5]/div').click()
    sleep(1)
    botão_programados = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div').click()
    sleep(1)
    botão_editar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/div/div/div[3]/div/div').click()
    sleep(1)
    botao_marcar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[1]/div').click()
    sleep(1)
    botao_excluir = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]').click()
    sleep(1)
    botao_confirmar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]').click()
def verificar_teste():
    sleep(3)
    confirmação = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div[1]').text
    if(confirmação == "Você não tem nenhum Tweet programado"):
        print("passou")
    else:
        print("falhou")
    sleep(0.5)
    driver.close()

logar()
excluir_tweet_programado()
verificar_teste()
