from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    checkout_button = "//*[@id='mega-menu-primary']/li[13]"
    check_search = "//*[@id='wr_live_search-17']/form/div/input[3]"
    assert_prise = "//*[@id='post-10']/div/div/form/table/tbody/tr[1]/td[4]/span"
    quantity = "//input [@class='input-text qty text']"  #количество
    assert_result = "//*[@id='post-10']/div/div/form/table/tbody/tr[1]/td[6]/span/bdi"
    delete_product = "//td [@class='product-remove']"
    assert_delete = "//p [@class='cart-empty woocommerce-info']"  # Ваша корзина пока пуста.
    cancel = "//*[@id='post-10']/div/div/div/div/a" # кнопка отменить
    back_store = "//*[@id='post-10']/div/div/p/a" # кнопка вернутся в магазин
    update_cart = "//*[@id='post-10']/div/div/form/table/tbody/tr[2]/td/button"
    up_cart = "//*[@id='mega-menu-primary']/li[14]/a"
    general_page = "//*[@id='masthead']/div/div/a/img"
    assert_title = "//*[@id='post-10']/div/div/form/table/tbody/tr[1]/td[3]/a"

    # Getters

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_check_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_search)))

    def get_assert_prise(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_prise)))

    def get_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quantity)))

    def get_assert_result(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_result)))

    def get_delete_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_product)))

    def get_assert_delete(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_delete)))

    def get_cancel(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cancel)))

    def get_back_store(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.back_store)))

    def get_update_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.update_cart)))

    def get_up_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.up_cart)))

    def get_general_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.general_page)))

    def get_assert_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_title)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    def click_check_search(self):
        self.get_check_search().click()
        print("Тест строки поиска")

    def input_quantity(self, quantity):
        self.get_quantity().send_keys(quantity)
        print("Тест количества")

    def click_delete_product(self):
        self.get_delete_product().click()
        print("Удаление товара")

    def click_cancel(self):
        self.get_cancel().click()
        print("Отменить удаление товара")

    def click_back_store(self):
        self.get_back_store().click()
        print("Вернутся в магазин")

    def click_update_cart(self):
        self.get_update_cart().click()
        print("Нажимаем кнопку Обновить корзину")

    def click_up_cart(self):  # Выбираем элементы на странице
        self.get_up_cart().click()
        print("Нажимаем кнопку корзину")

    def click_general_page(self):  # Вход
        self.get_general_page().click()
        print("Переходим на главную страницу")

    # Methods

    def test_cart(self):
        with allure.step("Test cart"):
            Logger.add_start_step(method='test_cart')
            self.get_current_url() #выводим сайт в терминал
            self.driver.maximize_window()
            self.get_delete(self.get_quantity()) # Удаляем количество
            self.input_quantity('2')  # Вводим количество
            self.get_enter(self.get_quantity())
            self.click_general_page()
            self. click_up_cart()
            self.get_price_comparison(self.get_assert_prise(),  self.get_up_cart(), self.get_assert_result()) # цена товара, количество, общая цена
            self.click_delete_product()
            self.click_cancel()
            self.click_delete_product()
            self.click_back_store()
            Logger.add_end_step(url=self.driver.current_url, method='test_cart')

    def product_confirmation(self):
        with allure.step("Product confirmation"):
            Logger.add_start_step(method='product_confirmation')
            self.get_current_url()  # выводим сайт в терминал
            self.get_assert_url('https://nike-off.ru/cart/')
            self.get_price_comparison(self.get_assert_prise(), self.get_up_cart(), self.get_assert_result())
            self.click_delete_product()
            self.click_back_store()
            Logger.add_end_step(url=self.driver.current_url, method='product_confirmation')

    def delet_product(self):
        with allure.step("Delet product"):
            Logger.add_start_step(method='delet_product')
            self.get_current_url()  # выводим сайт в терминал
            self.get_assert_url('https://nike-off.ru/cart/')
            self.get_assert_word(self.get_assert_delete(), "Ваша корзина пока пуста.")
            Logger.add_end_step(url=self.driver.current_url, method='delet_product')

    def test_product_page(self):
        with allure.step("Test product page"):
            Logger.add_start_step(method='test_product_page')
            self.get_price_comparison(self.get_assert_prise(), self.get_up_cart(),self.get_assert_result())  # цена товара, количество, общая цена
            self.click_delete_product()
            self.click_cancel()
            self.get_assert_word(self.get_assert_title(), "nike air Jordan 4 taupe haze DB0732_200 - 42 евро / 26,5 см.")
            self.click_delete_product()
            self.click_back_store()
            Logger.add_end_step(url=self.driver.current_url, method='test_product_page')
