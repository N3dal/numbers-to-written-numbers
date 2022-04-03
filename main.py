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
