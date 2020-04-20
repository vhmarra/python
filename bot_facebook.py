from selenium import webdriver #pip install seleium 
                               #chrome webdrives has to be on python path
from time import sleep


class bot_loga_face():
    def __init__(self):
        self.options = webdriver.ChromeOptions()#---------------------------------------------------------------|
        self.options.add_argument("--incognito")#---------------------------------------------------------------|SET GOOGLE CHROME TO INCOGNITO MODE
        self.driver = webdriver.Chrome(options=self.options)#---------------------------------------------------|
        self.driver.get('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110')#--|OPEN FACEBOOK WEB PAGE
        self.driver.find_element_by_name("email")\
            .send_keys('EMAIL HERE') #FILL EMAIL FORM
        self.driver.find_element_by_name("pass")\
            .send_keys('PASSWORD HERE') # FILL PSWD FORM
        self.driver.find_element_by_name("login")\
            .click() #CLICK ON LOGIN BUTTON


bot = bot_loga_face()
