
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_Wave_Height(driver):
    try:
        waveheight = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="RenderBodyContainer"]/div/div/div[1]/div[2]/div/div/div[1]/h1'))
        )
    except:
        print("Couldn't get wave height successfully.")

    height_val = [waveheight.text[0], waveheight.text[2]] #Value of the height of the waves at the specific break

    return height_val   

def get_Tide_Height(driver):
    try:
        tide = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="swellTableID"]/table/tbody/tr[1]/td[2]'))
        )
    except:
        print("Couldn't get tide successfully.")
    
    tide_val = tide.text[0] #Value of the incoming or outgoing tide (in feet)
    return tide_val

def get_Tide_Direction(driver):
    try:
        tide_dir = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="swellTableID"]/table/tbody/tr[1]/td[2]/span'))
        )
    except:
        print("Couldn't get tide direction successfully.")
    tide_dir_gliph = tide_dir.get_attribute("outerHTML")
    return tide_dir_gliph

def get_Wind_Speed(driver):
    try:
        wind_speed = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="swellTableID"]/table/tbody/tr[6]/td[2]'))
        )
    except:
        print("Couldn't get wind speed successfully.")
    wind_speed_val = wind_speed.text
    #Extracing the Direction of the wind
    wind_direction = wind_speed_val.split("(")[-1].strip(")")
    #Extracting the speed of the wind
    for i in wind_speed_val:
        if i.isdigit() == True:
            wind_speed_val = i
    return wind_speed_val, wind_direction
    
