from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # Locator for the "Checkout" button
    CART_BUTTON = (By.XPATH, "//div[@id='shopping_cart_container']")

    def go_to_checkout(self):
        self.click(*self.CART_BUTTON)
