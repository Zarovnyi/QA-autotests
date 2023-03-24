from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import Cart_page
from pages.product_page import Product_page
from pages.product_selection import Product_selection
from pages.main_page import Main_page

def test_main_page(set_up, set_group):

    options = Options()          #убираем знаки в терминале
    options.add_experimental_option("excludeSwitches", ['enadle-logging'])
    driver = webdriver.Chrome(executable_path='D:\\Python\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test 3")

    mp = Main_page(driver) # Выбираем товара с главной страницы
    mp.general_test()

    ps = Product_selection(driver) # Выбираем первый товар
    ps.select_product1()

    pp = Product_page(driver) # На странице товара подтверждаем
    pp.select_product_page()

    cp = Cart_page(driver)     # В корзине проверяем цену и удаляем товар
    cp.product_confirmation()
