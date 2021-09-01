from .BaseApp import BasePage
from selenium.webdriver.common.by import By

from .NewLoanAppPage import NewLoanAppHelper
from .PropertyDetailsPage import PropertyDetailsHelper
import time


class PreAppLoginLocators:
    LOCATOR_EMAIL_INPUT = (By.ID, "email")
    LOCATOR_PASSWORD_INPUT = (By.ID, "password")
    LOCATOR_SUBMIT_BUTTON = (By.CLASS_NAME, "blue-btn")
    LOCATOR_MODAL_LATER_BUTTON = (By.CSS_SELECTOR, "div.modal__btn-cancel")

class PreAppLoginHelper(BasePage):
    def logging(self, email_keys, password_keys):
        email_input = self.find_element(PreAppLoginLocators.LOCATOR_EMAIL_INPUT)
        email_input.send_keys(email_keys)

        password_input = self.find_element(PreAppLoginLocators.LOCATOR_PASSWORD_INPUT)
        password_input.send_keys(password_keys)



    def submitting(self):
        submit_button = self.find_clickable_element(PreAppLoginLocators.LOCATOR_SUBMIT_BUTTON)
        submit_button.click()
        return NewLoanAppHelper(self.browser)






