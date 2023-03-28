from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import Cart_page
from pages.product_page import Product_page
from pages.product_selection import Product_selection
from pages.main_page import Main_page
from pages.сlient_information_page import Login_page
import allure

@allure.description("Test buy product")
def test_buy_product(set_up, set_group):

    options = Options()          #убираем знаки в терминале
    options.add_experimental_option("excludeSwitches", ['enadle-logging'])

    driver = webdriver.Chrome(executable_path='D:\\Python\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test 1")

    mp = Main_page(driver) # Выбираем товара с главной страницы
    mp.select_product()

    ps = Product_selection(driver) # Выбираем первый товар
    ps.select_product1()

    pp = Product_page(driver) # На странице товара подтверждаем
    pp.select_product_page()

    cp = Cart_page(driver)     # В корзине проверяем цену и удаляем товар
    cp.product_confirmation()

    ci = Login_page(driver)  # авторизация переходим в корзину через личный кабинет
    ci.authorization()

    cp = Cart_page(driver) # товар удален и корзина пуста
    cp.delet_product()
