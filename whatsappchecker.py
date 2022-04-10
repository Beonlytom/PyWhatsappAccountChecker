from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


listnumber = open("list.txt", "r+")

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
with open("existingnumbers.txt", "r+") as a:
       a.truncate()


print("LOGIN IN WHATSAPP WEB, WAIT FOR THE PAGE TO LOAD AND THEN CLICK ENTER IN THE CONSOLE")
input()


for numbers in listnumber:
       print("Checking this number: " + str(numbers) )
       driver.get("https://web.whatsapp.com/send?phone=$"+ str(numbers) + "&text&app_absent=0")
       time.sleep(14)

       if len(driver.find_elements_by_xpath("/html/body/div[1]/div[1]/span[2]/div[1]/span/div[1]/div/div/div")) == 0:
              print("Number Exists\n\n")
              with open("existingnumbers.txt", "a+") as z:
                     z.write(str(numbers))

       if len(driver.find_elements_by_xpath("/html/body/div[1]/div[1]/span[2]/div[1]/span/div[1]/div/div/div")) > 0:
              print("Number Doesn't Exist\n\n")
       






input()
driver.close()



