from pyvirtualdisplay import Display
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get('http://ids.hhu.edu.cn/amserver/UI/Login?goto=http://form.hhu.edu.cn/pdc/form/list')
browser.find_element_by_id("IDToken1").send_keys("学号")
browser.find_element_by_id("IDToken2").send_keys("密码")
time.sleep(1)
browser.find_element_by_id("IDToken2").send_keys(Keys.ENTER)

time.sleep(2)
print(browser.title)

#browser.find_elements_by_class_name("datav-ren-arrow").click()
#browser.find_element_by_xpath("//div[@class='datav-ren-arrow'][0]").click()
browser.find_element_by_xpath("/html/body/div[1]/div[4]/div/section/section/div/a/div[3]/span").click()
time.sleep(2)
print(browser.title)
time.sleep(2)
browser.find_element_by_id("saveBtn").click()

browser.close()
display.stop()

