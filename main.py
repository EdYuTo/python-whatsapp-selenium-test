from selenium.webdriver.common.by import By
from src.custom_chrome_driver import CustomChromeDriver

import time

# -- #
# customization
target = 'contact name'
number_of_times = 10
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

# send sticker
driver.wait_for_element(By.XPATH, '//span[@data-testid="smiley"]').click()
driver.wait_for_element(By.XPATH, '//span[@data-testid="sticker"]').click()
sticker = driver.wait_for_element(By.XPATH, '//img[@class="_3t1hO _1aShU ZRhsD"]') # set your sticker
for i in range(number_of_times):
    sticker.click()
    if i != number_of_times - 1:
        time.sleep(delay_in_seconds)
    else:
        time.sleep(1)
