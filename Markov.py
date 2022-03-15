

class SimpleState:
    # state_start is inclusive while state_end is exclusive
    # I included the num days variable bc its just too much work calculating it lol
    state_ID = 0

    def __init__(self, percent_leeway, stonk, state_start, state_end, num_days, pre_created, data, location_in_bulk):
        if not pre_created:
            self.state_start = state_start
            self.state_end = state_end
            self.state = stonk.get_data(state_start, state_end, "1d", "opens")
            self.num_days = num_days
        else:
            self.state = data
            self.num_days = num_days
            self.location_in_bulk = location_in_bulk
        self.num_days = num_days
        self.percent_leeway = percent_leeway
        self.stonk = stonk
        self.is_in_group = False
        self.state_start = state_start
        self.state_end = state_end
        self.future = []
        self.group = 0
        SimpleState.state_ID += 1
        self.set_ID = SimpleState.state_ID

    # forgiveness should be 0<x<1
    # intended to return True or False based on weather or not all of the values of one state fall within the minimum
    # and maximum (determined by forgiveness) values of another state.
    def is_similar(self, other, forgiveness):
        print('comparing states ' + str(self.state) + " and " + str(other.state))
        if other.num_days == self.num_days:
            for i in range(0, self.num_days - 1):
                max_range = self.state[i] + (self.state[i] * forgiveness)
                min_range = self.state[i] - (self.state[i] * forgiveness)
                if other.state[i] > max_range or other.state[i] < min_range:
                    print('Not similar, states have differing values beyond forgiveness.')
                    return False
            print("SAME!")
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
        self.create_simple_states()
        self.groups = []
        self.bulk = self.stonk.get_data(self.set_start, self.set_end, "1d", "opens")

    def create_simple_states_arr(self):
        print("Creating a set of simple states from '" + self.set_start + "' to '" + self.set_end + "'")
        bulk = self.stonk.get_data(self.set_start, self.set_end, "1d", "opens")
        temp_stage = []
        for i in range(0, len(bulk) - 2):
            for y in range(i, i + 3):
                temp_stage.append(bulk[y])
            self.set.append(temp_stage)
            temp_stage = []

    def create_simple_states(self):
        print("Creating a set of simple states from '" + self.set_start + "' to '" + self.set_end + "'")
        temp_stage = []
        self.bulk = self.stonk.get_data(self.set_start, self.set_end, "1d", "opens")
        for i in range(0, len(self.bulk) - 5):
            for y in range(i, i + self.num_days_in_state):
                temp_stage.append(self.bulk[y])
            self.set.append(SimpleState(.03, self.stonk, calculate_date(self.set_start, i), calculate_date(self.set_start, i + 3),
                                        self.num_days_in_state, True, temp_stage, i))
            temp_stage = []

    # precondition: set has been created using create_simple_states
    def group_simple_states(self):
        for i in self.set:
            if not i.is_in_group:
                self.groups.append(Group(i))
                i.is_in_group = True
                for y in range(self.set.index(i) + 1, len(self.set) - 1):
                    if self.groups[-1].fits_in(self.set[y]):
                        self.groups[-1].add_set(self.set[y])
                        self.set[y].is_in_group = True

    # precondition: group_simple_states has been called and all simple states have been grouped
    def calc_group_futures(self):
        print("Adding futures to simple states...")  # In the future: add the futures upon construction of simple states
        for i in self.set:
            for n in range(i.location_in_bulk + 3, i.location_in_bulk + 6):
                i.future.append(self.bulk[n])
        print("Futures have been added to all simple states.")
        print("Checking which groups futures belong to.")
        for i in self.groups:
            print("Organizing futures for group " + str(self.groups.index(i)))
            for y in i.contents:
                for n in self.groups:
                    if i is not n:
                        if n.fits_in(SimpleState(.03, y.stonk, y.state_start, y.state_end, y.num_days, True, y.future, y.location_in_bulk)):
                            i.add_future(n)
                            break

    def calc_group_future_chances(self):
        for z in self.groups:
            z.calc_future_chances()


class Group:
    current_group_number = 0

    def __init__(self, first_state):
        Group.current_group_number += 1
        self.group_number = Group.current_group_number
        self.contents = []
        self.contents.append(first_state)
        self.avg_state = SimpleState(.03, first_state.stonk, first_state.state_start, first_state.state_end, first_state.num_days, True, first_state.state, first_state.location_in_bulk)
        self.future_possibilities = {}
        self.future_chances = {}

    def add_set(self, simple_state):
        self.contents.append(simple_state)
        self.__avg()

    # a private method
    def __avg(self):
        for i in range(0, len(self.avg_state.state) - 1):
            temp = 0
            for y in self.contents:
                temp += y.state[i]
            self.avg_state.state[i] = temp / len(self.contents)

    def fits_in(self, state):
        if self.avg_state.is_similar(state, .05):
            return True
        else:
            return False

    def add_future(self, group):
        if group.group_number in self.future_possibilities:
            self.future_possibilities[group.group_number] += 1
        else:
            self.future_possibilities.update({group.group_number: 1})

    def calc_future_chances(self):
        total = sum(self.future_possibilities.values())
        keys = list(self.future_possibilities.keys())
        for i in range(0, len(self.future_possibilities) - 1):
            self.future_chances.update({keys[i]: (self.future_possibilities[keys[i]]/total)})


# method made obsolete by new method with one large data request
def calculate_date(start_date, days_in_advance):
    year = start_date[0] + start_date[1] + start_date[2] + start_date[3]
    day = start_date[8] + start_date[9]
    month = start_date[5] + start_date[6]
    num_year = int(year)
    num_day = int(day)
    num_month = int(month)
    for i in range(0, days_in_advance-1):
        if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month \
                == "12":
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
            if year == 2024 and year == 2020 and year == 2016 and year == 2012 and year == 2008 and year == 2004 and \
                    year == 2000:
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
