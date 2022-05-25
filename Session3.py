from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_Obj = Service("/Users/rst/Desktop/chromedriver")

driver = webdriver.Chrome(service=ser_Obj)

# driver.get("http://automationpractice.com/index.php")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()


#Absolute xpath
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

#Relative xpath

# driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//button[@name='submit_search']").click()

#xpath options

# and
# or
# contains()
# starts-with()
# text()

#Or operator
#driver.find_element(By.XPATH, "//input[@name='txtUsername' or @id='txtUsername']").send_keys("Admin")

# and operator

#driver.find_element(By.XPATH, "//input[@name='txtPassword' and @id='txtPassword']").send_keys("admin123")

# contains() : it will always use key , value pair example : (@id,'value') where id is key

#driver.find_element(By.XPATH, "//input[contains(@id,'txtUse')]").send_keys("Admin")

# starts-with()

#driver.find_element(By.XPATH, "//input[starts-with(@id,'txtPass')]").send_keys("admin123")

# text() : if you want to identify element using inner  text  example a tag you can use text : text()='INNER HTML VALUE'


driver.find_element(By.XPATH, "//a[text()='Forgot your password?']").click()