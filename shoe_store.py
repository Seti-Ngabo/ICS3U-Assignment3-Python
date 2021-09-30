#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program tells you how much you have to pay for the shoe boxes
#   with user input

import constants


def main():
    # this function calculates the math

    # input
    amount_as_string = input(
        "How many boxes of shoe would you like to buy ($150 per box): "
    )
    print("")

    # process and output
    try:
        amount_as_number = int(amount_as_string)
        sub_total = amount_as_number * constants.COST
        total = sub_total + (sub_total * constants.HST)
        if total > constants.MAX_COST:
            discount = total / constants.PERCENTAGE_DISCOUNT
            total = total - discount
            print("The total is ${0} (including tax plus 10% off.)".format(total))
        else:
            print("The total is ${0} (including tax).".format(total))
            print("")

    except Exception:
        print("{0} is an invalid input, try again.".format(amount_as_string))
        print("")
    finally:
        print("Thanks for checking.")
    print("\nDone.")


if __name__ == "__main__":
    main()
