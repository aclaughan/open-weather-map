import logging
from urllib.parse import urlencode
from secrets import WEATHER_KEY
import requests as requests

logging.basicConfig(level=logging.INFO, filename="app.log")


def main():
    endpoint = "https://api.openweathermap.org/data/2.5/onecall"

    params = \
        {
            "lon": 18.4232,
            "lat": -33.9258,
            "appid": WEATHER_KEY,
            "units": "metric",
            "exclude": "hourly,daily,minutely"
        }

    # convert the 'English' string to HTML
    url_params = urlencode(params)

    url = f"{endpoint}?{url_params}"

    logging.info(url)

    response = requests.get(url)

    wdata = response.json()

    print(f"Current temperature: {wdata['current']['temp']}c")


if __name__ == '__main__':
    main()

# logging.debug(stuff)
