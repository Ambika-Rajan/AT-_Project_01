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

    # Step 4: Locate the employee to edit
    # Assuming we're editing the first employee in the list
    edit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(), 'Edit')])[1]"))
    )
    edit_button.click()

    # Step 5: Edit employee information
    # Example: Change the first name
    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )
    first_name_input.clear()  # Clear the existing name
    first_name_input.send_keys("Jane")  # Update to new name

    # Optional: You can edit other fields as necessary

    # Step 6: Click 'Save'
    save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
    save_button.click()

    # Step 7: Verify the success message
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-toast oxd-toast--success']"))
    )

    print("Success message:", success_message.text)

finally:
    # Close the browser
    driver.quit()
