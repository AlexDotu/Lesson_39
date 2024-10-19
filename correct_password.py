import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data import my_datart_login, my_datart_password

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def correct_login():
    driver.get(url="https://www.datart.cz/")
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="c-p-bn"]').click()

    time.sleep(2)

    try:
        login_button = driver.find_element(By.XPATH, '//*[@id="snippet--header-user"]/div/div[1]/span')
        login_button.click()
        time.sleep(3)
        print('=======1')
        login_field = driver.find_element(By.ID, 'frm-login')
        login_field.clear()
        login_field.send_keys(my_datart_login)
        print('=======2')

        password_field = driver.find_element(By.ID, 'frm-password')
        password_field.clear()
        password_field.send_keys(my_datart_password)

        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-login")
        submit_button.click()
        time.sleep(3)
        print('==3')
    

        dropdown_button = driver.find_element(By.XPATH, '//*[@id="snippet--header-user"]/div/div[1]/span')
        dropdown_button.click()
        print('====ok')
        time.sleep(2)

        try:
            logout_button = driver.find_element(By.XPATH, '//*[@id="snippet--header-user"]/div/div[2]/ul/li[10]/a')
            print('===I got it!')
            return True
        except NoSuchElementException:
            print(f"Unable to locate element, {logout_button}")
            return False

    finally:

        driver.close()
    driver.quit()


correct_login()
