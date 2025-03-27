from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")


search = driver.find_element(By.NAME, "q")
search.send_keys("Python", Keys.ENTER)
