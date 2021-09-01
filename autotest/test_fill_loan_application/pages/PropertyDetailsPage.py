from .BaseApp import BasePage
from selenium.webdriver.common.by import By
from .AboutYouPage import AboutYouHelper

class PropertyDetailsLocators:
    LOCATOR_MODAL_LATER_BUTTON = (By.CSS_SELECTOR, "div.modal__btn-cancel")
    LOCATOR_LINE1_INPUT = (By.ID, "ADDRESS_LINE_1")
    LOCATOR_CITY_INPUT = (By.ID, "ADDRESS_CITY")
    LOCATOR_POSTAL_INPUT = (By.ID, "ADDRESS_ZIP_CODE")
    LOCATOR_YEAR_INPUT = (By.ID, "YEAR_BUILT")
    LOCATOR_CURRENT_OCCUPANCY_LISTBOX = (By.ID, "CURRENT_OCCUPANCY")
    LOCATOR_ASSERT_CURR_OCCUPANCY = (By.CSS_SELECTOR, 'span.ng-option-label.ng-star-inserted')
    LOCATOR_PROPOSED_OCCUPANCY_LISTBOX = (By.CSS_SELECTOR, "[formcontrolname = 'PROPOSED_OCCUPANCY']")
    LOCATOR_ASSERT_PROP_OCCUPANCY = (By.CSS_SELECTOR, 'span.ng-option-label.ng-star-inserted')
    LOCATOR_CHECKBOX_TEXT = (By.CSS_SELECTOR, "label[for='checkMarket']:nth-child(3)")
    LOCATOR_CHECKBOX_BUTTON = (By.ID, "switchFullname")
    LOCATOR_ADD_NEW_PERSON_BUTTON = (By.CSS_SELECTOR, "div.addDeal")
    LOCATOR_FIRST_NAME_INPUT = (By.ID, "1NAME")
    LOCATOR_MIDDLE_NAME_INPUT = (By.ID, "1MIDDLE_NAME")
    LOCATOR_LAST_NAME_INPUT = (By.ID, "1LAST_NAME")
    LOCATOR_ADD_ENTITY_BUTTON = (By.CSS_SELECTOR, "div.addDeal:nth-child(2)")
    LOCATOR_ENTITY_LISTBOX = (By.CSS_SELECTOR, "[formcontrolname='TYPE_OF_ENTITY'] .ng-select-container")
    LOCATOR_ASSERT_ENTITY = (By.CSS_SELECTOR, 'span.ng-option-label.ng-star-inserted')
    LOCATOR_ENTITY_NAME_INPUT = (By.ID, "0NAME_OF_ENTITY")
    LOCATOR_NEXT_BUTTON = (By.CSS_SELECTOR, ".row div.blue-btn")
    LOCATOR_IMG = (By.CSS_SELECTOR, "a[href*='property'] img")

