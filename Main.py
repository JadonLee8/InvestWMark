from ChartData import Crypto
import ChartData

bitcoin = Crypto("btc", "Bitcoin", "binance")
print(bitcoin.get_data("2020-01-01", "2020-02-01", "1d", "opens"))

ethereum = Crypto("eth", "Ethereum", "binance")
print(ethereum.get_data("2020-01-01", "2020-02-01", "1d", "opens"))

binance = Crypto("bnb", "Binance Blockchain Coin", "binance")
print(binance.get_data("2020-01-01", "2020-02-01", "1d", "opens"))

Terra = Crypto("luna", "Terra", "binance")
print(Terra.get_data("2020-01-01", "2020-02-01", "1d", "opens"))  # none

xrp = Crypto("xrp", "xrp", "binance")
print(xrp.get_data("2020-01-01", "2020-02-01", "1d", "opens"))

cardano = Crypto("ada", "Cardano", "binance")
print(cardano.get_data("2020-01-01", "2020-02-01", "1d", "opens"))

solana = Crypto("sol", "Solana", "binance")
print(solana.get_data("2020-01-01", "2020-02-01", "1d", "opens"))  # either doesn't have data available for selected dates or
# API doesn't have same with Terra and avalanche

avalanche = Crypto("avax", "Avalanche", "binance")
print(avalanche.get_data("2020-01-01", "2020-02-01", "1d", "opens"))  # none

dogecoin = Crypto("doge", "DogeCoin", "binance")
print(dogecoin.get_data("2020-01-01", "2020-02-01", "1d", "opens"))

monero = Crypto("xmr", "Monero", "binance")
print(monero.get_data("2020-01-01", "2020-02-01", "1d", "opens"))
