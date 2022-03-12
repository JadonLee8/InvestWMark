import urllib.request
import json


class Crypto:
    def __init__(self, ticker, name, pref_source):
        self.ticker = ticker
        self.name = name
        self.pref_source = pref_source

    # start_date and end_date should be formatted as YYYY-MM-DD
    # interval can be "1m" "5m" "15m" "30m" "1h" "1d" "1w"
    # all params should be strings
    def get_data(self, start_date, end_date, interval):
        print("fetching JSON from messari.io API...")
        url = "https://data.messari.io/api/v1/markets/" + self.pref_source + "-" + self.ticker + "-usdt/metrics/price/time-series?start=" + start_date + "&end=" + end_date + "&interval=" + interval + "&format=json"
        json_file = urllib.request.urlopen(url).read()
        # json_file = json_file[1:]
        print("JSON fetched for " + self.name)
        values = psiphon("values", json_file)
        return values


def psiphon(keyword, file):
    file_dict = json.loads(file)
    data = file_dict["data"]
    return data[keyword]
