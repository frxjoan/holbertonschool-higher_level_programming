#!/usr/bin/python3
def print_last_digit(number):
    ld = abs(number)
    print(ld % 10, end="")
    return ld % 10
