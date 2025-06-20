from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DropdownPage:
    URL = "https://the-internet.herokuapp.com/dropdown"
    DROPDOWN = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def select_option(self, value="Option 2"):
        dropdown_element = self.driver.find_element(*self.DROPDOWN)
        Select(dropdown_element).select_by_visible_text(value)
