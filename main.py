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

# TODO: make it this script convert from binary/hex/oct to decimal then,
# TODO: write the written number, in simple words convert from (binary/hex/oct) to written num.
# TODO: convert any exp number to written for example "3e10" express on it first then write it.
# TODO: or "3.5E10" same thing.


from os import name as OS_NAME
from os import system


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
    12345 => [VALID]
    123.45 => [VALID]
    '32FD' => [NON-VALID]

    output-type: string.
    """


def main():
    pass


if __name__ == "__main__":
    main()
