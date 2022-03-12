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
    def get_data(self, start_date, end_date, interval, value_request):
        print("fetching JSON from messari.io API...")
        url = "https://data.messari.io/api/v1/markets/" + self.pref_source + "-" + self.ticker + "-usdt/metrics/price/time-series?start=" + start_date + "&end=" + end_date + "&interval=" + interval + "&format=json"
        json_file = urllib.request.urlopen(url).read()
        # json_file = json_file[1:]
        print("JSON fetched for " + self.name)
        values = psiphon("values", json_file)
        return_val = []
        if values is not None:
            for i in values:
                temp_day = i
                for y in temp_day:
                    if value_request == "opens" and temp_day.index(y) == 1:
                        return_val.append(y)
                        break
                    elif value_request == "highs" and temp_day.index(y) == 2:
                        return_val.append(y)
                        break
                    elif value_request == "lows" and temp_day.index(y) == 3:
                        return_val.append(y)
                        break
                    elif value_request == "closes" and temp_day.index(y) == 4:
                        return_val.append(y)
                        break
                    elif value_request == "volumes" and temp_day.index(y) == 5:
                        return_val.append(y)
                        break
            return return_val
        else:
            return None


def psiphon(keyword, file):
    file_dict = json.loads(file)
    data = file_dict["data"]
    return data[keyword]
