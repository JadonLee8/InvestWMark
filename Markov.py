from ChartData import Crypto


class SimpleState:
    # state_start is inclusive while state_end is exclusive
    # I included the num days variable bc its just too much work calculating it lol
    def __init__(self, percent_leeway, stonk, state_start, state_end, num_days):
        self.percent_leeway = percent_leeway
        self.stonk = stonk
        self.state_start = state_start
        self.state_end = state_end
        temp_state = stonk.get_data(state_start, state_end, "1d", "opens")
        self.state = []
        for i in range(0, num_days):
            self.state.append(temp_state[i])








