from random import randrange, uniform


def get_random_integer(range):
    return randrange(range)


def get_decimal_number(start, end, round_place=2):
    decimal = uniform(start, end)
    rounded = round(decimal, round_place)
    return rounded