from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

# -- #
# customization
target = 'target'
message = 'message'
number_of_times = 2
delay_in_seconds = 5
user_data_dir = 'chrome://version/ to check your profile path'
# https://stackoverflow.com/questions/69246191/how-to-use-certain-chrome-profile-with-selenium-python
# -- #

# browser configs
options = webdriver.ChromeOptions()
options.add_argument(f'user-data-dir={user_data_dir}')

# init browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# search target
# search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Er7QU')))
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Search input textbox"]')))
time.sleep(1)
search_box.click()
search_box.send_keys(target)

# interact with target
# contact = search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_1Oe6M')))
contact = wait.until(EC.presence_of_element_located((By.XPATH, f"//span[@title='{target}']")))
time.sleep(1)
contact.click()

# write text
message_box = driver.find_element(By.XPATH, "//div[@title='Type a message']")
for i in range(number_of_times):
    message_box.send_keys(message + Keys.ENTER)
    if i != number_of_times - 1:
        time.sleep(delay_in_seconds)
    else:
        time.sleep(1)
