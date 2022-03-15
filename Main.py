from ChartData import Crypto
import ChartData
from Markov import SimpleState
from Markov import SimpleStageSet
from Tester import tester

# currently this file is pretty much just for testing as I create methods for stuff.
bitcoin = Crypto("btc", "Bitcoin", "binance")
# test_state = SimpleState(10, bitcoin, "2020-01-01", "2020-01-04", 3, False)
# print(test_state.state)
#
# test_state_2 = SimpleState(10, bitcoin, "2020-01-01", "2020-01-04", 3, False)
# print(test_state_2.is_similar(test_state, .05))
#
# test_state_3 = SimpleState(10, bitcoin, "2020-01-01", "2020-01-05", 4, False)
# print(test_state_3.is_similar(test_state, .05))
#
# test_state_4 = SimpleState(10, bitcoin, "2019-09-27", "2019-09-30", 3, False)
# test_state_5 = SimpleState(10, bitcoin, "2020-01-12", "2020-01-15", 3, False)
# print(test_state_4.is_similar(test_state_5, .02))
print("enter the date range to gather data on")
print("Ranges larger than 2 years tend to cause HTTP Error 504: Gateway Time-out")
print("When prompted, enter all dates in the format: YYYY-MM-DD")
stage_set_test = SimpleStageSet(input("Enter start date"), input("Enter end date"), 3, bitcoin, .03, 1111)

# for i in stage_set_test.set:
#     print(i.state)
stage_set_test.group_simple_states()
# for i in stage_set_test.groups:
#     print("Group: " + str(stage_set_test.groups.index(i)))
#     print(i.avg_state.state)
#     print("Contents: ")
#     for y in i.contents:
#         print(y.state)
stage_set_test.calc_group_futures()  # it ... worked?
# for i in stage_set_test.set:
#     print(i.state)
#     print("-")
#     print(i.future)
# for i in stage_set_test.groups:
#     print(i.future_possibilities)
stage_set_test.calc_group_future_chances()
# for i in stage_set_test.groups:
#     print(i.future_chances)
# for i in stage_set_test.set:
#     print(i.future)
tester(bitcoin, stage_set_test)


# print(bitcoin.get_data("2020-01-01", "2020-02-01", "1d", "opens"))

# ethereum = Crypto("eth", "Ethereum", "binance")
# print(ethereum.get_data("2020-01-01", "2020-02-01", "1d", "opens"))
#
# binance = Crypto("bnb", "Binance Blockchain Coin", "binance")
# print(binance.get_data("2020-01-01", "2020-02-01", "1d", "opens"))
#
# Terra = Crypto("luna", "Terra", "binance")
# print(Terra.get_data("2020-01-01", "2020-02-01", "1d", "opens"))  # none
#
# xrp = Crypto("xrp", "xrp", "binance")
# print(xrp.get_data("2020-01-01", "2020-02-01", "1d", "opens"))
#
# cardano = Crypto("ada", "Cardano", "binance")
# print(cardano.get_data("2020-01-01", "2020-02-01", "1d", "opens"))
#
# solana = Crypto("sol", "Solana", "binance")
# print(solana.get_data("2020-01-01", "2020-02-01", "1d", "opens"))  # either doesn't have data available for selected dates or
# # API doesn't have same with Terra and avalanche
#
# avalanche = Crypto("avax", "Avalanche", "binance")
# print(avalanche.get_data("2020-01-01", "2020-02-01", "1d", "opens"))  # none
#
# dogecoin = Crypto("doge", "DogeCoin", "binance")
# print(dogecoin.get_data("2020-01-01", "2020-02-01", "1d", "opens"))
#
# monero = Crypto("xmr", "Monero", "binance")
# print(monero.get_data("2020-01-01", "2020-02-01", "1d", "opens"))
