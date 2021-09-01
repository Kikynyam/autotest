import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Sign in case №5 Успешный Log in с корректным Email и Password (в ручную)
@pytest.mark.skip
def test_signing_in(browser):
    link = "https://dev.borrowlabs.com/"
    browser.get(link)
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 10)

    browser.execute_script("window.scrollBy(0, 500);")

    log_in_button = browser.find_element_by_class_name("loans-index")
    log_in_button.click()

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys("ana.pa729cat@yandex.ru")

    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("123456")

    submit_button = browser.find_element_by_class_name("blue-btn")
    submit_button.click()
    time.sleep(30)

    URL = browser.current_url

    assert URL == "https://dev.borrowlabs.com/dashboard/loans",\
           f"The action URL is {URL} not 'https://dev.borrowlabs.com/dashboard/loans'"


# №7 Успешный Log in с корректным Email и Password (через соц-сети Google через Sing up)
@pytest.mark.skip
def test_signing_in_with_google_acc(browser):
    link = "https://dev.borrowlabs.com/login"
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



#№9 Успешный Log in с корректным Email и Password (через соц-сети Linkedin через Sing up)
@pytest.mark.skip
def test_signing_in_with_linkedin_acc(browser):
    link = "https://dev.borrowlabs.com/login"
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


#№10 Restore password
def test_restoring_password(browser):
    link = "https://dev.borrowlabs.com/login"
    browser.get(link)
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 10)

    restore_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-target='#restorePassword']")))
    restore_button.click()

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "restorePasswordInput")))
    email_input.send_keys("ana.pa729cat@yandex.ru")

    restore_password_button = browser.find_element_by_id("restorePassBtn")
    restore_password_button.click()

    browser.execute_script("window.open()")
    browser.switch_to.window(browser.window_handles[1])
    browser.get("https://passport.yandex.ru/auth?from=mail&origin=hostroot_homer_auth_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F%3Fuid%3D113572612&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1")

    login_input = wait.until(EC.visibility_of_element_located((By.ID, "passp-field-login")))
    login_input.send_keys("ana.pa729cat")

    submit_button = browser.find_element_by_css_selector("[type='submit']")
    submit_button.click()

    login_input = wait.until(EC.visibility_of_element_located((By.ID, "passp-field-passwd")))
    login_input.send_keys("dow66jones66")

    login_button = browser.find_element_by_css_selector("[type='submit']")
    login_button.click()

    time.sleep(30)

    first_letter = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mail-MessagesList a:nth-of-type(1)")))
    first_letter.click()

    time.sleep(20)

    reset_password_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".dbea1dc6b1175adbwrap-table-email a")))
    reset_password_button.click()

    time.sleep(10)

    browser.switch_to.window(browser.window_handles[2])

    new_password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    new_password_input.send_keys("23456789")

    renew_password_input = wait.until(EC.visibility_of_element_located((By.ID, "repeatPassword")))
    renew_password_input.send_keys("23456789")

    change_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#restorePasswordForm button")))
    change_button.click()

    time.sleep(10)

    browser.switch_to.window(browser.window_handles[3])

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    email_input.send_keys("ana.pa729cat@yandex.ru")

    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_input.send_keys("23456789")

    submit_button = browser.find_element_by_class_name("blue-btn")
    submit_button.click()

    time.sleep(20)

    URL = browser.current_url

    assert URL == "https://dev.borrowlabs.com/dashboard/loans", \
        f"The action URL is {URL} not 'https://dev.borrowlabs.com/dashboard/loans'"





