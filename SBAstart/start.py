import time
from selenium import webdriver
# ブラウザを開く。
driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe")
driver.implicitly_wait(20) # seconds
# ZPWログイン画面を開く
driver.get('https://dash.zpw.jp/')
# 5秒待ちます
time.sleep(2)
# uuid
login_id = driver.find_element_by_name("mcuuid")
login_id.send_keys("dff946e1-5a0a-46c6-9474-1559fb65ed96")
# pass
login_id = driver.find_element_by_name("pass")
login_id.send_keys("WSDA12wsda")
# click
time.sleep(2)
login_btn = driver.find_element_by_xpath("/html/body/main/section/div/div/div/div[1]/div/div[2]/form/div[4]/button")
login_btn.click()
time.sleep(4)
login_btn = driver.find_element_by_xpath("/html/body/div/a")
login_btn.click()
time.sleep(1)
login_btn = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/div[2]/button")
login_btn.click()
time.sleep(20)
# close
driver.close()