from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (Using Chrome in this example)
browser = webdriver.Chrome()

# Open the website
browser.get('https://learn.acloud.guru')

# Wait for the page to load
time.sleep(3)

# Locate the email and password fields by their IDs
email_field = browser.find_element(By.ID, '1-email')
password_field = browser.find_element(By.ID, '1-password')

# Input the email and password
email_field.send_keys('info@everestelites.com')
password_field.send_keys('Bodzud-zukca2-sikfif')

# Locate and click the login button
login_button = browser.find_element(By.ID, '1-submit')
login_button.click()

# Initialize WebDriverWait
wait = WebDriverWait(browser, 10)

# Check for the presence of the profile menu element
try:
    profile_menu = wait.until(EC.presence_of_element_located((By.ID, 'menu-list-:r9:-menuitem-:ra:')))
    print("Login successful")
except TimeoutException:
    print("Login failed or timeout reached")

# Continue with other actions or close the browser
# ...

# Close the browser after completing tasks
browser.quit()




# # Find and click the 'Start AWS Sandbox' button
# # You need to replace the 'button_text' with the actual text or identifier of the button
# aws_sandbox_button = browser.find_element(By.LINK_TEXT, 'Start AWS Sandbox')
# aws_sandbox_button.click()

# # Perform any additional actions or close the browser
# # browser.quit()


# # ... [previous login and button click code] ...

# # Wait for the credentials to be displayed
# wait = WebDriverWait(browser, 10)  # Wait for a maximum of 10 seconds

# # Assuming each piece of data has an ID or unique selector
# username = wait.until(EC.visibility_of_element_located((By.ID, 'username_id'))).text
# password = wait.until(EC.visibility_of_element_located((By.ID, 'password_id'))).text
# url = wait.until(EC.visibility_of_element_located((By.ID, 'url_id'))).text
# access_key = wait.until(EC.visibility_of_element_located((By.ID, 'access_key_id'))).text
# secret_key = wait.until(EC.visibility_of_element_located((By.ID, 'secret_key_id'))).text
# shutdown_time = wait.until(EC.visibility_of_element_located((By.ID, 'shutdown_time_id'))).text

# print(f"Username: {username}")
# print(f"Password: {password}")
# print(f"URL: {url}")
# print(f"Access Key ID: {access_key}")
# print(f"Secret Access Key: {secret_key}")
# print(f"Auto Shutdown: {shutdown_time}")

# # ... [rest of your code] ...
