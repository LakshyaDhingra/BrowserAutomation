from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Defining driver options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service("chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(options=chrome_options, service=service)

# Loading webpage
driver.get("https://demoqa.com/login")

# Web scraping to get username and password fields
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Sending our values to the fields
username_field.send_keys('sel-username')
password_field.send_keys('SelPassword123$')
driver.execute_script("arguments[0].click();", login_button)

# Conditions to close the browser
input("Press Enter to close the Browser")
driver.quit()
