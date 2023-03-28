from pages.menu_lateral import Menu_lateral
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

@allure.description("Test menu lateral")
def test_menu_lateral():

    options = Options()          #убираем знаки в терминале
    options.add_experimental_option("excludeSwitches", ['enadle-logging'])
    driver = webdriver.Chrome(executable_path ='D:\\Python\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test 6")

    ml = Menu_lateral(driver)
    ml.test_lateral()
