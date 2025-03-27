from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()

