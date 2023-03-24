from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Login_page(Base):

    url = 'https://nike-off.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    personal_account = "//*[@id='mega-menu-item-5545']/a"
    user_name = "//input [@id='username']"
    password = "//input [@id='password']"
    login_button = "//button [@type='submit']" # Нажимаем на кнопку войти в личный кабинет
    main_word = "//*[@id='post-12']/div/div/div/p[1]/a" #локатор проверки слова Выход в личном кабинете
    g_main_page = "//*[@id='mega-menu-item-34551']/a"
    control_panel = "//*[@id='post-12']/div/div/nav/ul/li[1]/a"
    orders = "//*[@id='post-12']/div/div/nav/ul/li[2]/a"
    downloads = "//*[@id='post-12']/div/div/nav/ul/li[3]/a"
    addresses = "//*[@id='post-12']/div/div/nav/ul/li[4]/a"
    questionnaire = "//*[@id='post-12']/div/div/nav/ul/li[5]/a"
    exit = "//*[@id='post-12']/div/div/nav/ul/li[6]/a"
    recent_orders = "//*[@id='post-12']/div/div/div/p[2]/a[1]"
    nike_catalog = "//*[@id='menu-item-806']/a"
    basket = "//*[@id='menu-item-808']/a"
    blog_interesting = "//*[@id='menu-item-34989']/a"
    viewing_products = "//*[@id='post-12']/div/div/div/div[2]/a"

    # Getters

    def get_personal_account(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.personal_account)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self. main_word)))

    def get_g_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.g_main_page)))

    def get_control_panel(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.control_panel)))

    def get_orders(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.orders)))

    def get_downloads(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.downloads)))

    def get_addresses(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.addresses)))

    def get_questionnaire(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.questionnaire)))

    def get_exit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.exit)))

    def get_recent_orders(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.recent_orders)))

    def get_nike_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.nike_catalog)))

    def get_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket)))

    def get_blog_interesting(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.blog_interesting)))

    def get_viewing_products(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.viewing_products)))

    # Actions

    def input_personal_account(self): # клик вход в личный кабинет
        self.get_personal_account().click()
        print("Вход в личный кабинет")

    def input_user_name(self, user_name): # ввод информации в поле
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):  # ввод информации в поле
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):  # Нажимаем на кнопку войти в личный кабинет
        self.get_login_button().click()
        print("Click login button")

    def click_g_main_page(self):
        self.get_g_main_page().click()
        print("Переход на главную страницу")

    def click_blog_interesting(self):
        self.get_blog_interesting().click()
        print("Переход на страницу блога")

    def click_basket(self):
        self.get_basket().click()
        print("Переход в Корзину")

    def click_nike_catalog(self):
        self.get_nike_catalog().click()
        print("Переход на главную страницу")

    def click_recent_orders(self):
        self.get_recent_orders().click()
        print("Переход Недавние заказы")

    def click_exit(self):
        self.get_exit().click()
        print("Выход из личного кабинета")

    def click_questionnaire(self):
        self.get_questionnaire().click()
        print("Переход в Анкету")

    def click_addresses(self):
        self.get_addresses().click()
        print("Переход в раздел Адрес")

    def click_downloads(self):
        self.get_downloads().click()
        print("Переход в загрузки")

    def click_orders(self):
        self.get_orders().click()
        print("Переход в заказы")

    def click_viewing_products(self):
        self.get_viewing_products().click()
        print("Переход по кнопке Просмотр товаров")

    def click_control_panel(self):
        self.get_control_panel().click()
        print("Переход в Панель управления")

    # Methods

    def test_authorization(self):
        self.driver.get(self.url) #открываем сайт
        self.driver.maximize_window() # расширяем на весь экран
        self.get_current_url() #выводим сайт в терминал
        self.input_personal_account()
        self.input_user_name("Zarovnyaev92@yandex.ru") #вводим логин
        self.input_password("Z22101992!") #вводим пароль
        self.click_login_button() #нажимаем кнопку
        self.click_orders()
        self.get_assert_title('Заказы')
        self.click_downloads()
        self.get_assert_title('Загрузки')
        self.click_addresses()
        self.get_assert_title('Адрес')
        self.click_questionnaire()
        self.get_assert_title('Анкета')
        self.click_exit()
        self.get_assert_title('Мой аккаунт')
        self.click_login_button()
        self.click_basket()

    def authorization(self):
        self.driver.get(self.url)  # открываем сайт
        self.driver.maximize_window()  # расширяем на весь экран
        self.get_current_url()  # выводим сайт в терминал
        self.input_personal_account()
        self.input_user_name("Zarovnyaev92@yandex.ru")  # вводим логин
        self.input_password("Z22101992!")  # вводим пароль
        self.click_login_button()  # нажимаем кнопку
        self.click_basket() # Переходим в корзину
