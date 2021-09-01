from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class AssetsLocators:
    LOCATOR_BANK_NAME1_INPUT = (By.ID, "0BANK_NAME")
    LOCATOR_ACCOUNT_TYPE1_LISTBOX = (By.CSS_SELECTOR, "[formcontrolname='ACCOUNT_TYPE'] .ng-select-container")
    LOCATOR_ASSERT_ACCOUNT_TYPE1_LISTBOX = (By.CSS_SELECTOR, ".ng-option-label")
    LOCATOR_ADD_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='about']/div/div/div/app-assets/div/form/div[4]")
    LOCATOR_BANK_NAME2_INPUT = (By.ID, "1BANK_NAME")
    LOCATOR_ACCOUNT_TYPE2_LISTBOX = (By.XPATH, "//*[@id='1ACCOUNT_TYPE']/div")
    LOCATOR_ASSERT_ACCOUNT_TYPE2_LISTBOX = (By.CSS_SELECTOR, ".ng-option-label")
    LOCATOR_DELETE_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='1ACCOUNT_TYPE']/div")
    LOCATOR_PROPERTY_ADDRESS_INPUT = (By.ID, "0PROPERTY_ADDRESS")
    LOCATOR_PROPERTY_TYPE_LISTBOX = (By.CSS_SELECTOR, "[formcontrolname='PROPERTY_TYPE'] .ng-select-container")
    LOCATOR_ASSERT_PROPERTY_TYPE_LISTBOX = (By.CSS_SELECTOR, ".ng-option-label")
    LOCATOR_PROPERTY_DESIGNATION_LISTBOX = (By.CSS_SELECTOR, "[formcontrolname='PROPERTY_DESIGNATION'] .ng-select-container")
    LOCATOR_ASSERT_PROPERTY_DESIGNATION_LISTBOX = (By.CSS_SELECTOR, ".ng-option-label")
    LOCATOR_PROPERTY_MARKET_VALUE_INPUT = (By.ID, "0PRESENT_MARKET_VALUE")
    LOCATOR_AMOUNT_OF_MORTGAGES_INPUT = (By.ID, "0AMOUNT_OF_MORTGAGES")



    LOCATOR_BANK_NAME1_INPUT = (By.ID, "0BANK_NAME")
    LOCATOR_EMPLOYMENT_ADDRESS_INPUT = (By.ID, "NAME_ADDRESS_OF_EMPLOYER")
    LOCATOR_CHECKBOX_TEXT = (By.XPATH, "//*[@id='about']/div/div/div/app-income/div/form/div[3]/div[2]/div/div[2]/label[2]")
    LOCATOR_CHECKBOX_BUTTON = (By.XPATH, "//*[@id='about']/div/div/div/app-income/div/form/div[3]/div[2]/div/div[2]/label[1]")
    LOCATOR_TYPE_BUSINESS_INPUT = (By.ID, "POSITION_TITLE_TYPE_OF_BUSINESS")
    LOCATOR_BUSINESS_PHONE_INPUT = (By.ID, "BUSINESS_PHONE")
    LOCATOR_YRS_IN_JOB_INPUT = (By.ID, "YRS_ON_THIS_JOB")
    LOCATOR_YRS_IN_PROFESSION_INPUT = (By.ID, "YRS_IN_THIS_PROFESSION")
    LOCATOR_NEXT_BUTTON = (By.CSS_SELECTOR, ".row div.blue-btn")

class AssetsHelper(BasePage):

    def checking_radio_button(self, elem, button):
        if(elem.text == "YES"):
            print("Кнопка в положении 'YES'")
        else:
            name_checkbox = self.find_clickable_element(button)
            name_checkbox.click()

    def enter_income_and_employment(self, annual_income_keys, employment_address_keys, type_business_keys, business_phone_keys, years_in_job_keys, years_in_prof_keys):
        annual_income_input = self.find_element(EmploymentLocators.LOCATOR_ANNUAL_INCOME_INPUT)
        annual_income_input.clear()
        annual_income_input.send_keys(annual_income_keys)

        employment_address_input = self.find_element(EmploymentLocators.LOCATOR_EMPLOYMENT_ADDRESS_INPUT)
        employment_address_input.clear()
        employment_address_input.send_keys(employment_address_keys)

        type_business_input = self.find_element(EmploymentLocators.LOCATOR_TYPE_BUSINESS_INPUT)
        type_business_input.clear()
        type_business_input.send_keys(type_business_keys)

        business_phone_input = self.find_element(EmploymentLocators. LOCATOR_BUSINESS_PHONE_INPUT)
        business_phone_input.clear()
        business_phone_input.send_keys(business_phone_keys)

        years_in_job_input = self.find_element(EmploymentLocators.LOCATOR_YRS_IN_JOB_INPUT)
        years_in_job_input.clear()
        years_in_job_input.send_keys(years_in_job_keys)

        years_in_prof_input = self.find_element(EmploymentLocators.LOCATOR_YRS_IN_PROFESSION_INPUT)
        years_in_prof_input.clear()
        years_in_prof_input.send_keys(years_in_prof_keys)