from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import Cart_page
from pages.menu_lateral import Menu_lateral
from pages.product_page import Product_page
from pages.product_selection import Product_selection
from pages.сlient_information_page import Login_page

def test_сlient_information_page(set_up, set_group):

    options = Options()          #убираем знаки в терминале
    options.add_experimental_option("excludeSwitches", ['enadle-logging'])
    driver = webdriver.Chrome(executable_path='D:\\Python\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test 5")

    ml = Menu_lateral(driver)  # Выбираем товар для теста через левое меню
    ml.checking_jordan_retro4()

    ps = Product_selection(driver) # Выбираем товар
    ps.select_product_3()

    pp = Product_page(driver) # На странице товара подтверждаем
    pp.select_product_page()

    ci = Login_page(driver)  # авторизация переходим в корзину через личный кабинет
    ci.test_authorization()

    cp = Cart_page(driver) # товар удален и корзина пуста
    cp.delet_product()
