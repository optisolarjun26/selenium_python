from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time


# Initialize Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)

# ========== 1. Checkboxes ==========
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

# Check first checkbox if not already checked
if not checkboxes[0].is_selected():
    checkboxes[0].click()
    print("Checked checkbox 1")

# Uncheck second checkbox if checked
if checkboxes[1].is_selected():
    checkboxes[1].click()
    print("Unchecked checkbox 2")

time.sleep(2)

# ========== 2. Dropdown ==========
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")
print("Selected 'Option 2' from dropdown")

time.sleep(2)

# ========== 3. Mouse Hover ==========
driver.get("https://the-internet.herokuapp.com/hovers")

# Hover over the first figure box
figures = driver.find_elements(By.CLASS_NAME, "figure")
hover = ActionChains(driver)
hover.move_to_element(figures[0]).perform()

# Wait to show hover effect
print("Hovered over first figure")
time.sleep(2)

# Click on the profile link revealed on hover
profile_link = figures[0].find_element(By.TAG_NAME, "a")
profile_link.click()
print("Clicked on 'View profile'")

time.sleep(2)
driver.back()  # Navigate back to continue

# ========== 4. Simulating Radio Button ==========
# Herokuapp has no real radio buttons, but you can simulate using dropdown/checkboxes or custom logic

print("No native radio button page found, skipping radio test")

# ========== Close Browser ==========
driver.quit()
