from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # Defining driver options and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)
        service = Service("chromedriver-mac-arm64/chromedriver")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):

        # Loading webpage
        self.driver.get("https://demoqa.com/login")

        # Web scraping to get username and password fields
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Sending our values to the fields
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, cur_address, per_address):
        # Locate the Elements dropdown and text box
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located
                                                        ((By.XPATH, '//*[@id="app"]/div/div/'
                                                                    'div/div[1]/div/div/'
                                                                    'div[1]/span/div')))
        elements.click()

        textbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        textbox.click()

        # Locate the form fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(cur_address)
        permanent_address_field.send_keys(per_address)

        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Locate upload and download
        updown_field = self.driver.find_element((By.ID, 'item-7'))
        self.driver.execute_script("arguments[0].click();", updown_field)

        # Click download button
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login('sel-username', 'SelPassword123')
    webautomation.fill_form('John Cena', 'john.cena@gmail.com',
                            'Cena Street, West Newbury, Massachusetts, USA',
                            'Cena Street, West Newbury, Massachusetts, USA')
    webautomation.download()
    webautomation.close()
