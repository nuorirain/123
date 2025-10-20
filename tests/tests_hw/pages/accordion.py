from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Accordion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = "https://demoqa.com/accordian"
        self.section1 = (By.ID, "section1Heading")
        self.section2 = (By.ID, "section2Heading")
        self.section3 = (By.ID, "section3Heading")
