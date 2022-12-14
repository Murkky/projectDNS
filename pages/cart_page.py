import allure
from seleniumpagefactory.Pagefactory import PageFactory

from utilities.logger import Logger


class CartPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    locators = {
        'navigate_to_checkout_button': ('XPATH', '//button[@id="buy-btn-main"]')
    }

    def click_navigate_to_checkout_button(self):
        self.navigate_to_checkout_button.click_button()
        print("Click Checkout Button")

    def checkout(self):
        with allure.step('Checkout'):
            Logger.add_start_step(method='checkout')
            self.click_navigate_to_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='checkout')

