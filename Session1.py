from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# SELENIUM 3 STANDARD

# driver = webdriver.Chrome(executable_path="C:\\Users\\Nitin Bangia\\Documents\\chromedriver_win32\\chromedriver.exe")
# driver.get("https://opensource-demo.orangehrmlive.com/");
# driver.maximize_window()
#
# driver.find_element_by_id("txtUsername").send_keys("Admin")
# driver.find_element_by_name("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
#
# act_Title = driver.title
# print(act_Title)
# expected_title = "OrangeHRM"
#
# if act_Title == expected_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
#
# driver.close()

# SELENIUM 4 UPGRADE VERSION STANDARD
from selenium.webdriver.common.by import By

ser_Obj = Service("C:\\Users\\Nitin Bangia\\Documents\\chromedriver_win32\\chromedriver.exe")

driver = webdriver.Chrome(service=ser_Obj)
driver.get("https://opensource-demo.orangehrmlive.com/");
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.NAME, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

#Assertion
act_Title = driver.title
print(act_Title)
expected_title = "OrangeHRM"

if act_Title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()
