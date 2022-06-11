from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

def sleep_for_period_of_time():
    limit = random.randint(60,90)
    time.sleep(limit)

def main():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://www.instagram.com")
    print('stop')

    while(True):
        try:
            list_of_people_who_we_are_following = driver.find_elements(By.XPATH, '//div[@class="_aaes"]//*//*')
            for person in list_of_people_who_we_are_following:
                if person.text == 'Following':
                    person.click()
                    time.sleep(3)
                    try:
                        driver.find_element(By.XPATH, '//*[text()="Unfollow"]').click()
                        print('Unfollowed')
                    except Exception as e:
                        print('could not unfollow')
                    sleep_for_period_of_time()

            driver.execute_script("arguments[0].scrollIntoView(true);", list_of_people_who_we_are_following[-1])

        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()