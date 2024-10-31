from selenium import webdriver
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    text_yourName_xpath = "//label[contains(.,'Your Name :')]"
    text_UserSelect_id = "userSelect"

    def __init__(self, driver):
        self.driver = driver

    def verifySuccefulLogin(self):
        self.driver.find_element(By.XPATH, self.text_yourName_xpath).is_displayed()

    def UserSelect(self, userSelect):
        wait = WebDriverWait(self.driver, 10)
        UserSelectElement = wait.until(EC.visibility_of_element_located((By.ID, self.text_UserSelect_id)))
        UserSelectElement.Select(userSelect)
