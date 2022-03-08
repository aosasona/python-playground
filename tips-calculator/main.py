# Python Tips Calculator - PLAYGROUND PROJECT

import datetime

print("======= Basic Tips Calculator In Python =======")
name = input("What is your name? ")
total = int(input(f"Hello {name}, how much do you intend to spend? "))
currency = input(f"Okay {name}, what is your currency? ")
while int(total) <= 0:
    total = int(input(f"Hello {name}, how much do you intend to spend? "))
tip = int(input("How many percent do you want to tip? "))


def tips(total, percent, currency):
    tip = (percent / 100) * total
    print(f"The tip is {currency}{tip}")


if total > 0:
    tips(total, tip, currency)
else:
    print("Please enter a total amount greater than zero")
