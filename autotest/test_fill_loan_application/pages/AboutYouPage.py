from .BaseApp import BasePage
from selenium.webdriver.common.by import By
import time

class AboutDetailsLocators:
    LOCATOR_YEARS_SCHOOL_INPUT = (By.ID, "YRS_SCHOOL")
    LOCATOR_MARITAL_STATUS_LISTBOX = (By.CSS_SELECTOR, "[formcontrolname='MARITAL_STATUS'] .ng-select-container")
    LOCATOR_ASSERT_MAR_STATUS_LISTBOX = (By.CSS_SELECTOR, ".ng-option-label")
    LOCATOR_CHECKBOX1_TEXT = (By.XPATH, "//*[@id='about']/div/div/div/app-about/div/form/div[3]/div/div[1]/label[2]")
    LOCATOR_CHECKBOX1_BUTTON = (By.XPATH, "//*[@id='about']/div/div/div/app-about/div/form/div[3]/div/div[1]/label[1]")
    LOCATOR_ANY_DEPENDANTS_INPUT = (By.ID, "ANY_DEPENDENTS")
    LOCATOR_PRESENT_ADDRESS_INPUT = (By.ID, "PRESENT_ADDRESS")
    LOCATOR_ABOUT_YOU_BUTTON = (By.CSS_SELECTOR, "a[href*='about']")
    LOCATOR_CLICK1_LABEL = (By.XPATH, "//*[@id='about']/div/div/div/app-about/div/form/div[5]/div/div/div/div")
    LOCATOR_BLANK_SPACE = (By.XPATH, "//html")
    LOCATOR_OWN_BUTTON = (By.CSS_SELECTOR, "[value='Own'] button")
    LOCATOR_NO_YEARS_INPUT = (By.ID, "PA_YEARS_OF_RESIDENCY")
    LOCATOR_CHECKBOX2_TEXT = (By.XPATH, "//*[@id='about']/div/div/div/app-about/div/form/div[7]/div/div[2]/label[2]")
    LOCATOR_CHECKBOX2_BUTTON = (By.XPATH, "//*[@id='about']/div/div/div/app-about/div/form/div[7]/div/div[2]/label[1]")
    LOCATOR_MAILING_ADDRESS_INPUT = (By.ID, "MAILING_ADDRESS")
    LOCATOR_FORMER_ADDRESS_INPUT = (By.CSS_SELECTOR, "input[formcontrolname='FORMER_ADDRESS']")
    LOCATOR_OWN2_BUTTON = (By.CSS_SELECTOR, "[formcontrolname='FA_OCCUPANCY_BASIS'] mat-button-toggle:nth-child(2) button")
    LOCATOR_NO_YEARS2_INPUT = (By.XPATH, "//*[@id='0FA_YEARS_OF_RESIDENCY']")
    LOCATOR_ADD_NEW_ADDRESS_BUTTON = (By.XPATH, "//*[@id='about']/div/div/div/app-about/div/form/div[8]/div[4]")
    LOCATOR_FORMER_ADDRESS1_INPUT = (By.ID, "1FORMER_ADDRESS")
    LOCATOR_NO_YEARS3_INPUT = (By.ID, "1FA_YEARS_OF_RESIDENCY")
    # LOCATOR_NEXT_BUTTON = (By.CSS_SELECTOR, ".row div.blue-btn")
    LOCATOR_TRACK_RECORD_BUTTON = (By.CSS_SELECTOR, "a[href*='trackrecord']")

