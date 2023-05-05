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

    return render_template("index.html", 
                            tide_dir = tide_dir,
                            wave_height = wave_height,
                            tide_height = tide_height,
                            wind_speed = wind_speed)


if __name__ == "__main__":
    app.run(debug = True)
