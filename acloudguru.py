# PART 1 Login to ACloudGuru 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Initialize the WebDriver (Using Chrome in this example)
browser = webdriver.Chrome()

# Open the website
browser.get('https://learn.acloud.guru/cloud-playground/cloud-sandboxes')

# Wait for the page to load
time.sleep(3)

# Locate the email and password fields by their IDs
email_field = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, '1-email'))
)
password_field = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, '1-password'))
)

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
    browser.quit()
    exit(1)

# Wait for the page to load
time.sleep(5)

# _____________________________________________________________________________

# PART 2 Start AWS Sandbox

# Increase the timeout period for waiting for the 'Start AWS Sandbox' button
try:
    start_sandbox_button = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-cy='button--start-sandbox']"))
    )
    start_sandbox_button.click()
except TimeoutException:
    print("Failed to find the 'Start AWS Sandbox' button within the given time.")
    browser.quit()
    exit(1)

# Wait for the page to load
time.sleep(3)

# Locate the input elements for the username and password
credential_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input[aria-label='Copy to clipboard']")))

# Extract the values
# Assuming the first one is the username and the second is the password
username = credential_elements[0].get_attribute('value')
password = credential_elements[1].get_attribute('value')
url = credential_elements[2].get_attribute('value')
access_key_id = credential_elements[3].get_attribute('value')
secret_access_key = credential_elements[4].get_attribute('value')

# Print the credentials (for debugging purposes)
print(f"Username: {username}")
print(f"Password: {password}")
print(f"URL: {url}")
print(f"access_key_id: {access_key_id}")
print(f"secret_access_key: {secret_access_key}")

# Write the credentials to a file
with open('credentials.txt', 'w') as file:
    file.write(f"Username: {username}\n")
    file.write(f"Password: {password}\n")
    file.write(f"URL: {url}\n")
    file.write(f"access_key_id: {access_key_id}\n")
    file.write(f"secret_access_key: {secret_access_key}\n")

# Close the browser after completing tasks
browser.quit()
