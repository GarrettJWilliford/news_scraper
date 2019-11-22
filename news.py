from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os
from scp import remove_html

def driver_init():
    fop = Options()
    fop.add_argument('--headless')
    fop.add_argument('--window_size1920x1080')
    return webdriver.Firefox(options = fop)




def bbc(driver):
    no_words = ['Share this with', 'Email','Facebook','Messenger','Twitter','Pinterest','WhatsApp',\
                'LinkedIn','Copy this link', 'These are external links and will open in a new window', \
                'Home','About us','Generation Project','Worklife 101','Bright Sparks','More']
    while True:
        os.system('clear')
        driver.get('https://www.bbc.com/') 
        time.sleep(4)
        try:
            links = driver.find_elements_by_class_name('media__link')
        except:
            print('<<!FAILED_TO_FIND_LINKS!>>')
            print('<<!RESTARTING_DRIVER!>>')
            time.sleep(2)
        print('<<<<<<<<<<<<<<<<<<<<NEWS>>>>>>>>>>>>>>>>>>>>')
        for l in links:
            print(str(links.index(l)) + '| ' +  l.get_attribute('innerHTML').strip())
            print('-----------------------------------------------------------------------')
        print('>>| BACK')
        print('-----------------------------------------------------------------------')
        command = input('>>SELECT_STORY>> ')
        print('<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>')
        if command == 'BACK':
            driver.quit()
            return
        if command.isdigit():
            try:
                [story for story in links if int(command) == links.index(story)][0].click()
            except:
                print('<<!STORY_NOT_FOUND!>>')
                continue
            time.sleep(.5)
            p = driver.find_elements_by_tag_name('p')
            for pp in p:
                if '<a href' in pp.get_attribute('innerHTML'):
                    continue
                if pp.get_attribute('innerHTML') in no_words:
                    continue
                pp = remove_html(pp.get_attribute('innerHTML'))
                if pp == False:
                    continue
                else:
                    print(pp)
            command = input('<<|PRESS_ENTER_TO_CONTINUE|>>')      
        else:
            error = input('<<!STORY_NOT_FOUND!>')
            
    driver.quit()

