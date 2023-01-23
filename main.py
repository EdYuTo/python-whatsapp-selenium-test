from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

# TODO: extract with dependencies
def __waitForView(by=By.ID, value: str = None):
    wait = WebDriverWait(driver, 600)
    return wait.until(EC.presence_of_element_located((by, value)))

# -- #
# customization
target = 'target'
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

# search target
# search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Er7QU')))
search_box = __waitForView(By.XPATH, '//div[@title="Search input textbox"]')
time.sleep(1)
search_box.click()
search_box.send_keys(target)

# interact with target
# contact = search_box = wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_1Oe6M')))
contact = __waitForView(By.XPATH, f"//span[@title='{target}']")
time.sleep(1)
contact.click()

# send sticker
# driver.find_element(By.XPATH, '//button[@aria-label="Open emojis panel"]').click()
__waitForView(By.XPATH, '//span[@data-testid="smiley"]').click()
__waitForView(By.XPATH, '//span[@data-testid="sticker"]').click()
sticker = __waitForView(By.XPATH, '//img[@class="_3t1hO _1aShU ZRhsD"]') # set your sticker
for i in range(number_of_times):
    sticker.click()
    if i != number_of_times - 1:
        time.sleep(delay_in_seconds)
    else:
        time.sleep(1)
