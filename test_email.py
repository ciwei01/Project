import time
from selenium import webdriver


driver = webdriver.Chrome(executable_path='C:\\webdriver\\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://mail.126.com')
driver.switch_to.frame('x-URS-iframe1566703827612.9866')
driver.implicitly_wait(5)
driver.find_element_by_id('lbNormal').click()
driver.implicitly_wait(1)
driver.find_element_by_id('auto-id-1566703842417').send_keys('good')