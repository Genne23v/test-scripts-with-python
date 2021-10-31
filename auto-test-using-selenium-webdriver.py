from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://google.com')
element = driver.find_element_by_name('q')
element.send_keys('test')

from selenium.webdriver.common.keys import Keys

element.send_keys(Keys.RETURN)


# from selenium import webdriver
# driver = webdriver.Chrome()
driver.get('https://www.seleniumhq.org')
element = driver.find_element_by_xpath('//*[@id="choice"]/tbody/tr/td[1]/center/a[1]/img')
element.click()
