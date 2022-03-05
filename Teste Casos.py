from Main import Connection
from time import sleep

def Testar(caso):
    controller = Connection()

    #Log in com email
    if caso == 1:
        controller.log_in(2)
        controller.close_windows()

    #Log in com username
    if caso == 2:
        controller.log_in(1)
        controller.close_windows()

    #Log in com email invalido
    if caso == 3:
        controller.log_in(4)
        controller.close_windows()

    #Log in com user admin senha admin
    if caso == 4:
        controller.log_in(3)
        controller.close_windows()

    #Criar enquete
    if caso == 5:
        controller.log_in(1)
        controller.create_pool()
        controller.close_windows()

    #Pesquisar conta não existente
    if caso == 6:
        controller.log_in(1)
        controller.search("wubalubadubdub123123577345")
        controller.close_windows()

    #Twettar
    if caso == 7:
        controller.log_in(1)
        controller.twettar("Esse é um tweet automatizado")
        controller.close_windows()

    #Twettar com mais de 280 caracteres
    if caso == 8:
        lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate '
        controller.log_in(1)
        controller.twettar_long(lorem_ipsum)
        controller.close_windows()

     #Tweetar duas vezes o mesmo conteúdo 
    if caso == 9:
        controller.log_in(1)
        controller.twettar("Esse é um tweet automatizad")
        sleep(10)
        controller.twettar("Esse é um tweet automatizad")

        controller.close_windows()
        


    #Log in com telefone
    if caso == 10:
        controller.log_in(5) 
        controller.close_windows()


i = 10
while i <=10:    
    Testar(1)
    i +=1 

