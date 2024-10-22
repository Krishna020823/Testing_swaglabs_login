import time

from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://www.saucedemo.com/v1/index.html')  # Replace with your actual login URL
    context.login_page = LoginPage(context.driver)


@when('I enter valid credentials')
def step_impl(context):
    context.login_page.login('standard_user', 'secret_sauce')


@when('I add an item to the cart')
def step_impl(context):
    context.product_page = ProductPage(context.driver)
    context.product_page.add_item_to_cart()
    time.sleep(3)


@when('I go to checkout')
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.go_to_checkout()
    checkout_button = context.driver.find_element(By.XPATH, "//a[@class='btn_action checkout_button']")
    checkout_button.click()
    time.sleep(4)


@when('I fill out the checkout details')
def step_impl(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.fill_checkout_details("Krishna", "Yadav", "12345")


@then('I complete the checkout process')
def step_impl(context):
    context.checkout_page.complete_checkout()
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//a[@class='btn_action cart_button']").click()


@then('I should logout')
def step_impl(context):
    logout = context.driver.find_element(By.XPATH, "//div[@class='bm-burger-button']")
    logout.click()
    time.sleep(2)
    logout_click=context.driver.find_element(By.ID ,"logout_sidebar_link")
    logout_click.click()
    print("Order Placed Successfully !")
