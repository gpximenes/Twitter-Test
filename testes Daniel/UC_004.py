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
    input_usuario.send_keys(usuario)
    input_usuario.send_keys(Keys.RETURN)
    sleep(3)
    input_usuario = driver.find_element(By.NAME, "password")
    input_usuario.send_keys(senha)
    input_usuario.send_keys(Keys.RETURN)
    sleep(5)
def mudar_para_profissional():
    botão_perfil = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
    sleep(3)
    botão_editar_perfil = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[2]/a').click()
    sleep(2)
    botão_profissional = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/a').click()
    sleep(5)
    botão_concordar = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div').click()
    sleep(5)
    bolinha_marcação = driver.find_element(By.NAME,'single-choice').click()
    sleep(2)
    botao_avancar = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
    sleep(2)
    selecionar_criador = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div[2]').click()
    sleep(0.5)
    botao_avancar2 = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div').click()
    #Procurar a string 'Bem-vindo ao Twitter para Profissionais'
def verificar_teste():
    sleep(5)
    confirmação = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[1]').text
    if(confirmação == "Bem-vindo ao Twitter para Profissionais"):
        print("passou")
    else:
        print("falhou")
    sleep(0.5)
    driver.close()

logar()
mudar_para_profissional()
verificar_teste()
