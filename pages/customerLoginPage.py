

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerLoginPage:
    button_CustomerLogins_xpath = "//button[contains(.,'Customer Login')]"

    def __init__(self, driver):
        self.driver = driver

    def clickCustomerLoginsButton(self):
        self.driver.find_element(By.XPATH, self.button_CustomerLogins_xpath).click()
