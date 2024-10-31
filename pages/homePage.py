from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_dropdown = (By.ID, "userSelect")
        self.login_button = (By.XPATH, "//button[contains(text(), 'Login')]")

    def select_customer(self, customer_name):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.customer_dropdown)).click()
        customer_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[contains(text(), '{customer_name}')]")))
        customer_option.click()

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
