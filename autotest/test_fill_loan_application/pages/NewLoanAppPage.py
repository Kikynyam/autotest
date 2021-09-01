from .BaseApp import BasePage
from selenium.webdriver.common.by import By
import time

from .PropertyDetailsPage import PropertyDetailsHelper


class NewLoanAppLocators:
    LOCATOR_SEE_DETAILS_BUTTON = (By.XPATH, "//*[@id='pills-home']/div/div/div/div[4]")
    LOCATOR_LOAN_APPLICATION_LISTBOX = (By.CSS_SELECTOR, "#headingOne div")
    LOCATOR_PROPERTY_DETAILS_BUTTON = (By.CSS_SELECTOR, "a[href*='property']")


class NewLoanAppHelper(BasePage):
    def creating(self):
        details_button = self.find_clickable_element(NewLoanAppLocators.LOCATOR_SEE_DETAILS_BUTTON)
        details_button.click()

    #     time.sleep(2)
    #
    #     loan_application_button = self.find_clickable_element(NewLoanAppLocators.LOCATOR_LOAN_APPLICATION_LISTBOX)
    #     loan_application_button.click()
    #
    # def switching_to_property_page(self):
    #
    #     property_details_button = self.find_clickable_element(NewLoanAppLocators.LOCATOR_PROPERTY_DETAILS_BUTTON)
    #     property_details_button.click()
    #     return PropertyDetailsHelper(self.browser)





