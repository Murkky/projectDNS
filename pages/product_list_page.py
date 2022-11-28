import time
from seleniumpagefactory.Pagefactory import PageFactory
from pages.base_methods import Base


class ProductListPage(PageFactory, Base):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    locators = {
        'price_filter': ('XPATH', '//span[text()="301 - 500 ₽  "]/../span[contains(@class,"ui-checkbox__box")]'),
        'vendor_filter': ('XPATH', '//span[text()="DEXP  "]/../span[contains(@class,"ui-checkbox__box")]'),
        'apply_filters': ('XPATH', '//button[@class="button-ui button-ui_brand left-filters__button"]'),
        'sort_products_by': ('XPATH', '//div[@data-id="order"]/a[@class="ui-link ui-link_blue"]'),
        'sorting_products': ('XPATH', '//span[text()="Сначала популярные"]'),
        'select_product': ('XPATH', '//div[@data-id="product"][1]/a')
    }

    def click_filters(self):
        self.price_filter.click_button()
        self.vendor_filter.click_button()
        self.apply_filters.click_button()
        print("Click Filters")

    def click_sort_products(self):
        self.sort_products_by.click_button()
        self.sorting_products.click_button()
        time.sleep(3)
        print("Apply Sort Products")

    def click_name_product(self):
        self.select_product.click_button()

    def selected_product(self):
        self.assert_url('https://www.dns-shop.ru/catalog/17a8a26516404e77/kabeli-dlya-mobilnyx-ustrojstv/')
        self.driver.execute_script("window.scroll(0,500)")
        self.click_filters()
        self.driver.execute_script("window.scroll(0,0)")
        self.click_sort_products()
        self.click_name_product()
