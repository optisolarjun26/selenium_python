from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class HoverPage:
    URL = "https://the-internet.herokuapp.com/hovers"
    FIGURES = (By.CLASS_NAME, "figure")
    PROFILE_LINK = (By.LINK_TEXT, "View profile")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def hover_and_check_link_visible(self):
        figures = self.driver.find_elements(*self.FIGURES)
        hover = ActionChains(self.driver)
        hover.move_to_element(figures[0]).perform()

        # Find the link AFTER hover
        link = figures[0].find_element(*self.PROFILE_LINK)
        return link.is_displayed()

