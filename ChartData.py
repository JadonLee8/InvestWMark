import urllib.request
import json


class Crypto:
    def __init__(self, ticker, name, pref_source):
        self.ticker = ticker
        self.name = name
        self.pref_source = pref_source

    def get_data(self):
        url = "https://data.messari.io/api/v1/markets/" + self.pref_source + "-" + self.ticker + "-usdt/metrics/price" \
                                                                                                 "/time-series?start" \
                                                                                                 "=2020-01-01&end" \
                                                                                                 "=2020-02-01" \
                                                                                                 "&interval=1d&format" \
                                                                                                 "=json "
        json_file = urllib.request.urlopen(url).read()
        # json_file = json_file[1:]
        print(json_file)
        values = psiphon("values", json_file)
        print(values)

    @staticmethod
    def test():
        print("Methods are working!")


def psiphon(keyword, file):
    file_dict = json.loads(file)
    data = file_dict["data"]
    return data[keyword]

# bellow is a waste of time, since the JSON module can already turn a json file into a dictionary :|
# def psiphon(keyword, file, arr):
#     in_word = True
#     value = ""
#     return_var = ""
#     for i in file:
#         if file[i] == '"':
#             if in_word:
#                 i += 1
#                 for y in range(i, len(file)):
#                     if file[y] == '"':
#                         in_word = False
#                         i += 1
#                         break
#                     value += y
#                     i += 1
#                 if value == keyword:
#                     for y in range(i+1, len(file)):
#                         if file[y] == '}' or file[y] == '"':
#                             break
#                         else:
#                             return_var += file[y]
#                             i += i
#             else:
#                 in_word = True
#
#     if arr:
#         return_var =



