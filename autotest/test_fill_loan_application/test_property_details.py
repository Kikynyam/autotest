import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from pages.AboutYouPage import AboutYouHelper
from pages.IncomeAndEmploymentPage import EmploymentHelper
from pages.PreAppLoginPage import PreAppLoginHelper
from pages.NewLoanAppPage import NewLoanAppHelper
from pages.TrackRecordPage import TrackRecordHelper
from .pages.PropertyDetailsPage import PropertyDetailsHelper




def test_preapp_login_page(browser):
    pre_app_login_page = PreAppLoginHelper(browser)
    pre_app_login_page.go_to_site()
    pre_app_login_page.logging("ana.pa729cat@yandex.ru", "23456789")
    time.sleep(3)
    pre_app_login_page.submitting()

def test_new_loan_app_page(browser):
    new_loan_app_page = NewLoanAppHelper(browser)
    new_loan_app_page.creating()
    new_loan_app_page.switching_to_property_page()




def test_property_details_page(browser):
    property_detail_page = PropertyDetailsHelper(browser)

    time.sleep(2)

    property_detail_page.modal_window()
    time.sleep(2)

    property_detail_page.enter_address("1415 New Jersey", "New Hill", "08034-2210")

    time.sleep(2)

    browser.execute_script("window.scrollBy(0, 500);")

    time.sleep(2)

    property_detail_page.clicking_listboxes("2000", "Owner", "Vacant")

    time.sleep(2)

    browser.execute_script("window.scrollBy(0, 500);")

    time.sleep(2)

    property_detail_page.turn_checkbox_button()

    time.sleep(2)

    property_detail_page.click_add_person_button()

    time.sleep(2)

    property_detail_page.enter_name("Neo", "4", "Matrix")

    property_detail_page.click_add_entity_button()

    time.sleep(2)

    browser.execute_script("window.scrollBy(0, 200);")

    time.sleep(2)

    property_detail_page.enter_entity_listbox("Corporation", "Google")

    property_detail_page.click_next_button()

    time.sleep(2)

    # property_detail_page.assert_status_accepted()
    #
    # property_detail_page.assert_opened_page()

    # time.sleep(3)

def test_about_you_page(browser):

    about_you_page = AboutYouHelper(browser)

    about_you_page.enter_about_you("10", "Unmarried (includes divorced, widow)", "7,10")

    browser.execute_script("window.scrollBy(0, 200);")

    time.sleep(2)

    about_you_page.enter_present_address("i have small tits", "1")

    time.sleep(2)

    about_you_page.refreshing()

    time.sleep(2)

    browser.execute_script("window.scrollBy(0, 500);")

    about_you_page.turn_checkbox2_button()

    about_you_page.enter_diff_mail_address("NJ Springfield")

    time.sleep(2)

    about_you_page.refreshing()

    time.sleep(2)

    browser.execute_script("window.scrollBy(0, 700);")

    about_you_page.enter_former_address("Yessss", "1")

    time.sleep(2)

    about_you_page.refreshing()

    time.sleep(2)

    browser.execute_script("window.scrollBy(0, 1000);")

    time.sleep(2)

    about_you_page.add_new_former_address()

    browser.execute_script("window.scrollBy(0, 200);")

    about_you_page.enter_former_address2("TRARTAAT", "1")

    about_you_page.refreshing()

    time.sleep(3)

    browser.execute_script("window.scrollBy(0, 1200);")

    time.sleep(3)

    about_you_page.switch_to_track_record()

    time.sleep(5)


def test_track_record_page(browser):

    track_record_page = TrackRecordHelper(browser)

    time.sleep(3)

    track_record_page.enter_property1("Miami beach", "01/01/2020", "1000", "2000", "01/01/2020", "1000")

    time.sleep(3)

    browser.execute_script("window.scrollBy(0, 500);")

    track_record_page.enter_property2("Brighton beach", "01/01/2020", "1000", "2000", "01/01/2020", "1000")

    time.sleep(10)


# def test_income_and_employment(browser):
#
#     employment_page = EmploymentHelper(browser)
#     time.sleep(3)
#
#     employment_page.enter_income_and_employment("1000", "HellRoad666", "prayer", "(343)534-5345", "5", "10")
#
#     employment_page.turning_self_employed_checkbox()
#
#     time.sleep(3)
#
#     browser.execute_script("window.scrollBy(0, 400);")
#
#     time.sleep(3)
#
#     employment_page.click_next_button_to_your_assets()
#
#     time.sleep(5)












