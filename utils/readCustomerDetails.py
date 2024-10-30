import configparser

config=configparser.RawConfigParser()
config.read("./configurations/customerLogins.ini")

class ReadData():
    def getUrl(self):
        return config.get("URL","protructorPracticeUrl")
    def getCustomer1_name(self):
        return config.get("Customer1","customer1_username")
    def getCustomer1_accounts(self):
        return config.get("Customer1", "account_1").split(", ")
    def getCustomer2_name(self):
        return config.get("Customer2","customer2_username")

    def getCustomer2_accounts(self):
        return config.get("Customer2", "account_2").split(", ")
    def getCustomer3_name(self):
        return config.get("Customer3","customer3_username")

    def getCustomer3_accounts(self):
        return config.get("Customer3", "account_3").split(", ")
    def getCustomer4_name(self):
        return config.get("Customer4","customer4_username")

    def getCustomer4_accounts(self):
        return config.get("Customer4", "account_4").split(", ")
    def getCustomer5_name(self):
        return config.get("Customer5","customer5_username")

    def getCustomer5_accounts(self):
        return config.get("Customer5", "account_5").split(", ")