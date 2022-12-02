import pytz
import requests
from datetime import datetime, timedelta


def get_grapth_data(start_date, days, currency):
    url = "https://api.exchangerate.host/timeseries?base=USD&start_date={}&end_date={}&symbols={}".format(
        start_date - timedelta(days=days),
        start_date,
        currency
    )

    response = requests.get(url)
    data = response.json().get("rates")
    return [data[key].get(currency, "-") for key in data.keys()]


print(get_grapth_data(datetime.now(pytz.timezone("Etc/GMT+1")), 5, "UAH"))
