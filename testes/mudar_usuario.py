from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
#import Login
driver = webdriver.Firefox()


def logar():
    driver.get("https://twitter.com/i/flow/login")
    usuario = "@danyvazquez69"#input("Digite seu usuario: ")
    global senha
    senha = "mamaco007"#input("Digite sua senha: ")
    email = "danyv7818@gmail.com"#input("Digite seu email: ")
    sleep(2)
    driver.implicitly_wait(10)
    input_email = driver.find_element(By.NAME, "text")
    input_email.send_keys(email)
    input_email.send_keys(Keys.RETURN)
    sleep(2)
    input_usuario = driver.find_element(By.NAME, "text")
    input_usuario.send_keys(usuario)
    input_usuario.send_keys(Keys.RETURN)
    sleep(2)
    input_usuario = driver.find_element(By.NAME, "password")
    input_usuario.send_keys(senha)
    input_usuario.send_keys(Keys.RETURN)
    print("Login com sucesso")
def mudar_usuario_():
    driver.implicitly_wait(10)
    global novo_usuario
    novo_usuario = "mamaco0007"#input("Qual o novo nome de usuario desejado: ")
    sleep(2)
    driver.implicitly_wait(10)
    botao_mais = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/div').click()
    sleep(2)
    botao_configurações = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[8]/a/div').click()
    sleep(1)
    botao_suaconta = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[1]/div[2]/div[2]/div[1]').click()
    sleep(1)
    botao_informacoesdaconta = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/div[2]').click()
    sleep(1)
    input_senha = driver.find_element(By.NAME,'current_password')
    input_senha.click()
    input_senha.send_keys(senha)
    sleep(1)
    botao_confirmar = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[4]/div').click()
    sleep(1)
    botao_nome_usuario = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div/a[1]/div').click()
    sleep(1)
    input_usuario = driver.find_element(By.NAME,'typedScreenName')
    input_usuario.clear()
    input_usuario.send_keys(novo_usuario)
    sleep(1)
    botao_salvar = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/section[2]/div[2]/div[3]/div").click()
def verificar_teste():
    sleep(2)
    driver.implicitly_wait(10)
    botão_perfil = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div').click()
    sleep(5)
    nome_usuario = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/div/div[2]/div/span').text
    print(f"Usuario informado:{nome_usuario}")
    print(f"Usuario atual:@{novo_usuario}")
    if (nome_usuario == f"@{novo_usuario}"):
        print("teste ok")
    else:
        print('teste com erros')
    sleep(5)
    driver.close()

try:
    logar()
    mudar_usuario_()
    verificar_teste()
except Exception as e:
    print("Elemento falhou em caregar")
