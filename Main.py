from ChartData import Crypto
import ChartData

bitcoin = Crypto("btc", "Bitcoin", "binance")
bitcoin.get_data()

ethereum = Crypto("eth", "Ethereum", "binance")
ethereum.get_data()




