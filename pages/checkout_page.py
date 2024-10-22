from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Locators for checkout form fields
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_CODE_FIELD = (By.ID, "postal-code")
    FINISH_BUTTON = (By.XPATH, "//input[@class='btn_primary cart_button']")

    def fill_checkout_details(self, first_name, last_name, zip_code):
        self.send_keys(*self.FIRST_NAME_FIELD, first_name)
        self.send_keys(*self.LAST_NAME_FIELD, last_name)
        self.send_keys(*self.ZIP_CODE_FIELD, zip_code)

    def complete_checkout(self):
        self.click(*self.FINISH_BUTTON)
