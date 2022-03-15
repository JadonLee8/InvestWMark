from Markov import SimpleState

from Markov import calculate_date


def tester(stonk, state_set):
    date = input("enter date: ")
    current_state = SimpleState(.03, stonk, date, calculate_date(date, 3), 3, False, None, None)
    for i in state_set.groups:
        if i.fits_in(current_state):
            the_chances = i.future_chances
            print("Prices from " + current_state.state_start + " to " + current_state.state_end + ": " + str(current_state.state))
            print(the_chances)
            for m in state_set.groups:
                if m.group_number in list(the_chances.keys()):
                    print("Average of group " + str(m.group_number) + ": " + str(m.avg_state.state))
            break
