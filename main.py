from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

# INSTAGRAM INFO
# # CREDENTIALS
INSTA_PASSWORD = 'Pass goes here'
INSTA_USERNAME = 'username goes here'
# ^ Add your own password and username here
# # SIMILAR ACCOUNT
SIMILAR_ACCOUNT = 'shaznazbot'
# ^ This is the target account, add any accounts username

# Selenium info
chrome_driver_path = '/Users/shahbaznaziri/Desktop/Web development/chromedriver'


class InstaFollowers:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(4)
        username_box = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_box.send_keys(INSTA_USERNAME)
        password_box = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_box.send_keys(INSTA_PASSWORD)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()

        # Sometimes the notification pop up opens up, this is to close it
        try:
            time.sleep(6)
            pop_up_button = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            pop_up_button.click()

        except NoSuchElementException:
            print('NO POP-UP')
            pass


    def find_followers(self):
        time.sleep(2)
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        time.sleep(4)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(0,15):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector('li button')
        for button in all_buttons:
            try:
                time.sleep(2)
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollowers()

bot.login()
bot.find_followers()
bot.follow()
