from configparser import ConfigParser
from Config.VarConfig import PageElementLocatorPath

class ParseCofigFile(object): 
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(PageElementLocatorPath)
        
        
    def getItemsSection(self,sectionName):
        optionsDict = dict(self.cf.items(sectionName))
        p=optionsDict["loginPage.frame".lower()].split(">")[1]
        print(p)
        print(optionsDict)
        return optionsDict
    
    def getOptionValue(self,sectionName,optionName):
        value = self.cf.get(sectionName, optionName)
        print(value)
        return value

if __name__ == "__main__":
    a=ParseCofigFile()
    a.getItemsSection("126mail_login")
    a.getOptionValue('126mail_login', 'loginPage.frame')