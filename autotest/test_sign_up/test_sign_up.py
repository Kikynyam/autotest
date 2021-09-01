import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Успешная регистрация с корректным Email и Password (в ручную через калькулятор) test-case#1

def test_signing_up_with_calculator(browser):
    link = "https://dev.borrowlabs.com/"
    browser.get(link)
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 10)

    rate_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rate a")))
    rate_button.click()

    demo_password_input = wait.until(EC.visibility_of_element_located((By.ID, "passwordInput")))
    demo_password_input.send_keys("12345")

    demo_button = wait.until(EC.element_to_be_clickable((By.ID, "loginPassBtn")))
    demo_button.click()

    time.sleep(5)

    #Property

    state_select = Select(browser.find_element_by_id("state-select"))
    state_select.select_by_visible_text("New Jersey")  # ищем элемент с текстом "New Jersey"

    # wait for dropdown to exist
    browser.execute_script("document.getElementById('propertyTypeSelect').style.display='inline-block';")
    wait.until(EC.presence_of_element_located((By.ID, "propertyTypeSelect")))
    type_select = Select(browser.find_element_by_id("propertyTypeSelect"))
    type_select.select_by_value("Single Family")  # ищем элемент с value "Single Family"

    browser.execute_script("window.scrollBy(0, 300);")
    time.sleep(5)


    #Value and Loan
    browser.find_element_by_id("headingTwo").click()
    time.sleep(5)

    purchase_input = wait.until(EC.visibility_of_element_located((By.ID, "BuyingValue")))
    purchase_input.send_keys("500000")

    downpayment_input = wait.until(EC.visibility_of_element_located((By.ID, "downpaymentValue")))
    downpayment_input.send_keys("100000")


    #Borrower
    browser.find_element_by_css_selector("div[data-target ='#collapseThree']").click()
    time.sleep(5)

    browser.execute_script("document.querySelector('select[name = 'TRACK_RECORD']').style.display='inline-block';")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name ='TRACK_RECORD']")))
    number_of_deals_select = Select(browser.find_element_by_css_selector("select[name ='TRACK_RECORD']"))
    number_of_deals_select.select_by_value("More")  # ищем элемент с value "More"

    # browser.execute_script("document.getElementByName('CREDIT_SCORE').style.display='inline-block';")
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name ='CREDIT_SCORE']")))
    # credit_score_select = Select(browser.find_element_by_css_selector("select[name ='CREDIT_SCORE']"))
    # credit_score_select.select_by_value("700 and more: Hall of Fame worthy!")  # ищем элемент с value "700 and more..."

    #See your rate
    # browser.find_element_by_id("buyingSubmitBtn").click()









# Signing up with Google test-case#2
@pytest.mark.skip()
def test_signing_up_with_google_acc(browser):
    link = "https://dev.borrowlabs.com/signup"
    browser.get(link)
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 10)

    google_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.social a:first-of-type")))
    google_button.click()

    email_input = wait.until(EC.visibility_of_element_located((By.NAME, "identifier")))
    email_input.send_keys("anastasiya.pavlova@borrowlabs.com")

    next_button = browser.find_element_by_xpath("//div[@id='identifierNext']/div/button")
    next_button.click()
    time.sleep(5)

    password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_input.send_keys("BlackMambo666")

    next1_button = browser.find_element_by_xpath("//div[@id='passwordNext']/div/button")
    next1_button.click()
    time.sleep(50)

    URL = browser.current_url

    assert URL == "https://dev.borrowlabs.com/dashboard/loans",\
           f"The action URL is {URL} not 'https://dev.borrowlabs.com/dashboard/loans'"




# Signing up with LinkedIn test-case#4
@pytest.mark.skip()
def test_signing_up_with_linkedin_acc(browser):
    link = "https://dev.borrowlabs.com/signup"
    browser.get(link)
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 10)

    linkedin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.social a:nth-child(4)")))
    linkedin_button.click()

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "username")))
    email_input.send_keys("dan.worldeconomy@gmail.com")

    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("Hw2pts?x*8Lm9EE")

    submit_button = browser.find_element_by_css_selector(".login__form_action_container button")
    submit_button.click()
    time.sleep(10)

    URL = browser.current_url

    assert URL == "https://dev.borrowlabs.com/dashboard/loans",\
           f"The action URL is {URL} not 'https://dev.borrowlabs.com/dashboard/loans'"












