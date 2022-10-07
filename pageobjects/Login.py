import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from toolium.pageobjects.page_object import PageObject


class LoginPageObjects(PageObject):

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.message_title = None
        self.message_error = None
        self.logout = None
        self.burger_menu = None
        self.message = None
        self.login_button = None
        self.password = None
        self.username = None
        ActionChains(self.driver)

    def open(self):
        self.driver.get('{}/'.format(self.config.get('Test', 'url')))
        return self

    def input_field(self):
        action = ActionChains(self.driver)
        self.username = self.driver.find_element(By.XPATH, "//input[@id='user-name']")
        action.click(self.username).send_keys('standard_user').perform()
        time.sleep(3)
        self.password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        action.click(self.password).send_keys('secret_sauce').perform()
        time.sleep(3)
        return self

    def login_input(self, user):
        self.username = InputText(By.XPATH, "//input[@id='user-name']")
        self.password = InputText(By.XPATH, "//input[@id='password']")
        self.username.text = user['username']
        time.sleep(3)
        self.password.text = user['password']
        time.sleep(3)

    def click(self):
        # ActionChains(self.driver)
        self.login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)
        return self

    def menu_burger(self):
        action = ActionChains(self.driver)
        self.burger_menu = Button(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        # action.move_to_element(self.burger_menu).click()
        time.sleep(2)

    def logout_btn(self):
        action = ActionChains(self.driver)
        self.logout = self.driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']")
        action.move_to_element(self.logout).click().perform()
        # self.logout.wait_until_visible()
        return self

    def get_message(self):
        # ActionChains(self.driver)
        self.message = self.driver.find_element(By.XPATH, "//span[@class='title']")
        return self.message.text

    def find_message(self):
        # ActionChains(self.driver)
        self.message = self.driver.find_element \
            (By.XPATH, "//div[@class='error-message-container error']")
        # self.message.wait_until_visible()
        return self.message.text

    def display(self):
        self.message_error = self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']")
        self.message_title = self.driver.find_element(By.XPATH, "//span[@class='title']")
        time.sleep(2)
        if self.message_error.is_enabled():
            return self.message_error.text
        time.sleep(2)
        if self.message_title.is_enabled():
            return self.message_title.text

    def wait_until_loaded(self):
        self.message.wait_until_visible()
        return self

