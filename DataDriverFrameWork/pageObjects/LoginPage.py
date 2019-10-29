from util.ObjectMap import *

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        
    def switchToFrame(self):
        self.driver.switch_to.frame("x-URS-iframe")
        
    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()
        
    def userNameObj(self):
        try:
            elementObj = getElement(self.driver,
                                    "xpath",'//input[@name = "email"]')
            return elementObj 
        except Exception as e:
            raise e