from selenium import webdriver
from datetime import datetime
import info
import time

current_time = datetime.now()
print(current_time)
day_str = str(current_time.date().strftime("%d"))
print(day_str)

browser = webdriver.Chrome("chromedriver.exe")
browser.get('https://moodle.cpce-polyu.edu.hk/')

browser.find_element_by_id('ctl00_ContentPlaceHolder1_UsernameTextBox').send_keys(info.ac)
browser.find_element_by_id('ctl00_ContentPlaceHolder1_PasswordTextBox').send_keys(info.passwd)
browser.find_element_by_id('ctl00_ContentPlaceHolder1_SubmitButton').click()

time.sleep(5)
browser.find_element_by_link_text(day_str).click()

cards = browser.find_elements_by_link_text('Go to activity')

main_win = browser.current_window_handle

lnks = browser.find_elements_by_tag_name("a")

for lnk in cards:
    lnk_str = lnk.get_attribute("href")
    print(lnk_str)
    browser.execute_script("window.open();")
    browser.switch_to.window(browser.window_handles[1])
    browser.get(lnk_str)
    browser.find_element_by_link_text("Submit attendance").click()
    browser.find_element_by_xpath(".//*[contains(text(), 'Present')]").click()
    browser.find_element_by_id('id_submitbutton').click()
    browser.close()

browser.quit()
