import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# SETUP: Create ChromeDriver with download dir
download_dir = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_dir, exist_ok=True)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(5)

# ==========================
# 1. FILE UPLOAD
# ==========================
driver.get("https://the-internet.herokuapp.com/upload")

# Replace with your actual file
file_path = os.path.abspath("sample.txt")

upload_input = driver.find_element(By.ID, "file-upload")
upload_input.send_keys(file_path)

driver.find_element(By.ID, "file-submit").click()

success = driver.find_element(By.TAG_NAME, "h3").text
assert "File Uploaded!" in success
print(" File Upload Passed")

time.sleep(2)


driver.get("https://the-internet.herokuapp.com/download")

# Download the first file in the list
file_link = driver.find_element(By.CSS_SELECTOR, ".example a")
filename = file_link.text
file_link.click()

print(f"Downloading file: {filename}")

# Wait for file to be downloaded
downloaded_file_path = os.path.join(download_dir, filename)
timeout = 10
while timeout > 0:
    if os.path.exists(downloaded_file_path):
        print(f" File Downloaded: {downloaded_file_path}")
        break
    time.sleep(1)
    timeout -= 1
else:
    print(" File download failed or timed out.")

driver.quit()
