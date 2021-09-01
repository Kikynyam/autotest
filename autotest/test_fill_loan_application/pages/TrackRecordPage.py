from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class TrackRecordLocators:
    LOCATOR_PROPERTY_ADDRESS1_INPUT = (By.ID, "0PROPERTY_ADDRESS")
    LOCATOR_PURCHASE_DATE1_INPUT = (By.ID, "0PURCHASE_DATE")
    LOCATOR_PURCHASE_PRICE1_INPUT = (By.ID, "0PURCHASE_PRICE")
    LOCATOR_REHAB_BUDGET1_INPUT = (By.ID, "0REHAB_BUDGET_USED")
    LOCATOR_SALE_DATE1_INPUT = (By.ID, "0SALE_DATE")
    LOCATOR_SOLD_PRICE1_INPUT = (By.ID, "0SALE_PRICE")

    LOCATOR_PROPERTY_ADDRESS2_INPUT = (By.ID, "1PROPERTY_ADDRESS")
    LOCATOR_PURCHASE_DATE2_INPUT = (By.ID, "1PURCHASE_DATE")
    LOCATOR_PURCHASE_PRICE2_INPUT = (By.ID, "1PURCHASE_PRICE")
    LOCATOR_REHAB_BUDGET2_INPUT = (By.ID, "1REHAB_BUDGET_USED")
    LOCATOR_SALE_DATE2_INPUT = (By.ID, "1SALE_DATE")
    LOCATOR_SOLD_PRICE2_INPUT = (By.ID, "1SALE_PRICE")
    LOCATOR_ADD_NEW_DEAL_BUTTON = (By.XPATH, "//*[@id='about']/div/div/div/app-track/div/form/div[5]")


class TrackRecordHelper(BasePage):
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


    def enter_property1(self, property_address_keys, purchase_date_keys, purchase_price_keys,rehab_budget_keys,sale_date_keys,sold_price_keys):

        property_address_input = self.find_element(TrackRecordLocators.LOCATOR_PROPERTY_ADDRESS1_INPUT)
        property_address_input.clear()
        property_address_input.send_keys(property_address_keys)

        purchase_date_input = self.find_element(TrackRecordLocators.LOCATOR_PURCHASE_DATE1_INPUT)
        purchase_date_input.clear()
        purchase_date_input.send_keys(purchase_date_keys)

        purchase_price_input = self.find_element(TrackRecordLocators.LOCATOR_PURCHASE_PRICE1_INPUT)
        purchase_price_input.clear()
        purchase_price_input.send_keys(purchase_price_keys)

        rehab_budget_input = self.find_element(TrackRecordLocators.LOCATOR_REHAB_BUDGET1_INPUT)
        rehab_budget_input.clear()
        rehab_budget_input.send_keys(rehab_budget_keys)

        sale_date_input = self.find_element(TrackRecordLocators.LOCATOR_SALE_DATE1_INPUT)
        sale_date_input.clear()
        sale_date_input.send_keys(sale_date_keys)

        sold_price_input = self.find_element(TrackRecordLocators.LOCATOR_SOLD_PRICE1_INPUT)
        sold_price_input.clear()
        sold_price_input.send_keys(sold_price_keys)

    def enter_property2(self, property_address_keys, purchase_date_keys, purchase_price_keys,rehab_budget_keys,sale_date_keys,sold_price_keys):

        property_address_input = self.find_element(TrackRecordLocators.LOCATOR_PROPERTY_ADDRESS2_INPUT)
        property_address_input.clear()
        property_address_input.send_keys(property_address_keys)

        purchase_date_input = self.find_element(TrackRecordLocators.LOCATOR_PURCHASE_DATE2_INPUT)
        purchase_date_input.clear()
        purchase_date_input.send_keys(purchase_date_keys)

        purchase_price_input = self.find_element(TrackRecordLocators.LOCATOR_PURCHASE_PRICE2_INPUT)
        purchase_price_input.clear()
        purchase_price_input.send_keys(purchase_price_keys)

        rehab_budget_input = self.find_element(TrackRecordLocators.LOCATOR_REHAB_BUDGET2_INPUT)
        rehab_budget_input.clear()
        rehab_budget_input.send_keys(rehab_budget_keys)

        sale_date_input = self.find_element(TrackRecordLocators.LOCATOR_SALE_DATE2_INPUT)
        sale_date_input.clear()
        sale_date_input.send_keys(sale_date_keys)

        sold_price_input = self.find_element(TrackRecordLocators.LOCATOR_SOLD_PRICE2_INPUT)
        sold_price_input.clear()
        sold_price_input.send_keys(sold_price_keys)
