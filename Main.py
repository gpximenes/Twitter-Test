import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Connection:    
    default_url = 'https://twitter.com/'

    username = "WeekProgressBar"
    password = "Twitterbot34"
    email = 'professorgabrielx@gmail.com'
    phone = '+5598981724676'

    def __init__(self):
        
        self.driver = self.get_driver()
        self.open_login_page(self.default_url)
        
        

    def get_driver(self):
        self.headless = False
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('log-level=3')
        
        if not self.headless:
            driver = webdriver.Chrome("C:\Códigos\ChromeDriver\chromedriver.exe")
        else:
            driver = webdriver.Chrome("C:\Códigos\ChromeDriver\chromedriver.exe", options=chrome_options)
        driver.set_window_size(600,600)       
        return driver

    def close_windows(self):
        self.driver.quit()

    def open_login_page(self,url):
        self.driver.get(url)


    def click_log_in(self):
        try:
            xpath_sign_in = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div'
        except:
            xpath_sign_in = '//*[@id="layers"]/div/div[1]/div/div/div/div[1]/a/div/span/span'
        while True:
            try:
                
                button_sign_in = self.driver.find_element_by_xpath(xpath_sign_in)
                button_sign_in.click()
                break
            except:
                time.sleep(3)




    
    def input_username(self):
        xpath_login_field_small = "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input"
        #xpath_login_field_big   = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
        while True:
            try: 
                login_field = self.driver.find_element_by_xpath(xpath_login_field_small)
                login_field.send_keys(self.username)
                button_next = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
                button_next.click()
                break
            except:
                time.sleep(3)


    def input_email(self):
        xpath_login_field_small = "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input"
        while True:
            try: 
                login_field = self.driver.find_element_by_xpath(xpath_login_field_small)
                login_field.send_keys(self.email)
                button_next = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
                button_next.click()
                break
            except:
                time.sleep(3)
        time.sleep(3)
        xpath_confirm_id = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input'
        selector_confirm_id = '#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input'
        try:
            confirm_id_button = self.driver.find_element_by_xpath(xpath_confirm_id)
        except:
            confirm_id_button = self.driver.find_element_by_css_selector(selector_confirm_id)
        confirm_id_button.send_keys(self.username)

        xpath_confirm_id_next = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div'
        confirm_id_next = self.driver.find_element_by_xpath(xpath_confirm_id_next)
        confirm_id_next.click()

    def input_email_invalid(self,email):
        xpath_login_field_small = "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input"
        while True:
            try: 
                login_field = self.driver.find_element_by_xpath(xpath_login_field_small)
                login_field.send_keys(email)
                button_next = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
                button_next.click()
                break
            except:
                time.sleep(3)
        time.sleep(3)
        xpath_confirm_id = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input'
        selector_confirm_id = '#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input'
        try:
            confirm_id_button = self.driver.find_element_by_xpath(xpath_confirm_id)
        except:
            confirm_id_button = self.driver.find_element_by_css_selector(selector_confirm_id)
        confirm_id_button.send_keys(self.username)


        xpath_error = '//*[@id="react-root"]/div/div/div'
        error = self.driver.find_element_by_xpath(xpath_error)
        if  error.is_displayed and error.is_enabled:
            print("Erro: Conta não localizada")
            return

        xpath_confirm_id_next = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div'
        confirm_id_next = self.driver.find_element_by_xpath(xpath_confirm_id_next)
        confirm_id_next.click()

    def input_login_admin(self):
        xpath_login_field_small = "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input"
        while True:
            try: 
                login_field = self.driver.find_element_by_xpath(xpath_login_field_small)
                login_field.send_keys("admin")
                button_next = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
                button_next.click()
                break
            except:
                time.sleep(3)
        time.sleep(3)

        while True:
            try:
                time.sleep(3)
                xpath_password_field = '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
                password_field = self.driver.find_element_by_xpath(xpath_password_field)

                password_field.send_keys("admin")

                xpath_auth_button = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/span/span'
                auth_button = self.driver.find_element_by_xpath(xpath_auth_button)
                auth_button.click()    
                break
            except:
                break    





        xpath_confirm_id = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input'
        selector_confirm_id = '#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-13qz1uu > div.css-1dbjc4n.r-8w3o46.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input'
        try:
            confirm_id_button = self.driver.find_element_by_xpath(xpath_confirm_id)
        except:
            confirm_id_button = self.driver.find_element_by_css_selector(selector_confirm_id)
        confirm_id_button.click()

        xpath_confirm_id_next = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div'
        confirm_id_next = self.driver.find_element_by_xpath(xpath_confirm_id_next)
        confirm_id_next.click()


        xpath_error = '//*[@id="react-root"]/div/div/div'
        error = self.driver.find_element_by_xpath(xpath_error)
        if  error.is_displayed and error.is_enabled:
            print("Erro: Conta não localizada")



    def input_phone(self):
        xpath_login_field_small = "/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input"
        while True:
            try: 
                login_field = self.driver.find_element_by_xpath(xpath_login_field_small)
                login_field.send_keys(self.phone)
                button_next = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
                button_next.click()
                break
            except:
                time.sleep(3) 

        try:
            self.input_password()
        except:
            xpath_error = '//*[@id="react-root"]/div/div/div'
            error = self.driver.find_element_by_xpath(xpath_error)
            if  error.is_displayed and error.is_enabled:
                print("TESTE Erro: Conta não localizada")



    def input_password(self):
        # try:
        #     if self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input').is_displayed and self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input').is_enabled:
        #         self.input_username()
        # except:
        #     pass

        while True:
            try: 
                time.sleep(3)
                xpath_password_field = '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
                password_field = self.driver.find_element_by_xpath(xpath_password_field)

                password_field.send_keys(self.password)

                xpath_auth_button = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/span/span'
                auth_button = self.driver.find_element_by_xpath(xpath_auth_button)
                auth_button.click()    
                break   
            except:
                break


    def log_in(self, mode):
        
        if mode == 1:
            self.click_log_in()
            self.input_username()
            self.input_password()

        if mode == 2:
            self.click_log_in()
            self.input_email()
            self.input_password()

        if mode == 3:
            self.click_log_in()
            self.input_login_admin()
            self.input_password()

        if mode == 4:
            self.click_log_in()
            self.input_email_invalid("eu@eu.com")

        if mode == 5:
            self.click_log_in()
            self.input_phone()    
        

        #self.input_username()
        #self.input_email()
        #self.input_email_invalid("eu@eu.com")
        #self.input_phone()   # COM ERRO DO TWITTER
        #self.input_login_admin()


        try:
            time.sleep(3)
            xpath_header = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/h2/span'
            #selector_header = '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-aqfbo4.r-gtdqiz.r-1gn8etr.r-1g40b8q > div.css-1dbjc4n.r-1loqt21.r-136ojw6 > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1pi2tsx.r-1777fci > div > h2 > span'
            header = self.driver.find_element_by_xpath(xpath_header)
            if header.text == 'Página Inicial':
                print("TESTE: Logado com sucesso!")
                self.driver.set_window_size(800,800)  
        except:
            print("TESTE: Erro no login")

    def twettar(self,tweet):
        xpath_tweet_field = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,xpath_tweet_field)))
        tweet_field = self.driver.find_element_by_xpath(xpath_tweet_field)
        tweet_field.send_keys(tweet)
        
        xpath_tweet_button = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'
        tweet_button = self.driver.find_element_by_xpath(xpath_tweet_button)
        tweet_button.click()
        time.sleep(1)
        selector_tweet_was_sent = 'div > div > div > div.css-901oao.r-jwli3a.r-1wbh5a2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-1e081e0.r-qvutc0 > span'
        tweet_was_sent = self.driver.find_element_by_css_selector(selector_tweet_was_sent)
        if  tweet_was_sent.is_displayed and tweet_was_sent.text == "Seu Tweet foi enviado.":
            print("TESTE: Tweet Enviado com sucesso!")

        try:
            time.sleep(2)
            selector_already_said_that = '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-ymttw5.r-1f1sjgu > div > div > div > div > span'
            already_said_that = self.driver.find_element_by_css_selector(selector_already_said_that)
            if already_said_that.is_displayed:
                print("TESTE: Não é possível twittar o mesmo conteúdo duas vezes")
                return
        except:
            return

    def twettar_long(self,tweet):
        xpath_tweet_field = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,xpath_tweet_field)))
        tweet_field = self.driver.find_element_by_xpath(xpath_tweet_field)
        tweet_field.send_keys(tweet)
        
        xpath_tweet_button = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'
        tweet_button = self.driver.find_element_by_xpath(xpath_tweet_button)
        try:
            WebDriverWait(self.driver,2).until(EC.element_to_be_clickable((By.XPATH,tweet_button)))
            print("TESTE: É possível twittar")
        except:
            print("TESTE: Não é possível twittar com essa quantidade de caracteres")

 

        


    def create_pool(self):
        selector_pool_button = '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div.css-1dbjc4n.r-14lw9ot.r-184en5c > div > div.css-1dbjc4n.r-14lw9ot.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(1) > div:nth-child(4) > div > svg'
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR,selector_pool_button)))
        pool_button = self.driver.find_element_by_css_selector(selector_pool_button)

        pool_button.click()

        time.sleep(3)
        xpath_choice1 = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div/label/div/div[2]/div/input'
        choice1 = 'verde'

        choice1_field = self.driver.find_element_by_xpath(xpath_choice1)
        choice1_field.send_keys(choice1)

        xpath_choice2 = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/label/div/div[2]/div/input'        
        choice2 = 'azul'
        choice2_field = self.driver.find_element_by_xpath(xpath_choice2)
        choice2_field.send_keys(choice2)


        xpath_title = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div'
        title_field = self.driver.find_element_by_xpath(xpath_title)
        tile_text = 'Qual a melhor cor?'
        title_field.send_keys(tile_text)

        
        xpath_tweet_button = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'
        tweet_button = self.driver.find_element_by_xpath(xpath_tweet_button)
        tweet_button.click()


        print("Enquete criada com sucesso.")
        time.sleep(2)


    def search(self,search):
        selector_search_button = '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div:nth-child(1) > div.css-1dbjc4n.r-1awozwy.r-15zivkp.r-1bymd8e.r-13qz1uu > nav > a:nth-child(2) > div > div > svg'
        search_button = self.driver.find_element_by_css_selector(selector_search_button)
        search_button.click()

        xpath_search_bar = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,xpath_search_bar)))
        search_bar = self.driver.find_element_by_xpath(xpath_search_bar)
        search_bar.send_keys(search)
        search_bar.send_keys(Keys.ENTER)

        selector_account_not_found = '#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div > div > div:nth-child(2) > div > div > div > div.css-901oao.r-18jsvk2.r-37j5jr.r-1yjpyg1.r-1vr29t4.r-ueyrd6.r-5oul0u.r-bcqeeo.r-fdjqy7.r-qvutc0 > span'
        try:
            time.sleep(3)
            account_not_found = self.driver.find_element_by_css_selector(selector_account_not_found)
            print("TESTE: Conta não encontrada")
        except:
            print("TESTE: Conta encontrada")




