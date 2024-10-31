from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerAccountPage:

    def __init__(self, driver):
        self.driver = driver

    def select_account(self, account_index=0):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "accountSelect"))
        )
        accounts = self.driver.find_elements(By.ID, "accountSelect")
        accounts[account_index + 1].click()


def deposit(self, amount):
    WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Deposit')]"))
    ).click()

    deposit_input = self.driver.find_element(By.XPATH, "//input[@ng-model='amount']")
    deposit_input.send_keys(amount)
    self.driver.find_element(By.XPATH, "//button[text()='Deposit']").click()
