from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Enter the username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Admin")

    # Step 3: Enter an invalid password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Invalid password")

    # Step 4: Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Step 5: Wait for the error message to appear
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))
    )

    # Print the error message
    print("Error message:", error_message.text)

finally:
    # Close the browser
    driver.quit()
