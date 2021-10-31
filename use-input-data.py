import gspread, time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspead.authorize(creds)

sheet = client.open('TextFieldInputs').sheet1

all_values = sheet.get_all_values()

input_data = []
for row in all_values[1:]:
    input_data.append(row[1])

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://opensource.demo.orangehrmlive.com/index.php/leave/assignLeave')

def login(driver):
    user_name = driver.find_element_by_id('txtUsername')
    pwd = driver.find_element_by_id('txtPassword')

    user_name.send_keys('Admin')
    pwd.send_keys('admin')

    login_button = driver.find_element_by_id('btnLogin')
    login_button.click()

login(driver)

driver.find_element_by_id('assignleave_txtEmployee_empName').send_keys('John Smith')

leave_types = driver.find_element_by_id('assignleave_txtLeaveType')
leave_type_options = leave_types.find_elements_by_tag_name('option')
for option in leave_type_options:
    if option.get_attribute('value') == '2':
        option.click()
        break

start_date = driver.find_element_by_id('assignleave_txtFromDate')
end_date = driver.find_element_by_id('assignleave_txtToDate')

start_date.click()
start_date.send_keys('2018-04-01')
start_date.send_keys(Keys.RETURN)
time.sleep(0.5)

end_date.click()
end_date.send_keys(Keys.CONTROL + 'a')
end_date.send_keys('2018-04-08')
end_date.send_keys(Keys.ENTER)

for input_item in input_data:
    comment_text_area = driver.find_element_by_id('assignleave_textComment')
    assign_button = driver.find_element_by_id('assignBtn')
    comment_text_area.send_keys(input_item)
    time.sleep(0.5)
    assign_button.click()
    time.sleep(0.5)
    driver.find_element_by_id('confirmOkButton').click()
    time.sleep(0.5)