import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



def squid_login_test(p_url, p_account_url, p_username, p_password):

    try:
        # Initialize the WebDriver using Chrome
        driver = webdriver.Chrome()

        driver.get(p_url)
        print("Browser Opened at the right url") #this is for debugging to see if I can make it to this part

        # Wait for the username field to be present and then enter the username
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        username_field.send_keys(p_username)
        print("Username entered")

        # Wait for the password field and enter the password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))  # password field ID
        )

        password_field.send_keys(p_password)
        print("Password entered")

        # Wait for the login button and click it
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))   # Login Button XPATH
        )

        login_button.click()
        print("Login button clicked")

        # Add a wait here to check for successful login. For example, check for an element on the logged-in page.

        try:
            #WebDriverWait(driver, 20).until(
            #    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Portfolio Value')]"))  # Example. Replace with a reliable selector.
            #)
            #print("Login successful!")
            # Wait for the page to navigate to the desired URL.
            WebDriverWait(driver, 120).until(EC.url_to_be(p_account_url))

            # Wait for the target element to be present and retrieve its value.
            target_element = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH,
                                                "//*[@id=\"__next\"]/div[2]/div/div/div[2]/div[1]/main/section/div[1]/div[1]/div[1]/div[1]/div/div/div/div[2]/div/span/div/div/span[2]"))
            )
            element_value = target_element.text
            print(f"The portfolio balance value is: {element_value}")

        except Exception as e:
            print(f"Login might have failed or could not verify login: {e}")



    except Exception as e:
        print(f"Whoopsie! An error occurred: {e}")
    finally:
        # Close the browser
        if 'driver' in locals() and driver:
            driver.quit()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python main_calvin.py <login_url> <Account_Overview_Url> <username> <password>")
    else:
        url = sys.argv[1]
        account_url = sys.argv[2]
        username = sys.argv[3]
        password = sys.argv[4]
        squid_login_test(url, account_url, username, password)