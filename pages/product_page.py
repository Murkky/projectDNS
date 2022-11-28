import allure
from seleniumpagefactory.Pagefactory import PageFactory
from pages.base_methods import Base
from utilities.logger import Logger


class ProductPage(PageFactory, Base):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    locators = {
        'add_to_cart': ('XPATH', '//div[@class="product-buy product-buy_one-line"]/button[contains(@class,"button-ui buy")]'),
        'cart_icon': ('XPATH', '//a[@class="ui-link cart-link"]'),
        'to_cart': ('XPATH', '//span[text()="В корзину"]'),
        'cart_word': ('XPATH', '//h1[@class="cart-title"]')
    }

    def click_add_to_cart(self):
        self.add_to_cart.click_button()
        print("Add Product To Cart")

    def hover_cart_icon(self):
        self.cart_icon.hover()
        print("Mouseover Cart Icon")

    def click_to_cart(self):
        self.to_cart.click_button()
        print("Click To Cart")

    def get_cart_word_text(self):
        return self.cart_word.get_text()

    def buy_product(self):
        with allure.step('Buy Product'):
            Logger.add_start_step(method='buy_product')
            self.click_add_to_cart()
            self.hover_cart_icon()
            self.click_to_cart()
            self.assert_word(self.get_cart_word_text(), 'Корзина')
            Logger.add_end_step(url=self.driver.current_url, method='buy_product')

