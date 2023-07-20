from selenium.webdriver.common.by import By

from src.custom_chrome_driver import CustomChromeDriver

import time

# Constants #
user_data_dir = 'D:\Python\zap\.session'
profile_directory = None
green_continue = '@class="_3HhhB _2NolF _275sd _1ZefG _2orIw _3PphB _9C_ii"'
yellow_continue = '@class="_3HhhB _2NolF _275sd _1ZefG _2orIw _3MQZc _1u49Q"'
red_continue = '@class="_3HhhB _2NolF _275sd _1ZefG _2orIw _3nf-s NAidc"'
play_button_1 = '@class="_16h82 WOZnx _275sd _1ZefG _13TEM _2HRY_"'
play_button_2 = '@class="_3XvZO _3HhhB _2NolF _275sd _1ZefG FKD2y"'
# --------- #

driver = CustomChromeDriver(user_data_dir, profile_directory, 15)

driver.load_url('https://www.duolingo.com/practice-hub')
driver.execute_script('window.open("https://translate.google.com/?sl=fr&tl=en","_blank");')
driver.switch_to_tab(0)

def quit_game():
    driver.wait_for_element(By.XPATH, '//button[@class="_1H_R6 _1ZefG _2hiHn"]').click()
    driver.wait_for_element(By.XPATH, '//button[@class="_3HhhB _2NolF _275sd _1ZefG _3yQTJ _27Lhl"]').click()

def play_game():
    last_phrase = ""
    repetition_count = 0
    while True:
        # audio_button = driver.wait_for_element(By.XPATH, '//button[@class="_1KXUd _1I13x _2kfEr _1nlVc _2fOC9 UCrz7 t5wFJ"]')
        time.sleep(1)
        try:
            speak_button = driver.wait_for_element(By.XPATH, f'//button[{play_button_1}] | //button[{play_button_2}]')            
        except:
            print("No more play button")
            break
        text = " ".join([element.text for element in driver.driver.find_elements(By.XPATH, '//div[@class="_34k_q _3Lg1h _13doy"]')])
        if last_phrase == text:
            if repetition_count == 3:
                print("Quit game")
                quit_game()
                break
            else:
                repetition_count += 1
        else:
            repetition_count = 0
        print(text)
        last_phrase = text
        speak_button.click()

        driver.switch_to_tab(1)
        try:
            # Clean text
            driver.find_element(By.XPATH, '//button[@class="VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe yHy1rc eT1oJ mN1ivc ZihNHd GA2I6e"]').click()
            time.sleep(1)
        except:
            pass
        # Paste text
        driver.find_element(By.XPATH, '//textarea[@aria-label="Source text"]').send_keys(text)
        time.sleep(2)
        try:
            # did you mean?
            driver.find_element(By.XPATH, '//span[@class="mvqA2c"]').click() 
            time.sleep(1)
        except:
            pass 
        # Play audio
        driver.wait_for_element(By.XPATH, '//button[@class="VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe fzRBVc tmJved mN1ivc rrPCWc"]').click()
        driver.switch_to_tab(0)

        # Continue
        driver.wait_for_element(By.XPATH, f'//button[{green_continue}] | //button[{yellow_continue}] | //button[{red_continue}]').click()

while True:
    print("(Re)Start")

    # Tap voice practice
    practice_card = driver.wait_for_element(By.XPATH, '//button[@class="_1H_R6 _1ZefG vJj1P"][position()=2]')
    practice_card.click()

    # Tap continue
    continue_button = driver.wait_for_element(By.XPATH, '//button[@class="_3HhhB _2NolF _275sd _1ZefG _4Mmno _2RNzK _2orIw _1SeBB"]')
    continue_button.click()

    play_game()

    try:
        continue_button = driver.wait_for_element(By.XPATH, f'//button[{green_continue}]')
        continue_button.click()
    except:
        pass