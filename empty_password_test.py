import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def incorrect_login():
    driver.get(url="https://www.datart.cz/")
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="c-p-bn"]').click()
    time.sleep(2)

    try:
        login_button = driver.find_element(By.XPATH, '//*[@id="snippet--header-user"]/div/div[1]/span')
        login_button.click()
        time.sleep(3)
        login_field = driver.find_element(By.ID, 'frm-login')
        login_field.clear()

        password_field = driver.find_element(By.ID, 'frm-password')
        password_field.clear()

        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-login")
        submit_button.click()
        time.sleep(3)

        message = driver.find_element(By.XPATH,
                                      '//*[@id="snippet--header-loginForm-dialog"]/form/div[1]/div/label/span[2]/span[2]').text
        empty_password_message = "Povinný údaj"

        if message == empty_password_message:
            print('Incorrect password - Test Passed')
        else:
            print('Incorrect password - Test Failed')

        time.sleep(2)


    except NoSuchElementException:
        print("Unable to locate element")
        return None


    finally:
        driver.close()
        driver.quit()


incorrect_login()
