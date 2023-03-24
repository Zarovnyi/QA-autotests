from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import Cart_page
from pages.menu_up import Menu_up
from pages.product_page import Product_page
from pages.product_selection import Product_selection

def test_product_page():

    options = Options()          #убираем знаки в терминале
    options.add_experimental_option("excludeSwitches", ['enadle-logging'])
    driver = webdriver.Chrome(executable_path='D:\\Python\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test 4")

    mu = Menu_up(driver) # Выбираем товара верхнее меню
    mu.checking_menu_blazer()

    ps = Product_selection(driver) # Выбираем первый товар
    ps.select_product1()

    pp = Product_page(driver) # Тест страницы товара
    pp.test_product_page()

    cp = Cart_page(driver)     # В корзине проверяем цену и название товара и удаляем товар
    cp.test_product_page()
