from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.menu_up import Menu_up


def menu_up():

    options = Options()          #убираем  знаки в терминале
    options.add_experimental_option("excludeSwitches", ['enadle-logging'])
    driver = webdriver.Chrome(executable_path ='D:\\Python\\resource\\chromedriver.exe', chrome_options = options)

    print("Start Test 7")

    mu = Menu_up(driver)
    mu.test_menu_up()
