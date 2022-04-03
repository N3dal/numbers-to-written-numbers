#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script fro convert numbers includes (int, float),
# to written numbers as string.
#
#
#
# Author:N84.
#
# Create Date:Sun Apr  3 15:05:42 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------

# note remember to add dash/hyp between some numbers like:
# 21=> "twenty-one" not "twenty one",
# 771=> "seven hundred and seventy-one" not "seven hundred and seventy-one"

# TODO: make this script convert from binary/hex/oct to decimal then,
# TODO: write the written number, in simple words convert from (binary/hex/oct) to written num.
# TODO: convert any exp number to written for example "3e10" express on it first then write it.
# TODO: or "3.5E10" same thing.
# TODO: make this script able to express any negative number either float or integer, or even string.


from os import name as OS_NAME
from os import system


MAX_LIMIT_NUMBER = 1_000_000 * 1000


def clear():
    """wipe the terminal screen"""

    if OS_NAME == "posix":
        # *nix machines.
        system("clear")

    else:
        # windows machines.
        system("cls")


clear()


def num2written(number: object):
    """convert any float/int/string number to written number.
    input-type: float/int/str.
    valid inputs:
    '12345' => [VALID]
    '12_345' => [VALID]
    12_345 => [VALID]
    '12_345.32' => [VALID]
    12345 => [VALID]
    123.45 => [VALID]
    '32FD' => [NON-VALID]

    output-type: string.
    """

    # Guard conditions.

    if type(number) not in (int, float, str):
        return -1

    if type(number) is str:

        try:
            number = int(number)

        except ValueError:

            try:
                number = float(number)
            except ValueError:
                return -1

    if number > MAX_LIMIT_NUMBER:
        # max number we can convert to it is billion.
        return -1

    # now convert num into string.
    string_num = str(number)

    WRITTEN_NUMBERS = (
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eightteen", "nineteen",
        "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
        "hundred", "thousnad", "million", "billion"
    )

    return number


def main():

    num = num2written("123_142_343")
    print(num)


if __name__ == "__main__":
    main()
