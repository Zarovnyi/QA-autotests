from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class Menu_up(Base):

    url = 'https://nike-off.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    # Раздел jordan выподающее меню
    select_jordan_menu = "//*[@id='mega-menu-item-6098']/a"
    # Раздел jordan retro
    jordan_menu_retro4 = "// *[ @ id = 'mega-menu-item-11602'] / a"
    # Раздел sb dunk
    menu_sb_dunk = "//*[@id='mega-menu-item-26679']/a"
    # Раздел air max
    menu_air_max = "//*[@id='mega-menu-item-3843']/a"
    # Раздел blazer
    menu_blazer = "//*[@id='mega-menu-item-16226']/a"

    # Getters

    # Раздел jordan выподающее меню
    def get_select_jordan_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_jordan_menu)))

    # Раздел jordan retro 4
    def get_jordan_menu_retro4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jordan_menu_retro4)))

    # Раздел sb dunk
    def get_menu_sb_dunk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_sb_dunk)))

    # Раздел air max
    def get_menu_air_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_air_max)))

        # Раздел blazer
    def get_menu_blazer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_blazer)))

    # Actions

    # Раздел jordan выподающее меню
    def click_select_jordan_menu(self):  # Выбираем элементы на странице
        self.get_select_jordan_menu().click()
        print("Открываем в разделе jordan выпадающее меню")

    # Раздел jordan retro 4
    def click_jordan_menu_retro4(self):  #Выбираем элементы на странице
        self.get_jordan_menu_retro4().click()
        print("Переходим в разделы jordan retro4")

    # Раздел sb dunk
    def click_menu_sb_dunk(self):  #Выбираем элементы на странице
        self.get_menu_sb_dunk().click()
        print("Переходим в разделы  sb dunk")

    # Раздел air max
    def click_menu_air_max(self):  #Выбираем элементы на странице
        self.get_menu_air_max().click()
        print("Переходим в разделы  air max")

    # Раздел blazer
    def click_menu_blazer(self):  # Выбираем элементы на странице
        self.get_menu_blazer().click()
        print("Переходим в разделы  blazer")

    # Methods

    def test_menu_up(self):
        self.driver.get(self.url)
        self.get_current_url() #выводим сайт в терминал
        self.driver.maximize_window()
        self.click_select_jordan_menu()
        self.click_jordan_menu_retro4()
        self.get_assert_url('https://nike-off.ru/product-category/jordan/retro-4/')
        self.get_current_url()
        self.get_assert_title_chapter('Nike Air Jordan 4 Retro')
        self.click_menu_sb_dunk()
        self.get_assert_title_chapter('sb dunk')
        self.click_menu_air_max()
        self.get_assert_title_chapter('Nike Air Max')
        self.click_menu_blazer()
        self.get_assert_title_chapter('Nike Blazer')

    def checking_jordan_retro4(self):
        self.driver.get(self.url)
        self.get_current_url()  # выводим сайт в терминал
        self.driver.maximize_window()
        self.click_select_jordan_menu()
        self.click_jordan_menu_retro4()
        self.get_assert_title_chapter('Nike Air Jordan 4 Retro')

    def checking_sb_dunk(self):
        self.driver.get(self.url)
        self.get_current_url()  # выводим сайт в терминал
        self.driver.maximize_window()
        self.click_menu_sb_dunk()
        self.get_assert_title_chapter('sb dunk')

    def checking_air_max(self):
        self.driver.get(self.url)
        self.get_current_url()  # выводим сайт в терминал
        self.driver.maximize_window()
        self.click_menu_air_max()
        self.get_assert_title_chapter('Nike Air Max')

    def checking_menu_blazer(self):
        self.driver.get(self.url)
        self.get_current_url()  # выводим сайт в терминал
        self.driver.maximize_window()
        self.click_menu_blazer()
        self.get_assert_title_chapter('Nike Blazer')