class AboutYouHelper(BasePage):
    def asserting(self, selector, text):
        elements = self.find_elements(selector)
        for elem in elements:
            texting = elem.text
            if texting == text:
                return elem.click()
            else:
                print('not correct element')

    def checking_radio_button(self, elem, button):
        if(elem.text == "YES"):
            print("Кнопка в положении 'YES'")
        else:
            name_checkbox = self.find_clickable_element(button)
            name_checkbox.click()

    def enter_about_you(self, yrs_school_keys, mar_status_item, dependants_keys):
        years_of_school_input = self.find_element(AboutDetailsLocators.LOCATOR_YEARS_SCHOOL_INPUT)
        years_of_school_input.clear()
        years_of_school_input.send_keys(yrs_school_keys)

        marital_status_listbox = self.find_clickable_element(AboutDetailsLocators.LOCATOR_MARITAL_STATUS_LISTBOX)
        marital_status_listbox.click()

        self.asserting(AboutDetailsLocators.LOCATOR_ASSERT_MAR_STATUS_LISTBOX, mar_status_item)
        checkbox1_text = self.find_element(AboutDetailsLocators.LOCATOR_CHECKBOX1_TEXT)
        self.checking_radio_button(checkbox1_text, AboutDetailsLocators.LOCATOR_CHECKBOX1_BUTTON)
        any_dependants_input = self.find_element(AboutDetailsLocators.LOCATOR_ANY_DEPENDANTS_INPUT)
        any_dependants_input.clear()
        any_dependants_input.send_keys(dependants_keys)

    def enter_present_address(self, pres_address_keys, no_years_keys):
        present_address_input = self.find_element(AboutDetailsLocators.LOCATOR_PRESENT_ADDRESS_INPUT)
        present_address_input.clear()
        present_address_input.send_keys(pres_address_keys)
        self.find_element(AboutDetailsLocators.LOCATOR_BLANK_SPACE).click()
        # click1_label = self.find_clickable_element(AboutDetailsLocators.LOCATOR_CLICK1_LABEL)
        # click1_label.click()
        own_button = self.find_clickable_element(AboutDetailsLocators.LOCATOR_OWN_BUTTON)
        own_button.click()
        no_years_input = self.find_element(AboutDetailsLocators.LOCATOR_NO_YEARS_INPUT)
        no_years_input.clear()
        no_years_input.send_keys(no_years_keys)

    def refreshing(self):
        self.browser.refresh()

    def turn_checkbox2_button(self):
        checkbox2_text = self.find_element(AboutDetailsLocators.LOCATOR_CHECKBOX2_TEXT)
        self.checking_radio_button(checkbox2_text, AboutDetailsLocators.LOCATOR_CHECKBOX2_BUTTON)

    def enter_diff_mail_address(self, mailing_address_keys):
        mailing_address_input = self.find_element(AboutDetailsLocators.LOCATOR_MAILING_ADDRESS_INPUT)
        mailing_address_input.clear()
        mailing_address_input.send_keys(mailing_address_keys)

    def enter_former_address(self, former_address_keys, no_years_keys):
        former_address_input = self.find_element(AboutDetailsLocators.LOCATOR_FORMER_ADDRESS_INPUT)
        former_address_input.clear()
        former_address_input.send_keys(former_address_keys)
        own2_button = self.find_clickable_element(AboutDetailsLocators.LOCATOR_OWN2_BUTTON)
        own2_button.click()
        no_years_input = self.find_element(AboutDetailsLocators.LOCATOR_NO_YEARS2_INPUT)
        no_years_input.clear()
        no_years_input.send_keys(no_years_keys)

    def add_new_former_address(self):
        add_address_button = self.find_clickable_element(AboutDetailsLocators.LOCATOR_ADD_NEW_ADDRESS_BUTTON)
        add_address_button.click()

    def enter_former_address2(self, former_address1_keys, no_years_keys):
        former_address_input = self.find_element(AboutDetailsLocators.LOCATOR_FORMER_ADDRESS1_INPUT)
        former_address_input.clear()
        former_address_input.send_keys(former_address1_keys)
        no_years_input = self.find_element(AboutDetailsLocators.LOCATOR_NO_YEARS3_INPUT)
        no_years_input.clear()
        no_years_input.send_keys(no_years_keys)

    def switch_to_track_record(self):
        track_record_button = self.find_clickable_element(AboutDetailsLocators.LOCATOR_TRACK_RECORD_BUTTON)
        track_record_button.click()
        # income_and_employment_button = self.find_clickable_element(AboutDetailsLocators.LOCATOR_INCOME_EMPLOYMENT_BUTTON)
        # income_and_employment_button.click()