class PropertyDetailsHelper(BasePage):

    def __init__(self, browser):
        super().__init__(browser)


    def asserting(self, selector, text):
        elements = self.find_elements(selector)
        for elem in elements:
            texting = elem.text
            if texting == text:
                return elem.click()
            else:
                print('not correct element')

    def checking_radio_button(self, elem):
        if(elem.text == "YES"):
            print("Кнопка в положении 'YES'")
        else:
            name_checkbox = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_CHECKBOX_BUTTON)
            name_checkbox.click()


    def modal_window(self):
        modal_later_button = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_MODAL_LATER_BUTTON)
        modal_later_button.click()


    def enter_address(self, line1_keys, city_keys, postal_keys):

        line1_input = self.find_element(PropertyDetailsLocators.LOCATOR_LINE1_INPUT)
        line1_input.clear()
        line1_input.send_keys(line1_keys)
        self.writing_in_test_log("line1_input", line1_keys)
        city_input = self.find_element(PropertyDetailsLocators.LOCATOR_CITY_INPUT)
        city_input.clear()
        city_input.send_keys(city_keys)
        self.writing_in_test_log("city_input", city_keys)
        postal_input = self.find_element(PropertyDetailsLocators.LOCATOR_POSTAL_INPUT)
        postal_input.clear()
        postal_input.send_keys(postal_keys)
        self.writing_in_test_log("postal_input", postal_keys)


    def clicking_listboxes(self, year_keys, curr_occupancy_item, prop_occupancy_item):
        year_input = self.find_element(PropertyDetailsLocators.LOCATOR_YEAR_INPUT)
        year_input.clear()
        year_input.send_keys(year_keys)
        self.writing_in_test_log("year_input", year_keys)
        current_occupancy_listbox = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_CURRENT_OCCUPANCY_LISTBOX)
        current_occupancy_listbox.click()
        self.asserting(PropertyDetailsLocators.LOCATOR_ASSERT_CURR_OCCUPANCY, curr_occupancy_item)
        self.writing_in_test_log("current_occupancy_listbox", curr_occupancy_item)
        proposed_occupancy_listbox = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_PROPOSED_OCCUPANCY_LISTBOX)
        proposed_occupancy_listbox.click()
        self.asserting(PropertyDetailsLocators.LOCATOR_ASSERT_PROP_OCCUPANCY, prop_occupancy_item)
        self.writing_in_test_log("proposed_occupancy_listbox", prop_occupancy_item)

    def turn_checkbox_button(self):
        checkbox_text = self.find_element(PropertyDetailsLocators.LOCATOR_CHECKBOX_TEXT)
        self.checking_radio_button(checkbox_text)
        self.writing_in_test_log("check_box", "YES")

    def click_add_person_button(self):
        add_new_button = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_ADD_NEW_PERSON_BUTTON)
        add_new_button.click()
        self.writing_in_test_log("add_new_button", "clicked")

    def enter_name(self, first_name_keys, middle_name_keys, last_name_keys):
        first_name_input = self.find_element(PropertyDetailsLocators.LOCATOR_FIRST_NAME_INPUT)
        first_name_input.send_keys(first_name_keys)
        self.writing_in_test_log("first_name_input", first_name_keys)
        middle_name_input = self.find_element(PropertyDetailsLocators.LOCATOR_MIDDLE_NAME_INPUT)
        middle_name_input.send_keys(middle_name_keys)
        self.writing_in_test_log("middle_name_input", middle_name_keys)
        last_name_input = self.find_element(PropertyDetailsLocators.LOCATOR_LAST_NAME_INPUT)
        last_name_input.send_keys(last_name_keys)
        self.writing_in_test_log("last_name_input", last_name_keys)

    def click_add_entity_button(self):
        add_entity_button = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_ADD_ENTITY_BUTTON)
        add_entity_button.click()
        self.writing_in_test_log("add_entity_button", "clicked")

    def enter_entity_listbox(self, entity_item, entity_name_keys):
        entity_listbox = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_ENTITY_LISTBOX)
        entity_listbox.click()
        self.asserting(PropertyDetailsLocators.LOCATOR_ASSERT_ENTITY, entity_item)
        self.writing_in_test_log("entity_listbox", entity_item)
        entity_name_input = self.find_element(PropertyDetailsLocators.LOCATOR_ENTITY_NAME_INPUT)
        entity_name_input.send_keys(entity_name_keys)
        self.writing_in_test_log("entity_name_input", entity_name_keys)

    def click_next_button(self):
        next_button = self.find_clickable_element(PropertyDetailsLocators.LOCATOR_NEXT_BUTTON)
        next_button.click()
        self.writing_in_test_log("next_button", "clicked")
        return AboutYouHelper(self.browser)

    # def assert_status_accepted(self):
    #     img = self.find_element(PropertyDetailsLocators.LOCATOR_IMG)
    #     imageUrl = img.get_attribute("src")
    #     assert imageUrl == "https://dev.borrowlabs.com/dashboard/assets/images/sidebar/status/accepted.svg", f"Property details status is not 'Accepted',image src -  {imageUrl} please check"
    #     self.writing_in_test_log("Статус страницы", "Accepted")

    #
    #
    # def assert_opened_page(self):
    #     URL = self.browser.current_url
    #     assert URL == "https://dev.borrowlabs.com/dashboard/loan/about?id=392", \
    #         f"The action URL is {URL} not 'https://dev.borrowlabs.com/dashboard/loan/about?id=392'"
    #     self.writing_in_test_log("Открыта страница", "About You")




    # def check_navigation_bar(self):
    #     all_list = self.find_elements(PropertyDetailsLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
    #     nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
    #     return nav_bar_menu