from selenium.webdriver.common.by import By

class CheckboxPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CHECKBOXES = (By.CSS_SELECTOR, "#checkboxes input")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        return self.driver.find_elements(*self.CHECKBOXES)

    def check_first_uncheck_second(self):
        checkboxes = self.get_checkboxes()
        if not checkboxes[0].is_selected():
            checkboxes[0].click()
        if checkboxes[1].is_selected():
            checkboxes[1].click()
