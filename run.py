from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
from initialize import initialize
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import uniform

def start(driver, link='https://play.typeracer.com/'):

    print('----Joining random game')

    try:
        if link == 'https://play.typeracer.com/':
        
            driver.get(link)

            sleep(2)
            
            accept_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button[2]')

            accept_button.click()

            while True:
                if 'Enter a typing race' in driver.page_source:
                    break

            element = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, Keys.ALT, 'I')

        else:

            driver.get(link)

            sleep(2)

            accept_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button[2]')

            accept_button.click()

            sleep(3)

            element = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL, Keys.ALT, 'K')


        print('-----Went in a game')

        sleep(2)

        text = ""

        source = driver.page_source
        soup = BeautifulSoup(source,'html.parser')
        table = soup.find('table',{'class':'inputPanel'})
        next_table = table.find('table')
        div = next_table.find('div')
        spans = div.find_all('span')
        for span in spans:
            text = text + span.text
        
        print(f'----Text is: "{text}"')
        
        WebDriverWait(driver,2000).until(EC.element_to_be_clickable((By.CLASS_NAME,'txtInput')))

        input_field = driver.find_element_by_class_name('txtInput')

        for letter in text:
            input_field.send_keys(letter)
            sleep(0.106)

    except Exception as e:
        print(e)


if __name__ == '__main__':

    driver = initialize()
    link = input("Give a link if you are with friends: ")
    if link == "":
        start(driver)
    else:
        start(driver,link)
    sleep(2)
    driver.quit()