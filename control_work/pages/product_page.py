from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    check_prise_product_order = "//*[@id='product-31926']/div[2]/p/span/bdi"
    check_title = "//h1 [@class='product_title entry-title']"
    check_search = "//*[@id='wr_live_search-17']/form/div/input[3]" #поиск товара
    select_size36 = "//input [@value ='36']"
    select_size40 = "//input [@value ='40']"
    select_size42 = "//input [@value ='42']"
    select_size44 = "//input [@value ='44']"
    select_size46 = "//input [@value ='46']"
    clear_size = "//a [@class='reset_variations']"
    check_quantity = "//div [@class='quantity']"
    buy_product = "//button [@type='submit']"
    transition_card = "//*[@id='main']/div[1]/div/a"
    quantity_selection = "//input [@class='input-text qty text']"
    quantity = "//*[@id='tab-title-description']/a"
    assert_quantity = "//*[@id='tab-description']/h2" # nike обзор модели кроссовок
    specifications = "//*[@id='tab-title-additional_information']/a"
    assert_specifications = "//*[@id='tab-additional_information']/h2"  # nike характеристики этой модели кроссовок
    reviews = "//*[@id='tab-title-reviews']/a"
    assert_reviews = "//*[@id='comments']/h2"  # Отзывы
    size_chart = "//*[@id='tab-title-size_guide']/a"
    assert_size_chart = "//*[@id='ct_size_guide']/h4"  # таблица размеров

    # Getters

    def get_select_size36(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size36)))

    def get_select_size40(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size40)))

    def get_select_size42(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size42)))

    def get_select_size44(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size44)))

    def get_select_size46(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size46)))

    def get_clear_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_size)))

    def get_buy_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product)))

    def get_transition_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.transition_card)))

    def get_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quantity)))

    def get_specifications(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.specifications)))

    def get_reviews(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reviews)))

    def get_size_chart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_chart)))

    def get_check_prise_product_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_prise_product_order)))

    def get_check_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_search)))

    def get_check_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_quantity)))

    def get_assert_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_quantity)))

    def get_assert_specifications(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_specifications)))

    def get_assert_reviews(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_reviews)))

    def get_assert_size_chart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.assert_size_chart)))

    def get_quantity_selection(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quantity_selection)))

    def get_check_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_title)))

    # Actions

    def click_select_size36(self):  #Выбираем элементы на странице
        self.get_select_size36().click()
        print("Выбираем размер чекбоксом 36")

    def click_select_size40(self):  #Выбираем элементы на странице
        self.get_select_size40().click()
        print("Выбираем размер чекбоксом 40")

    def click_select_size42(self):  #Выбираем элементы на странице
        self.get_select_size42().click()
        print("Выбираем размер чекбоксом 42")

    def click_select_size44(self):  #Выбираем элементы на странице
        self.get_select_size44().click()
        print("Выбираем размер чекбоксом 44")

    def click_select_size46(self):  #Выбираем элементы на странице
        self.get_select_size46().click()
        print("Выбираем размер чекбоксом 46")

    def click_clear_size(self):  #Выбираем элементы на странице
        self.get_clear_size().click()
        print("Удаляем чекбокс")

    def click_buy_product(self):  #Выбираем элементы на странице
        self.get_buy_product().click()
        print("Нашимаем на конпку купить")

    def click_transition_card(self):  #Выбираем элементы на странице
        self.get_transition_card().click()
        print("Переходим в корзину")

    def click_quantity(self):  #Выбираем элементы на странице
        self.get_quantity().click()
        print("Выбираем раздел описание товара")

    def click_specifications(self):  # Выбираем элементы на странице
        self.get_specifications().click()
        print("Выбираем раздел характеристики")

    def click_reviews(self):  # Выбираем элементы на странице
        self.get_reviews().click()
        print("Выбираем раздел отзывы")

    def click_size_chart(self):  # Выбираем элементы на странице
        self.get_size_chart().click()
        print("Выбираем раздел таблица размеров")

    def input_quantity_selection(self, quantity_selection):  # Выбираем элементы на странице
        self.get_quantity_selection().send_keys(quantity_selection)
        print("Выбираем количество товара")

    def input_check_search(self, check_search):  # Выбираем элементы на странице
        self.get_check_search().send_keys(check_search)
        print("Проверяем поле поиск")

    # Methods

    def test_product_page(self):
        self.get_current_url() #выводим сайт в терминал
        self.input_check_search("off white x nike air max 270 white")
        self.input_check_search(Keys.RETURN)
        self.get_assert_word(self.get_check_title(), 'off white x nike air max 270 white')
        self.input_check_search("nike air Jordan 4 taupe haze DB0732_200") # Ввод данных в поиск
        self.input_check_search(Keys.RETURN) # Нажимаем интер
        self.click_clear_size()
        self.click_select_size42()
        self.click_select_size46()
        self.click_select_size44()
        self.click_select_size42()
        self.click_size_chart()
        self.get_delete(self.get_quantity_selection())
        self.input_quantity_selection('2')
        self.input_quantity_selection(Keys.RETURN)  # Нажимаем интер
        self.click_reviews()
        self.get_assert_word(self.get_assert_reviews(), 'Отзывы')
        self.click_specifications()
        self.get_assert_word(self.get_assert_specifications(), 'nike характеристики этой модели кроссовок')
        self.click_quantity()
        self.get_assert_word(self.get_assert_quantity(), 'nike обзор модели кроссовок')
        self.click_buy_product()
        self.click_transition_card()

    def select_product_page(self):
        self.get_current_url() #выводим сайт в терминал
        self.click_buy_product()
        self.click_transition_card()
        self.get_assert_url('https://nike-off.ru/cart/')
