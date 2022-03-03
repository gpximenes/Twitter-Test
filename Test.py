import tweepy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




class Connection:
    consumer_key = 'mGah36SFG4RZsq3grtjOuFppV'
    consumer_secret = 'i6FSeyTj0hhrA3d78z1s19yIuIcCPaNMkPBWPqNaopbLui1TpV'
    callback_uri = 'oob'

    username = "WeekProgressBar"
    password = "Twitterbot34"

    def __init__(self):
        
        self.auth = self.get_auth()
        self.driver = self.get_driver()
        self.open_login_page = self.open_login_page(self.auth)
        self.log_in()
        self.get_code()
        self.api = self.create_api(self.auth)

    def get_auth(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret, self.callback_uri)
        return auth

    def get_url(self, auth):
        redirect_url = auth.get_authorization_url()
        return redirect_url

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
        return driver

    def open_login_page(self, auth):
        self.driver.get(self.get_url(auth))

    def log_in(self):
        login_field = self.driver.find_element_by_id("username_or_email")
        login_field.send_keys(self.username)

        password_field = self.driver.find_element_by_id("password")
        password_field.send_keys(self.password)

        auth_button = self.driver.find_element_by_id("allow")
        auth_button.click()

    def get_code(self):
        code = self.driver.find_element_by_xpath('//*[@id="oauth_pin"]/p/kbd/code').text
        user_pin_input = code
        return user_pin_input

    def create_api(self, auth):

        code = self.get_code()
        auth.get_access_token(code)
        bridge = tweepy.API(self.auth)
        return bridge





def tweet_percentage_past():
    api = Connection()
    tweet = f"Teste"
    api.api.update_status(tweet)
    #tweet_percentage_past(api)
    return print(tweet)
    
tweet_percentage_past()