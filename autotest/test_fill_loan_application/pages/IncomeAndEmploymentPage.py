from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class EmploymentLocators:
    LOCATOR_ANNUAL_INCOME_INPUT = (By.ID, "ANNUAL_INCOME")
    LOCATOR_EMPLOYMENT_ADDRESS_INPUT = (By.ID, "NAME_ADDRESS_OF_EMPLOYER")
    LOCATOR_CHECKBOX_TEXT = (By.XPATH, "//*[@id='about']/div/div/div/app-income/div/form/div[3]/div[2]/div/div[2]/label[2]")
    LOCATOR_CHECKBOX_BUTTON = (By.XPATH, "//*[@id='about']/div/div/div/app-income/div/form/div[3]/div[2]/div/div[2]/label[1]")
    LOCATOR_TYPE_BUSINESS_INPUT = (By.ID, "POSITION_TITLE_TYPE_OF_BUSINESS")
    LOCATOR_BUSINESS_PHONE_INPUT = (By.ID, "BUSINESS_PHONE")
    LOCATOR_YRS_IN_JOB_INPUT = (By.ID, "YRS_ON_THIS_JOB")
    LOCATOR_YRS_IN_PROFESSION_INPUT = (By.ID, "YRS_IN_THIS_PROFESSION")
    LOCATOR_NEXT_BUTTON = (By.CSS_SELECTOR, ".row div.blue-btn")

class EmploymentHelper(BasePage):

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

    def turning_self_employed_checkbox(self):
        checkbox_text = self.find_element(EmploymentLocators.LOCATOR_CHECKBOX_TEXT)
        self.checking_radio_button(checkbox_text, EmploymentLocators.LOCATOR_CHECKBOX_BUTTON)

    def click_next_button_to_your_assets(self):
        next_button = self.find_clickable_element(EmploymentLocators.LOCATOR_NEXT_BUTTON)
        next_button.click()









