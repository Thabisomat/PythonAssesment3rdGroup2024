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
