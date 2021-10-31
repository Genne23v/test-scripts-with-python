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

driver.back()

search_element = driver.find_element_by_id('q')
search_element.send_keys('webdriver')

go_button = driver.find_element_by_id('submit')
go_button.click()

import time
time.sleep(1)
driver.switch_to_frame('master-1')
link_elements = driver.find_elements_by_tag_name('a')
link_elements[0].get_attribute('href')


# from selenium import webdriver
# driver = webdriver.Chrome()
driver.get('http://www.phptravels.net/offers')
b_tags = driver.find_elements_by_tag_name('b')
price_list = []
for b in b_tags:
    price_list.append(b.text)

print (price_list)

clean_price_list = []

for price in price_list:
    if price.startswith('USD'):
        price_number = price[5:]
        integer_price = int(price_number.replace(',',''))
        clean_price_list.append(integer_price)

print(clean_price_list)

# from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver = webdriver.Chrome()

url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
driver.get(url)

product_containers = driver.find_elements_by_class_name('product-container')

for product_container in enumerate(product_containers):
    hover = ActionChains(driver).move_to_element(product_container)
    hover.perform()
    driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span').click()
    time.sleep(0.5)

