import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import  Keys



class Base():

    def __init__(self, driver): #для хранения методов(делать скрин и т.д)
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def get_assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")  # прописываем дату и время скриншота
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot('D:\\Python\\main_project\\screen\\' + name_screenshot)  # делаем скриншот

    """Method assert url"""

    def get_assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method price comparison"""

    def get_price_comparison(self, price, quantity, final_price): # цена товара, количество, общая цена
        value_price = price.text
        value_final_price = final_price.text
        value_quantity = quantity.text
        total_price = int(value_price[:-2])
        total_final_price = int(value_final_price[:-2])
        total_quantity = int(value_quantity[:2])
        print(total_quantity)
        result = total_price * total_quantity
        assert str(result) == str(total_final_price)
        print("Good final_price " + value_final_price)

    """Method scroll page"""

    def get_scroll(self):
        self.driver.execute_script('window.scrollTo(0, 700)')
        print("scroll")

    """Method assert title"""

    def get_assert_title(self, result):
        title = "//h1 [@class='entry-title']"
        word = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, title)))
        value_word = word.text
        assert value_word == result
        print("Проверка названия заголовка '" + value_word + "' успешна")

    """Method assert title chapter"""

    def get_assert_title_chapter(self, result):
        title = "//h3 [@class='woo-title entry-title']"
        word = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, title)))
        value_word = word.text
        assert value_word == result
        print("Проверка названия раздела '" + value_word + "' успешна")

    """Method delete"""

    def get_delete(self, meaning):
        meaning.click()
        meaning.send_keys(Keys.CONTROL + "a")  # удаляем из поля
        meaning.send_keys(Keys.BACKSPACE)
        print("Удаляем из поля данные")

    """Method enter"""

    def get_enter(self, enter):
        enter.send_keys(Keys.RETURN)
        print("Нажимаем интере")

    """Method refresh"""

    def get_refresh(self):
        self.driver.refresh() #обновляем страницу
        print("Обновляем страницу")
