import configparser

config=configparser.RawConfigParser()
config.read("./configurations/browser.ini")

class ReadData():
    def getUrl(self):
        return config.get("URL","protructorPracticeUrl")