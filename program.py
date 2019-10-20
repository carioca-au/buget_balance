"""
Rodrigo de Azevedo Carvalho
"""
# We've made the balance history readonly for the auto marking.
BALANCE_HISTORY = [107, 201, 201, 225, 216]


def inc_or_dec(days_ago):
    # Test if the input is an integer
    try:
        days_ago = int(days_ago)
    except ValueError:
        print('Value informed must be a valid number of days')
        quit()

    # Test for zero and negative input
    if days_ago < 1:
        print('Input invalid, input value must be positive and bigger than 0.')
        quit()

    # Force the amount of days to be the same length of the dataset
    elif len(BALANCE_HISTORY) < days_ago:
        days_ago = len(BALANCE_HISTORY)

    # Set the start index
    start = len(BALANCE_HISTORY) - days_ago
    # set the end of the range, avoiding errors
    stop = len(BALANCE_HISTORY) - 1
    for day in range(start, stop):
        balance_slice = BALANCE_HISTORY[day: day + 2]
        difference = balance_slice[1] - balance_slice[0]
        if difference > 0:
            print(f'Balance from {days_ago} days ago INCREASED!')
        elif difference < 0:
            print(f'Balance from {days_ago} days ago DECREASED!')
        elif difference == 0:
            print(f'Balance from {days_ago} stayed THE SAME!!')
        days_ago -= 1


d = input('How many days of data? ')
inc_or_dec(d)
