from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class BasePage:

    def __init__(self, browser):
        self. browser = browser
        self.base_url = "https://dev.borrowlabs.com/login"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.browser.get(self.base_url)

    def findElement(self, locator):
        return self.browser.findElement(locator)


    def writing_in_test_log(self, locator, keys):
        f = open("test.log", "a")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"{dt_string} объект - {locator} выбранное значение - {keys}\n")