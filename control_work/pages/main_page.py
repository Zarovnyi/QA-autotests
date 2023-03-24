from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from base.base_class import Base


class Main_page(Base):

    url = 'https://nike-off.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    action = ActionChains(Base)
    payment_section = "//*[@id='menu-item-6087']/a"
    discounts_section = "//*[@id='menu-item-35257']/a"
    delivery = "//*[@id='menu-item-6069']/a"
    contacts = "//*[@id='menu-item-6070']/a"
    warranty_refund = "//*[@id='menu-item-6071']/a"
    reviews = "//*[@id='menu-item-14589']/a"
    fag = "//*[@id='menu-item-14508']/a"
    entrance = "//*[@id='menu-item-6114']/a"
    filter = "//*[@id='main']/div[2]/form/select"
    filter_by_popularity = "//*[@id='main']/div[2]/form/select/option[1]" # проверка url по https://nike-off.ru/?orderby=popularity
    filter_rating = "//*[@id='main']/div[2]/form/select/option[2]"  # проверка url по https://nike-off.ru/?orderby=rating
    filter_date = "//*[@id='main']/div[2]/form/select/option[3]"    # проверка url по https://nike-off.ru/?orderby=date
    filter_price = "//*[@id='main']/div[2]/form/select/option[4]"   # проверка url по https://nike-off.ru/?orderby=price
    filter_price_desc = "//*[@id='main']/div[2]/form/select/option[5]" # проверка url по https://nike-off.ru/?orderby=price-desc
    filter_size_36 = "//*[@id='yith-woo-ajax-navigation-6']/ul/li[1]/a" # проверка url по https://nike-off.ru/nike/?filter_size=36
    filter_size_43 = "//*[@id='yith-woo-ajax-navigation-6']/ul/li[8]/a" # проверка url по https://nike-off.ru/nike/?filter_size=36,43
    filter_size_48 = "//*[@id='yith-woo-ajax-navigation-6']/ul/li[13]/a"  # проверка url по https://nike-off.ru/nike/?filter_size=36,43,48
    general_page = "//*[@id='masthead']/div/div/a/img"

    # Getters

    def get_payment_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_section)))

    def get_discounts_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discounts_section)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_contacts(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.contacts)))

    def get_warranty_refund(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.warranty_refund)))

    def get_reviews(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.reviews)))

    def get_fag(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.fag)))

    def get_entrance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.entrance)))

    def get_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter)))

    def get_filter_by_popularity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_by_popularity)))

    def get_filter_rating(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_rating)))

    def get_filter_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_date)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_filter_price_desc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_desc)))

    def get_filter_size_36(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size_36)))

    def get_filter_size_43(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size_43)))

    def get_filter_size_48(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_size_48)))

    def get_general_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.general_page)))

    # Actions

    def click_payment_section(self):  #оплат
        self.get_payment_section().click()
        print("Выбираем раздел оплата")

    def click_discounts_section(self):  #акции и скидки
        self.get_discounts_section().click()
        print("Выбираем раздел акции и скидки")

    def click_delivery(self):  #Nike Online
        self.get_delivery().click()
        print("Выбираем раздел Доставка Nike Online")

    def click_contacts(self):  #Контакты nike-off.ru интернет магазин
        self.get_contacts().click()
        print("Выбираем раздел Доставка Контакты nike-off.ru интернет магазин")

    def click_warranty_refund(self):  #Гарантия качества Nike интернет магазин
        self.get_warranty_refund().click()
        print("Выбираем раздел Гарантия качества Nike интернет магазин")

    def click_reviews(self):  #nike-off.ru отзывы
        self.get_reviews().click()
        print("Выбираем раздел nike-off.ru отзывы")

    def click_fag (self):  # Ответы на часто задаваемые вопросы
        self.get_fag().click()
        print("Выбираем раздел Ответы на часто задаваемые вопросы")

    def click_entrance(self):  # Вход
        self.get_entrance().click()
        print("Выбираем раздел вход")

    def click_filter(self):  # фильтр
        self.get_filter().click()
        print("Выбираем  фильтр")

    def click_filter_by_popularity(self):  # По рейтингу
        self.get_filter_by_popularity().click()
        print("Выбираем фильтр По рейтингу")

    def click_filter_rating(self):  # По рейтингу
        self.get_filter_rating().click()
        print("Выбираем  фильтр По рейтингу")

    def click_filter_date(self):  # По новизне
        self.get_filter_date().click()
        print("Выбираем фильтр По новизне")

    def click_filter_price(self):
        self.get_filter_price().click()
        print("Выбираем  фильтр Цены: по возрастанию")

    def click_filter_price_desc(self):  # Вход
        self.get_filter_price_desc().click()
        print("Выбираем фильтр Цены: по убыванию")

    def click_filter_size_36(self):  # По новизне
        self.get_filter_size_36().click()
        print("Выбираем фильтр размер 36")

    def click_filter_size_43(self):  # Ответы на часто задаваемые вопросы
        self.get_filter_size_43().click()
        print("Выбираем  фильтр размер 43")

    def click_filter_size_48(self):  # Вход
        self.get_filter_size_48().click()
        print("Выбираем фильтр размер 48")

    def click_general_page(self):  # Вход
        self.get_general_page().click()
        print("Переходим на главную страницу")

    # Methods

    def general_test(self):
         self.driver.get(self.url)
         self.driver.maximize_window()
         self.get_current_url() #выводим сайт в терминал
         self.get_scroll()
         self.click_payment_section()
         self.get_assert_url('https://nike-off.ru/pay/')
         self.get_assert_title('Оплата')
         self.click_general_page()
         self.click_discounts_section() # акции и скидки кроссовки nike
         self.get_assert_url('https://nike-off.ru/aktsii-i-skidki-krossovki-nike/')
         self.get_assert_title('акции и скидки кроссовки nike')
         self.click_general_page()
         self.click_delivery()  # Доставка Nike Online
         self.get_assert_url('https://nike-off.ru/dostavka-nike-online/')
         self.get_assert_title('Доставка Nike Online')
         self.click_general_page()
         self.click_contacts()  # Контакты nike-off.ru интернет магазин
         self.get_assert_url('https://nike-off.ru/kontakt/')
         self.get_assert_title ('Контакты nike-off.ru интернет магазин')
         self.click_general_page()
         self.click_warranty_refund()  # Гарантия качества Nike интернет магазин
         self.get_assert_url('https://nike-off.ru/quality/')
         self.get_assert_title('Гарантия качества Nike интернет магазин')
         self.click_general_page()
         self.click_reviews()  # nike-off.ru отзывы
         self.get_assert_url('https://nike-off.ru/nike-online-store-ru-otzyvy/')
         self.get_assert_title('nike-off.ru отзывы')
         self.click_general_page()
         self.click_fag()  # Ответы на часто задаваемые вопросы
         self.get_assert_url('https://nike-off.ru/otvety-na-chasto-zadavaemye-voprosy/')
         self.get_assert_title('Ответы на часто задаваемые вопросы')
         self.click_general_page()
         self.click_entrance()  # Мой аккаунт
         self.get_assert_url('https://nike-off.ru/my-account/')
         self.get_assert_title('Мой аккаунт')
         self.click_general_page()
         self.get_scroll()
         self.click_filter()  #
         self.click_filter_by_popularity()  #
         self.get_assert_url('https://nike-off.ru/?orderby=popularity')
         self.get_scroll()
         self.click_filter()  #
         self.click_filter_rating()  #
         self.get_assert_url('https://nike-off.ru/?orderby=rating')
         self.get_scroll()
         self.click_filter()  #
         self.click_filter_date()  #
         self.get_assert_url('https://nike-off.ru/?orderby=date')
         self.get_scroll()
         self.click_filter()  #
         self.click_filter_price()  #
         self.get_assert_url("https://nike-off.ru/?orderby=price")
         self.get_scroll()
         self.click_filter()  #
         self.click_filter_price_desc()  #
         self.get_assert_url('https://nike-off.ru/?orderby=price-desc')
         self.get_scroll()
         self.click_filter_size_36()
         self.click_filter_size_43()
         self.click_filter_size_48()


    def select_product(self):
         self.driver.get(self.url)
         self.driver.maximize_window()
         self.get_current_url() #выводим сайт в терминал
         self.get_scroll()
