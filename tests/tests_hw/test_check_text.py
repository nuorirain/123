from selenium.webdriver.common.by import By
from components.component import Component

def test_check_footer_text(driver):
    driver.get("https://demoqa.com/")
    footer = Component(driver, (By.CSS_SELECTOR, "footer span"))
    text = footer.get_text()
    assert text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.", \
        f"Ожидалось: '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.', но получено: '{text}'"


def test_check_elements_text(driver):
    driver.get("https://demoqa.com/")
    button = Component(driver, (By.XPATH, "//h5[text()='Elements']"))
    button.find_element(button.locator).click()
    
    center_text = Component(driver, (By.CSS_SELECTOR, "div.main-header ~ div"))
    text = center_text.get_text()
    assert text == "Please select an item from left to start practice.", \
        f"Ожидалось: 'Please select an item from left to start practice.', но получено: '{text}'"
