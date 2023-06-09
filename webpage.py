import webscrape_main

from flask import Flask
from flask import render_template

app = Flask(__name__)

#Home Page
@app.route("/")
def home():
    wave_height = webscrape_main.wave_height
    tide_height = webscrape_main.tide_height
    tide_dir = webscrape_main.tide_direction
    wind_speed = webscrape_main.wind_speed
    weather = webscrape_main.weather
    water_temp = webscrape_main.water_temp
    period = webscrape_main.period

    return render_template("index.html", 
                            tide_dir = tide_dir,
                            wave_height = wave_height,
                            tide_height = tide_height,
                            wind_speed = wind_speed,
                            weather = weather,
                            water_temp = water_temp,
                            period = period)


if __name__ == "__main__":
    app.run(debug = True)
