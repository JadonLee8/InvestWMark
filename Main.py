from ChartData import Crypto
import ChartData

bitcoin = Crypto("btc", "Bitcoin", "binance")
print(bitcoin.get_data("2020-01-01", "2020-02-01", "1d"))

ethereum = Crypto("eth", "Ethereum", "binance")
print(ethereum.get_data("2020-01-01", "2020-02-01", "1d"))




