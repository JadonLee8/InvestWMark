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
        self.num_days = num_days
        for i in range(0, self.num_days):
            self.state.append(temp_state[i])

    # forgiveness should be 0<x<1
    # intended to return True or False based on weather or not all of the values of one state fall within the minimum
    # and maximum (determined by forgiveness) values of another state.
    def is_similar(self, other, forgiveness):
        print('comparing states ' + str(self.state) + " and " + str(other.state))
        if other.num_days == self.num_days:
            for i in range(0, self.num_days):
                max_range = self.state[i] + (self.state[i] * forgiveness)
                min_range = self.state[i] - (self.state[i] * forgiveness)
                if other.state[i] > max_range or other.state[i] < min_range:
                    print('Not similar, states have differing values beyond forgiveness.')
                    return False
            return True
        else:
            print("Not similar, states have different amounts of days.")
            return False






