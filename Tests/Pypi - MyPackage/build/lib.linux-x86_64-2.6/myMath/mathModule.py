
import os
import sys
import printModule

def add(x, y):
    """Sum stuff

    Keyword arguments:
    x -- First number to sum.
    y -- Second number to sum.

    Returns:
    summ -- The sum of x and y.
    """
    summ = x + y
    printModule.zomgPrint("Inside function - "+str(summ))
    return summ


