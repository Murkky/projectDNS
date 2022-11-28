import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    request.cls.driver = chrome_driver
    chrome_driver.get('https://www.dns-shop.ru/')
    yield
    chrome_driver.quit()


@pytest.mark.usefixtures("chrome_driver_init")
class BasicTest:
    pass


class TestURL(BasicTest):
    def test_open_url(self):
        mp = MainPage(self.driver)
        plp = ProductListPage(self.driver)
        pp = ProductPage(self.driver)
        cp = CartPage(self.driver)
        chp = CheckoutPage(self.driver)

        mp.select_category()
        plp.selected_product()
        pp.buy_product()
        cp.checkout()
        chp.user_authorization()
        assert chp.is_tick_displayed() == True
