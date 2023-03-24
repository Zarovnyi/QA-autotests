from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Product_selection(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    prise_product_1 = "//p [@class='price']"
    title_product_1 = "//*[@id='main']/div[3]/ul/li[1]/a[1]/h2"
    select_product_1 = "//a [@data-quantity='1']"
    prise_product_3 = "//*[@id='main']/div[3]/ul/li[3]/a[1]/span/span"
    title_product_3 = "//*[@id='main']/div[3]/ul/li[3]/a[1]/h2"
    select_product3 = "//*[@id='main']/div[3]/ul/li[3]/a[2]"
    check_title_product = "//*[@id='product-30446']/div[2]/h1"
    check_prise_product ="//*[@id='product-36764']/div[2]/p/span/bdi"

    # Getters

    def get_prise_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.prise_product_3)))

    def get_title_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_product_3)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product3)))

    def get_prise_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.prise_product_1)))

    def get_title_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_product_1)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_check_title_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_title_product)))

    def get_check_prise_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_prise_product)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Выбираем первый товар")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Выбираем третий товар")

    # Methods

    def select_product1(self):
        self.get_current_url() #выводим сайт в терминал
        self.click_select_product_1()

    def select_product_3(self):
        self.get_current_url() #выводим сайт в терминал
        self.click_select_product_3()
