import time
import allure
from seleniumpagefactory.Pagefactory import PageFactory
from pages.base_methods import Base
from utilities.logger import Logger


class CheckoutPage(PageFactory, Base):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    locators = {
        'authorization_button': ('XPATH', '//a[@class="base-login-button__link_LYc"]'),
        'login_with_password': ('XPATH', '//div[@class="block-other-login-methods__password-caption"]'),
        'username_input_field': ('XPATH', '//input[@autocomplete="username"]'),
        'password_input_field': ('XPATH', '//input[@type="password"]'),
        'login_button': ('XPATH', '//div[@class="base-main-button"]'),
        'logged_in_tick': ('XPATH', '//span[contains(@class,"icon_check_xRi")]')
    }

    def click_authorization_button(self):
        self.authorization_button.click_button()
        print("Click Authorization Button")

    def click_login_with_password(self):
        self.login_with_password.click_button()
        print("Select Login With Password")

    def set_authorization(self):
        self.username_input_field.set_text('tests.popovich@gmail.com')
        self.password_input_field.set_text('Test1234')
        self.login_button.click_button()
        time.sleep(10)
        print("Set Authorization")

    def is_tick_displayed(self):
        return self.logged_in_tick.is_displayed()

    def user_authorization(self):
        with allure.step('User Authorization'):
            Logger.add_start_step(method='user_authorization')
            self.click_authorization_button()
            self.click_login_with_password()
            self.set_authorization()
            self.screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='user_authorization')
