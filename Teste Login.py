
from lib2to3.pgen2 import driver
from telnetlib import EC
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Connection:
    slowmode = True
    
    default_url = 'https://twitter.com/'

    username = "WeekProgressBar"
    password = "Twitterbot34"

    def __init__(self):
        
        self.driver = self.get_driver()
        self.open_login_page(self.default_url)
        self.log_in()
        
        

    def get_driver(self):
        self.headless = False
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        
        if not self.headless:
            driver = webdriver.Chrome("C:\Códigos\ChromeDriver\chromedriver.exe")
        else:
            driver = webdriver.Chrome("C:\Códigos\ChromeDriver\chromedriver.exe", options=chrome_options)
        driver.set_window_size(550,700)       
        return driver

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
        xpath_login_field_big   = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input'
        while True:
            try:
                if self.driver.find_element_by_xpath(xpath_login_field_big).is_displayed:
                        xpath_login_field = xpath_login_field_big
                if self.driver.find_element_by_xpath(xpath_login_field_small).is_displayed:
                        xpath_login_field = xpath_login_field_small
            except:
                xpath_login_field = xpath_login_field_small
            try: 
                login_field = self.driver.find_element_by_xpath(xpath_login_field)
                login_field.send_keys(self.username)
                button_next = self.driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
                button_next.click()
                break
            except:
                time.sleep(3)

    def input_password(self):
        try:
            if self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input').is_displayed:
                self.input_username()
        except:
            pass

        while True:
            time.sleep(3)
            xpath_password_field = '/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
            password_field = self.driver.find_element_by_xpath(xpath_password_field)

            password_field.send_keys(self.password)

            xpath_auth_button = '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/span/span'
            auth_button = self.driver.find_element_by_xpath(xpath_auth_button)
            auth_button.click()    
            break   


    def log_in(self):
        
        self.click_log_in()
        self.input_username()
        self.input_password()
    

    def twettar(self,tweet):
        xpath_tweet_field = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div'
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH,xpath_tweet_field)))
        tweet_field = self.driver.find_element_by_xpath(xpath_tweet_field)
        tweet_field.send_keys(tweet)
        
        xpath_tweet_button = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span'
        tweet_button = self.driver.find_element_by_xpath(xpath_tweet_button)
        tweet_button.click()



controller = Connection()

controller.twettar("oi")

time.sleep(600)