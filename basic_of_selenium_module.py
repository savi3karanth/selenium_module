from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

webdriver = webdriver.Chrome(options=chrome_options)
webdriver.get("https://google.com")

webdriver.close()
webdriver.quit()