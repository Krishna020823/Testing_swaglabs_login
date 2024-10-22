import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com/v1/')
    context.login_page = LoginPage(context.driver)


@when('I enter valid credentials')
def step_impl(context):
    context.login_page.login('standard_user', 'secret_sauce')


@then('I should be logged in successfully')
def step_impl(context):
    time.sleep(1)
    logout_menu = context.driver.find_element(By.XPATH, "//div[@class='bm-burger-button']")
    logout_menu.click()
    time.sleep(2)
    logout_button = context.driver.find_element(By.ID, 'logout_sidebar_link')
    logout_button.click()
    time.sleep(2)
    context.driver.quit()
