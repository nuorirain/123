from selenium.webdriver.common.by import By
from components.component import Component

def test_check_footer_text(driver):
    driver.get("https://demoqa.com/")
    footer = Component(driver, (By.CSS_SELECTOR, "footer span"))
    text = footer.get_text()
    assert text == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.", \
        f"Ожидалось: '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.', но получено: '{text}'"
