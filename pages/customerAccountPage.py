from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerAccountPage:
    textbox_selectedAccount_id = "accountSelect"
    button_deposit_xpath = "//button[contains(.,'Deposit')]"
    title_DepositSuccessful_xpath="//span[contains(.,'Deposit Successful')]"
    button_Logout="//button[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver = driver


    def select_account(self, account_index=0):
     WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, self.textbox_selectedAccount_id))
     )
     accounts = self.driver.find_elements(By.ID, self.textbox_selectedAccount_id)
     accounts[account_index + 1].click()


    def deposit(self, amount):
     WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, self.button_deposit_xpath))
     ).click()

     deposit_input = self.driver.find_element(By.XPATH, "//input[@ng-model='amount']")
     deposit_input.send_keys(amount)
     self.driver.find_element(By.XPATH, "//button[text()='Deposit']").click()

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 10)
        loginElement = wait.until(EC.visibility_of_element_located((By.ID, self.button_login_id)))
        loginElement.click()


    def verifySuccefullDeposit(self):
     wait = WebDriverWait(self.driver, 10)
     depositSuccessElement = wait.until(
        EC.visibility_of_element_located((By.XPATH,self.title_DepositSuccessful_xpath )))
     depositSuccessElement.is_displayed()


    def logout(self):
     self.driver.find_element(By.XPATH,self.button_Logout ).click()
