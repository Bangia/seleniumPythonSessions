# Locators in Python with Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\\Users\\Nitin Bangia\\Documents\\chromedriver_win32\\chromedriver.exe")

driver = webdriver.Chrome(service=ser_obj)

#driver.get("http://demo.nopcommerce.com/")

#For TagName and ClassName
#driver.get("http://automationpractice.com/index.php")

#For CSS selectors
driver.get("https://www.facebook.com/")


driver.maximize_window()

#Locators

#id & #name


#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo IdeaCentre 600 All-in-One PC")
#driver.find_element(By.NAME, "q").send_keys("Lenovo IdeaCentre 600 All-in-One PC")


#Link text & partial link text
#driver.find_element(By.LINK_TEXT, "Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()


#Classname and tag name

# sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")
# print("Total Number of Images :",len(sliders))
#
# #Total Number of Links in web Page - HomePage
#
# homePageAllLinks = driver.find_elements(By.TAG_NAME, "a")
# print("Total Number of Links in web Page - HomePage", (len(homePageAllLinks)))
#
# driver.close()

#For CSS selectors

#Tag with id : tagname#id : example ==> input#email

#driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")

#OR

#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc@gmail.com")

#Tag class : tagname.class : example ==> input.inputtext _55r1 _6luy

#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
#OR
#driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")


#Tag attribute tageName[attributeValue]

#driver.find_element(By.CSS_SELECTOR, "input[data-testid='royal_email']").send_keys("abc@gmail.com")

#tag,class & attribute tageName.class[attributeValue]

#example : input.inputtext[data-testid="royal_pass"]

driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid='royal_pass']").send_keys("abc@gmail.com")


driver.close()