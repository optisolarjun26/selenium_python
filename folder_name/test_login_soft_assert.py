
import pytest
import softest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginFunctionality(softest.TestCase):
    def setup_method(self, method):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/login")

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_with_valid_credentials(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        current_url = driver.current_url
        success_message = driver.find_element(By.ID, "flash").text
        logout_button_displayed = driver.find_element(By.CSS_SELECTOR, "a.button.secondary.radius").is_displayed()
        header = driver.find_element(By.TAG_NAME, "h2").text

        self.soft_assert(self.assertEqual, current_url, "https://the-internet.herokuapp.com/secure", "URL did not match after login")
        self.soft_assert(self.assertIn, "You logged into a secure area!", success_message, "Success message did not match")
        self.soft_assert(self.assertTrue, logout_button_displayed, "Logout button is not displayed")
        self.soft_assert(self.assertEqual, header, "Secure Area", "Header did not match after login")
        
        self.assert_all()


if __name__ == "__main__":
    pytest.main()
