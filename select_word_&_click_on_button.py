from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_counts = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")
# Extract the second count if it exists
if len(article_counts) > 1:
    second_article_count = article_counts[1].text
    print(f"Second article count (Total Pages Count): {second_article_count}")
else:
    print("Second article count not found.")

article_counts[1].click()

