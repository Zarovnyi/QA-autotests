from selenium import webdriver
from selenium.webdriver.chrome.options import Options  #убираем не понятные знаки в терминале
from pages.cart_page import Cart_page
from pages.product_page import Product_page
from pages.product_selection import  Product_selection
from pages.menu_lateral import Menu_lateral
import allure

@allure.description("Test cart")
def test_cart():

    options = Options()          #убираем  знаки в терминале
    options.add_experimental_option("excludeSwitches", ['enadle-logging'])
    driver = webdriver.Chrome(executable_path ='D:\\Python\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test 2")

    ml = Menu_lateral(driver) # Выбираем товар для теста через левое меню
    ml.checking_menu_blazer()

    ps = Product_selection(driver) # Выбираем третий товар из раздела
    ps.select_product_3()

    pp = Product_page(driver) # На странице товара подтверждаем переходим в корзину
    pp.select_product_page()

    cp = Cart_page(driver)
    cp.test_cart()
