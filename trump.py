#!/usr/bin/env python3

# 2020/07 BuRnCycL
# Trump Ads cost money. This robot will browse the top two Google Ads in a loop. Thus costing the campaign money.

import os
from time import sleep
from selenium import webdriver
from random import randint



def trump_donald():
    wait_interval_max = 10
    wait_interval_min = 2    
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
    
            # Browse first Google Ad using V0MxL class identifier. 
            browser.get(google_search_url)
            sleep(1)
            print(browser.title)
            browser.find_elements_by_class_name('V0MxL')[0].click() # List object returned, so target first element found.                    
            sleep(1)
            print(browser.title)
            #browser.save_screenshot('site1.png') # Debugging. Visually verifies we landed on the target page.
            sleep(1)

            # Wait before browsing the second Ad at random interval.            
            wait_time = randint(wait_interval_min, wait_interval_max)
            print('Waiting: {}s'.format(wait_time))
            sleep(wait_time)
     
            # Browse second Google Ad using sA5rQ class identifier.
            browser.get(google_search_url)
            sleep(1)
            print(browser.title)
            browser.find_elements_by_class_name('sA5rQ')[0].click() # List object returned, so target first element found.        
            sleep(1)
            print(browser.title)
            #browser.save_screenshot('site1.png') # Debugging. Visually verifies we landed on the target page.
            sleep(1)
    
            # Wait a random interval before continuing to the next loop.
            wait_time = randint(wait_interval_min, wait_interval_max)
            print('Waiting: {}s'.format(wait_time))
            sleep(wait_time)
            
        except Exception as e:
            print(e)
            browser.quit()
            continue


trump_donald()

