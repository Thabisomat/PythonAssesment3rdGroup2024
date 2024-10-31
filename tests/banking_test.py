import pytest

from pages.customerLoginPage import CustomerLoginPage
from utils.readCustomerDetails import ReadData


class Banking_test:
      bankingURL = ReadData().getUrl()
      Customer1 = ReadData().getCustomer1_name()
      Account1 = ReadData().getCustomer1_accounts()
#Customer2 = ReadData().getCustomer2_name()
# Account2 = ReadData().getCustomer2_accounts()
# Customer3 = ReadData().getCustomer3_name()
# Account3 = ReadData().getCustomer3_accounts()
# Customer4 = ReadData().getCustomer4_name()
# Account4 = ReadData().getCustomer4_accounts()
# Customer5 = ReadData().getCustomer5_name()
# Account5 = ReadData().getCustomer5_accounts()
      @pytest.mark.bank
      def test_loginBanking(self, browserSetup):
        self.driver = browserSetup
        self.driver.maximize_window()
        self.login=CustomerLoginPage()
