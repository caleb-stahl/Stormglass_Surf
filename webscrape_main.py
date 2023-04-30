"""
Webscrape wave height off Surfline
"""
import webscrape_def
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# set the "detach" option to True
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options = chrome_options)
driver.get("https://deepswell.com/surf-report/US/Santa-Barbara/Sands-Beach/1547")

print(webscrape_def.get_Wave_Height(driver))
print(webscrape_def.get_Tide_Height(driver))
print(webscrape_def.get_Tide_Direction(driver))
print(webscrape_def.get_Wind_Speed(driver))


driver.quit()
