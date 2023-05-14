"""
Webscrape
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

wave_height = webscrape_def.get_Wave_Height(driver)
tide_height = webscrape_def.get_Tide_Height(driver)
tide_direction = webscrape_def.get_Tide_Direction(driver)
wind_speed = webscrape_def.get_Wind_Speed(driver)
weather = webscrape_def.getWeather(driver)
water_temp = webscrape_def.getWaterTemp(driver)
period = webscrape_def.getPeriod(driver)


# print(wave_height)
# print(tide_height)
# print(type(tide_direction))
# print(wind_speed)


driver.quit()
