"""
Webscrape wave height off Surfline
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# create a ChromeOptions object
chrome_options = webdriver.ChromeOptions()

# set the "detach" option to True
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()),
                          options = chrome_options)
driver.get("https://deepswell.com/surf-report/US/Santa-Barbara/Sands-Beach/1547")


try:
    waveheight = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="RenderBodyContainer"]/div/div/div[1]/div[2]/div/div/div[1]/h1'))
    )
except:
    driver.quit()

height_list = [waveheight.text[0], waveheight.text[2]]
print(height_list)


driver.close()
