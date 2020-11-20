# import webdriver 
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path=r"C:\Program Files\geckodriver\geckodriver.exe")
driver.implicitly_wait(40)

# enter keyword to search 
keyword = "outlook"
  
# get geeksforgeeks.org 
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1605691820&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fmail%2f0%2finbox%3fnlp%3d1%26RpsCsrfState%3db7dd0b8d-469b-1cfa-b007-1fcebd162032&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015") 

def entrmail():  
    # get element  
    action = ActionChains(driver)
    driver.find_element_by_name("loginfmt").send_keys("hariharasudhan.vellaichamy@rap.ventures")
    time.sleep(2)
    enteremail = driver.find_element_by_id("idSIButton9")
    action.click(on_element = enteremail)
    action.perform()

def enterpassword():
    time.sleep(10)
    action = ActionChains(driver)
    driver.find_element_by_name("passwd").send_keys("rap@12345")
    signin = driver.find_element_by_xpath("//input[@value='Sign in']")
    action.click(on_element = signin)
    action.perform()
def staysigned_page():
    time.sleep(10)
    action = ActionChains(driver)
    staysign = driver.find_element_by_xpath("//input[@value='Yes']").click()
    action.perform()
def extract():
    action = ActionChains(driver)
    goto_views = driver.find_element_by_xpath("//*[@id='ember1601']/a/span").click()
    click_rrtickets = driver.find_element_by_link_text("Recently solved tickets").click().perform()
    if driver.find_element_by_xpath("//*[@id='table2']"):
        mail_table = driver.find_element_by_xpath("//*[@id='table2']")
        rows = mail_table.find_elements(By.TAG_NAME, "tr")
    getbody(rows)

def getbody(rows):
    action = ActionChains(driver)
    for row in rows:
            action.click(on_element = row)



entrmail()
enterpassword()
staysigned_page()
extract()