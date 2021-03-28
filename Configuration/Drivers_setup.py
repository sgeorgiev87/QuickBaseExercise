# this file is for initializing a driver in each test,
# giving opportunities for different environments, browsers, etc.

from selenium import webdriver
from random import randint
import re
import traceback


chromedriver_path = 'C:/drivers/chromedriver.exe'
geckodriver_path = 'C:/drivers/geckodriver.exe'


def driver_init(browser='Chrome'):
    driver = None

    if browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=chromedriver_path)
    elif browser == 'Firefox':
        driver = webdriver.Firefox(executable_path=geckodriver_path)
    else:
        raise Exception('#### Please provide valid browser - Chrome or Firefox!')

    return driver


def handle_exception(driver,
                     custom_exception='',
                     raise_exception=True,
                     screenshot_name='Error_' + str(randint(1,1000)).zfill(4) + '.png'):

    screenshot_pattern = "\w+.(jpg|JPG|png|PNG)$"

    exception = traceback.format_exc()

    if screenshot_name != '':
        scr_path = "./" + screenshot_name
        match = re.match(pattern=screenshot_pattern, string=screenshot_name)
        if match is None:
            raise Exception("Please specify a valid screenshot name --> ABC_Z_abc_z_012_9.(jpg|JPG|png|PNG)")
        try:
            driver.save_screenshot(scr_path)
            print("Screenshot taken: " + screenshot_name)
        except:
            print(screenshot_name + " could not be generated")

    full_exception = custom_exception + '\n' + exception

    if raise_exception:
        raise Exception(full_exception)
    else:
        print(full_exception)