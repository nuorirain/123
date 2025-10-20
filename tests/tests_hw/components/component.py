from pages.base_page import BasePage

class Component(BasePage):
    def __init__(self, driver, locator):
        super().__init__(driver)
        self.locator = locator

    def get_text(self):
        return str(self.find_element(self.locator).text)
