from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        element.send_keys(text)
