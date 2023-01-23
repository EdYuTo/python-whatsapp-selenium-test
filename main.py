from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.custom_chrome_driver import CustomChromeDriver

import src.fetcher as DF
import time

# -- #
# customization
target = 'contact name'
delay_in_seconds = 1

# See: https://stackoverflow.com/questions/69246191/how-to-use-certain-chrome-profile-with-selenium-python
user_data_dir = None
profile_directory = None
# -- #

# init browser
driver = CustomChromeDriver(user_data_dir, profile_directory)
driver.load_url("https://web.whatsapp.com/")

# search target
search_box = driver.wait_for_element(By.XPATH, '//div[@title="Search input textbox"]')
time.sleep(1)
search_box.click()
search_box.send_keys(target)

# interact with target
contact = driver.wait_for_element(By.XPATH, f"//span[@title='{target}']")
time.sleep(1)
contact.click()

# write text
message_box = driver.find_element(By.XPATH, "//div[@title='Type a message']")
messages = DF.getBrNationalAnthem()
for message in messages:
    message_box.send_keys(message + Keys.ENTER)
    if message != messages[-1]:
        time.sleep(delay_in_seconds)
    else:
        time.sleep(1)
