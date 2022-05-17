############################################################################
# Project: IVS 2022 - Calculator
# File: operations.py
# Date: 27.3.2022
# Last modify: 28.4.2022
# Author: Adam Dzurilla <xdzuri00@stud.fit.vutbr.cz>
#
# Description: In this file are stored operation functions for calculation
############################################################################

## 
# @file operations.py
# 
# @brief In this file are stored operation functions for calculation
# @author Adam Dzurilla <xdzuri00@stud.fit.vutbr.cz>

import math


## Operation Addition
def opp_add(num1, num2):
    return round(num1 + num2, 9)


## Operation Substitution
def opp_sub(num1, num2):
    return round(num1 - num2, 9)


## Operation Multiplication
def opp_mul(num1, num2):
    return round(num1 * num2, 9)


## Operation Division
def opp_div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Numbers can not be divided by 0")
    return round(num1 / num2, 9)


## Operation Power
def opp_pow(num1, num2):
    return round(num1 ** num2, 9)


## Operation Sqrt
def opp_sqrt(num1, num2):
    if num2 == 0:
        raise ValueError("Zero is not accepted!")
    elif (num1 < 0) and (num2 % 2 == 0):
        raise ValueError("Negative numbers are not accepted!")
    elif num1 < 0:
        return -opp_pow(-num1, float(1/num2))
    else:
        return opp_pow(num1, float(1/num2))


## Operation Sinus
def opp_sin(num):
    return round(math.sin(math.radians(num)), 9)


## Operation Cosine
def opp_cos(num):
    return round(math.cos(math.radians(num)), 9)


## Operation Factorial
def opp_factorial(num):
    if num < 0:
        raise ValueError("Negative numbers are not accepted!")
    elif not isinstance(num, int) and not num.is_integer():
        raise TypeError("The value has to be integer!")
    else:
        num = int(num)
        result = 1
        for i in range(1, num + 1):
            result *= i
        return float(result)
