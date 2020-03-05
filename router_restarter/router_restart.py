# A basic script to restart my 'Huawei HG255s' router.

from selenium import webdriver
import time

driver = webdriver.Firefox()
url = 'http://192.168.1.1/'
driver.get(url)
log = []
log.append(input('Please enter your username: '))
log.append(input('Please enter your password: '))

login_id = driver.find_element_by_xpath(
    '//*[@id="index_username"]')
login_id.clear()
login_id.send_keys(log[0])
login_password = driver.find_element_by_xpath(
    '//*[@id="password"]').send_keys(log[1])

login = driver.find_element_by_xpath('//*[@id="loginbtn"]').click()
time.sleep(1)
maintenance = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[6]/div/div').click()
time.sleep(1)
tools = driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div[1]/ul/li[3]/a/font').click()
time.sleep(1)
restart = driver.find_element_by_xpath('//*[@id="i18n-9"]').click()
time.sleep(1)
confirm = driver.find_element_by_xpath(
    '//*[@id="dev_mngt_modal_id_ok"]').click()
time.sleep(1)
driver.quit()
