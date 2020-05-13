from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep


options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

chrome_web_driver_path = "C:\\Users\\ssbajk\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_web_driver_path, options=options)

post_url = input('Post URL: ')
driver.get(post_url)

email_elem = driver.find_element_by_xpath('.//*[@id="email"]')
pw_elem = driver.find_element_by_xpath('.//*[@id="pass"]')
account = input('Login: ')
email_elem.send_keys(account)
password = input('Password: ')
pw_elem.send_keys(password)

login_btn = driver.find_element_by_xpath('.//*[@id="loginbutton"]')
sleep(1)
login_btn.click()

comment = "Teste"
for i in range(1000):
    comment_elem = driver.find_element_by_class_name('notranslate')
    comment_elem.send_keys(comment)
    comment_elem.send_keys(Keys.ENTER)
