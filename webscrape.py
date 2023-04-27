"""
Webscrape wave height off Surfline
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# set the "detach" option to True
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options = chrome_options)
driver.get("https://www.surfline.com/surf-report/sands/5842041f4e65fad6a7708964")
print(driver.title)
driver.close()
