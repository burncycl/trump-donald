#!/usr/bin/env python3

# 2020/07 BuRnCycL
# Trump Ads cost money. This robot will browse the top two Google Ads in a loop. Thus costing the campaign money.

import os
from time import sleep
from selenium import webdriver
from random import randint, choice


def trump_donald():

    count = 0
    google_search_url = 'https://www.google.com/search?&q=donald+trump+store'
    
    while True:
        count += 1
        print('Count: {}'.format(str(count)))
        
        try:
            # Run a headless Chrome browser with the following options
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--user-agent=' + 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
            browser = webdriver.Chrome('{}/chromedriver'.format(os.path.dirname(os.path.realpath(__file__))), chrome_options=chrome_options) #, service_args=['--verbose', '--log-path=/tmp/chromebrowser.log'])

            class_ids = ['V0MxL', 'sA5rQ'] # First two Ad class IDs on page.
    
            for class_id in class_ids:
                # Browse first Google Ad using V0MxL class identifier. 
                browser.get(google_search_url)
                #browser.save_screenshot('page00.png') # Debugging. Visually verifies we landed on the target page.
                sleep(1)
                print(browser.title)
                browser.find_elements_by_class_name(class_id)[0].click() # List object returned, so target first element found.                    
                sleep(1)
                print(browser.title)
                #browser.save_screenshot('page01.png') # Debugging. Visually verifies we landed on the target page.
                random_sleep()
                
                # Browse sub-page to simulate being a real person.
                link_list = browser.find_elements_by_tag_name("a")
                sub_page = choice(link_list)                
                try:
                    sub_page.click()
                except Exception as e:
                    print(e)        
                sleep(1)
                print(browser.title)        
                #browser.save_screenshot('page02.png') # Debugging. Visually verifies we landed on the target page.
                random_sleep()                 
            
            browser.quit() # Quit browser to nuke the session.
            
        except Exception as e:
            print(e)
            browser.quit()
            continue


def random_sleep():    
    # Wait random interval to simulate human browsing.            
    wait_interval_max = 15
    wait_interval_min = 5          
    wait_time = randint(wait_interval_min, wait_interval_max)
    print('Simulating Human - Waiting: {}s'.format(wait_time))
    sleep(wait_time)


trump_donald()

