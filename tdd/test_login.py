import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.login_page import LoginPage  
from selenium.webdriver.chrome.options import Options

class LoginTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(5)
        self.login_page = LoginPage(self.driver)
        self.login_page.load()

    def test_valid_login(self):
        self.login_page.login("tomsmith", "SuperSecretPassword!")
        flash_message = self.login_page.get_flash_message()
        self.assertIn("You logged into a secure area!", flash_message)

    def test_invalid_login(self):
        self.login_page.login("invalid_user", "invalid_password")
        flash_message = self.login_page.get_flash_message()
        self.assertIn("Your username is invalid!", flash_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
   