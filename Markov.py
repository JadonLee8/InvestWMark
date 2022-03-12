from time import sleep

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


class SimpleStageSet:
    def __init__(self, set_start, set_end, num_days_in_state, stonk, forgiveness, num_states):
        self.set = []
        self.num_days_in_state = num_days_in_state
        self.set_start = set_start
        self.set_end = set_end
        self.stonk = stonk
        self.forgiveness = forgiveness
        self.num_states = num_states

    def create_simple_states(self):
        print("Creating a set of simple states from '" + self.set_start + "' to '" + self.set_end + "'")
        # the below for loop is an incredibly inefficient way to calculate what the date will be for every increment so
        # that you will know when the date has passed the end_date TODO: While writing the below method, there were
        #  definitely some easy ways to optimize, definitely should make an effort to do
        bulk = self.stonk.get_data(self.set_start, self.set_end, "1d", "opens")
        temp_stage = []
        for i in range(0, len(bulk) - 2):
            for y in range(i, i + 3):
                temp_stage.append(bulk[y])
            self.set.append(temp_stage)
            temp_stage = []


# method made obsolete by new method with one large data request
def calculate_date(start_date, days_in_advance):
    year = start_date[0] + start_date[1] + start_date[2] + start_date[3]
    day = start_date[8] + start_date[9]
    month = start_date[5] + start_date[6]
    num_year = int(year)
    num_day = int(day)
    num_month = int(month)
    for i in range(0, days_in_advance-1):
        if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
            if day == "31":
                if month == "12":
                    num_year += 1
                    year = str(year)
                else:
                    num_month += 1
                    if num_month < 10:
                        month = "0" + str(num_month)
                    else:
                        month = str(num_month)
            else:
                num_day += 1
                if num_day < 10:
                    day = "0" + str(num_day)
                else:
                    day = str(num_day)
        elif month == "04" or month == "06" or month == "09" or month == "11":
            if day == "30":
                if month == "12":
                    num_year += 1
                    year = str(year)
                else:
                    num_month += 1
                    if num_month < 10:
                        month = "0" + str(num_month)
                    else:
                        month = str(num_month)
            else:
                num_day += 1
                if num_day < 10:
                    day = "0" + str(num_day)
                else:
                    day = str(num_day)
        else:
            if year == 2024 and year == 2020 and year == 2016 and year == 2012 and year == 2008 and year == 2004 and year == 2000:
                if day == "29":
                    if month == "12":
                        num_year += 1
                        year = str(year)
                    else:
                        num_month += 1
                        if num_month < 10:
                            month = "0" + str(num_month)
                        else:
                            month = str(num_month)
                else:
                    num_day += 1
                    if num_day < 10:
                        day = "0" + str(num_day)
                    else:
                        day = str(num_day)
            else:
                if day == "28":
                    if month == "12":
                        num_year += 1
                        year = str(year)
                    else:
                        num_month += 1
                        if num_month < 10:
                            month = "0" + str(num_month)
                        else:
                            month = str(num_month)
                else:
                    num_day += 1
                    if num_day < 10:
                        day = "0" + str(num_day)
                    else:
                        day = str(num_day)
    return year + "-" + month + "-" + day

