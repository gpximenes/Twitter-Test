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
def acessar_perfil():
    botão_perfil = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
    sleep(5)
def fixar_tweet():
    _3_pontinhos = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div').click()
    sleep(0.5)
    print("Achou 3 pontinhos")
    botao_fixar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[2]').click()
    sleep(1)
    botao_confirmar = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]').click()
    #procurar a string:"seu tweet foi fixado ao seu perfil"
def verificar_teste():
    sleep(5)
    confirmação = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[1]/div/div/article/div/div/div/div[1]/div/div/div/div/div[2]').text
    if(confirmação == "Tweet Fixado"):
        print("passou")
    else:
        print("falhou")
    sleep(0.5)
    driver.close()


logar()
acessar_perfil()
fixar_tweet()
verificar_teste()
