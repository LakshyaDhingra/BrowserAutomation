from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Defining driver options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

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

# Locate the Elements dropdown and text box
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/'
                                                                                       'div/div[1]/div/div/'
                                                                                       'div[1]/span/div')))
elements.click()

textbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
textbox.click()

# Locate the form fields and submit button
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill in form fields
fullname_field.send_keys('John Cena')
email_field.send_keys('john.cena@gmail.com')
current_address_field.send_keys('Cena Street, West Newbury, Massachusetts, USA')
permanent_address_field.send_keys('Cena Street, West Newbury, Massachusetts, USA')

driver.execute_script("arguments[0].click();", submit_button)

# Locate upload and download
updown_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="item-7"]')))
updown_field.click()

# Click download button
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)

# Conditions to close the browser
input("Press Enter to close the Browser")
driver.quit()
