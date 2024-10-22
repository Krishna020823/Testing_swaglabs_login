from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locator for the "Add to Cart" button
    ADD_TO_CART_BUTTON = (By.XPATH, "(//button[@class='btn_primary btn_inventory'])[1]")

    def add_item_to_cart(self):
        self.click(*self.ADD_TO_CART_BUTTON)
