from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from ddt import ddt, data, unpack


#https://the-internet.herokuapp.com
#data driven test
test_credentials=[("tomsmith","SuperSecretPassword!","Logged In"),("invaliduser","SuperSecretPassword!","username is invalid"),("tomsmith","jerry","password is invalid")]


@ddt
class LoginDDTTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")

    @data(*test_credentials)
    @unpack   
    def test_login(self, username, password, expected_message):
        driver=self.driver
        driver.find_element(By.ID,"username").send_keys(username)
        driver.find_element(By.ID,"password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # driver.find_element(By.CSS_SELECTOR,"button-radius").click()
        time.sleep(2)

        flash_message=driver.find_element(By.ID, "flash").text

        self.assertIn(expected_message, flash_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()