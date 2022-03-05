
#driver.close() fechar navegador
#drive.find_element_by_xpath buscar elemento
#elem.send_keys("pycon") escrever
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

class Fazer_login:

    def logar_conta():
        usuario = input("Digite seu usuario: ")
        senha = input("Digite sua senha: ")
        email = input("Digite seu email: ")
        #driver.get('https://www.hashtagtreinamentos.com/automacao-web-no-python')
        driver.get("https://twitter.com/i/flow/login")
        sleep(5)
        input_email = driver.find_element(By.NAME, "text")
        email = "danyv7818@gmail.com"#input("Email:")
        input_email.send_keys(email)
        input_email.send_keys(Keys.RETURN)
        sleep(2)
        input_usuario = driver.find_element(By.NAME, "text")
        usuario = "98991045626"#input("Usuario:")
        input_usuario.send_keys(usuario)
        input_usuario.send_keys(Keys.RETURN)
        sleep(2)
        input_usuario = driver.find_element(By.NAME, "password")
        senha = "dany5260818"#input("Senha:")
        input_usuario.send_keys(senha)
        input_usuario.send_keys(Keys.RETURN)

bnt = Fazer_login
bnt.logar_conta()
