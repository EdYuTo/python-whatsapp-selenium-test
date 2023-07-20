from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CustomChromeDriver:
    def __config(self, user_data_dir: str=None, profile_directory: str=None):
        options = webdriver.ChromeOptions()

        if user_data_dir is not None:
            options.add_argument(f'user-data-dir={user_data_dir}')
        if profile_directory is not None:
            options.add_argument(f'--profile-directory={profile_directory}')

        return options

    def __init__(self, user_data_dir: str=None, profile_directory: str=None, timeout: int=60):
        options = self.__config(user_data_dir, profile_directory)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, timeout)

    def load_url(self, url):
        self.driver.get(url)
    
    def switch_to_tab(self, tab):
        self.driver.switch_to.window(self.driver.window_handles[tab])
    
    def wait_for_element(self, by=By.ID, value: str=None):
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    def find_elements(self, by=By.ID, value: str=None):
        return self.driver.find_elements(by, value)

    def find_element(self, by=By.ID, value: str=None):
        return self.driver.find_element(by, value)

    def execute_script(self, script):
        self.driver.execute_script(script)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()