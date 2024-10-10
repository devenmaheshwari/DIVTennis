# Scrape "https://tennisinsight.com/injuries/" for 500 entries using Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()

driver.get("https://tennisinsight.com/injuries/")

time.sleep(2)

length = driver.find_element(By.ID, "injuriesTable_length")
# find sibling with class = "select"

select = length.find_element(By.CLASS_NAME, "select")

select.click()

time.sleep(2)

# find the option for "All"

all = driver.find_element(By.XPATH, "//option[@value='-1']")

all.click() # click on "All"

time.sleep(2)

# print table at div = "injuriesTable_wrapper"

table = driver.find_element(By.ID, "injuriesTable_wrapper")

# convert table to database 

# Injury Date in webpage - Date Column in DB
# Player in Webpage - Player Column in DB
# Injury Description Column in Webage - Tournament Column in DB
# Number 1 - Injury Column in DB

print(table.text)

driver.quit()


