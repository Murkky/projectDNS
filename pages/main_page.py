# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import ActionChains
# from src.pages.base_methods import Base
from seleniumpagefactory.Pagefactory import PageFactory


class MainPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    locators = {
        'main_category': ('XPATH', '//a[@href="/catalog/17a890dc16404e77/smartfony-i-fototexnika/"]'),
        'drop_category_1': ('XPATH', '//a[@href="/catalog/17a9ab6516404e77/zaryadka-i-podklyuchenie/"]'),
        'drop_category_2': ('XPATH', '//a[@href="/catalog/17a8a26516404e77/kabeli-dlya-mobilnyx-ustrojstv/"]')
    }

    def hover_main_category(self):
        self.main_category.hover()
        print("Mouseover Main Category")

    def hover_drop_category_1(self):
        self.drop_category_1.hover()
        print("Mouseover Drop Category")

    def click_drop_category_2(self):
        self.drop_category_2.click_button()
        print("Click Drop Category")

    def select_category(self):
        self.hover_main_category()
        self.hover_drop_category_1()
        self.click_drop_category_2()

    # locators
    # main_category = '//a[@href="/catalog/17a890dc16404e77/smartfony-i-fototexnika/"]'
    # drop_category_1 = '//a[@href="/catalog/17a9ab6516404e77/zaryadka-i-podklyuchenie/"]'
    # drop_category_2 = '//a[@href="/catalog/17a8a26516404e77/kabeli-dlya-mobilnyx-ustrojstv/"]'
    #
    # def get_main_category(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.main_category)))
    #
    # def get_drop_category_1(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.drop_category_1)))
    #
    # def get_drop_category_2(self):
    #     return WebDriverWait(self.driver, 30).until(
    #         EC.element_to_be_clickable((By.XPATH, self.drop_category_2)))
    #
    # # actions
    # def perform_main_category(self):
    #     action = ActionChains(self.driver)
    #     action.move_to_element(self.get_main_category()).perform()
    #     print("Category Mouseover")
    #
    # def perform_drop_category_1(self):
    #     action = ActionChains(self.driver)
    #     action.move_to_element(self.get_drop_category_1()).perform()
    #     print("Category Mouseover")
    #
    # def click_drop_category_2(self):
    #     self.get_drop_category_2().click()
    #     print("Click Drop Category")
    #
    # # methods
    # def select_category(self):
    #     self.perform_main_category()
    #     self.perform_drop_category_1()
    #     self.click_drop_category_2()
    #     time.sleep(5)
