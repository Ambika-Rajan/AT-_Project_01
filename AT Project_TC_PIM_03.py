from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Set up the path to your WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the OrangeHRM login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step 2: Log in
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Admin")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("admin123")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Step 3: Navigate to the PIM module
    pim_module = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']"))
    )
    pim_module.click()

    # Step 4: Select an employee from the list to delete
    # Assuming we're deleting the first employee in the list
    employee_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[1]"))
    )
    employee_checkbox.click()

    # Step 5: Click the delete button
    delete_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete')]")
    delete_button.click()

    # Step 6: Confirm the deletion
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Yes, Delete')]"))
    )
    confirm_button.click()

    # Step 7: Verify the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-toast oxd-toast--success']"))
    )

    print("Success message:", success_message.text)

finally:
    # Close the browser
    driver.quit()
