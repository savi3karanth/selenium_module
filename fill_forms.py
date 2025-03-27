from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Savithri", Keys.TAB)
l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("karanth", Keys.TAB)
email = driver.find_element(By.NAME, "email")
email.send_keys("karanth.savi3@gmail.com", Keys.TAB)
submit =driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()