############################################################################
# Project: IVS 2022 - Calculator
# File: utilities.py
# Date: 16.4.2022
# Last modify: 17.4.2022
# Author: Adam Dzurilla xdzuri00@stud.fit.vutbr.cz
#
# Description: Utilities for calculation.py file
############################################################################

##
# @file utilities.py
#
# @brief Utilities for calculation.py file
# @author Adam Dzurilla <xdzuri00@stud.fit.vutbr.cz>

from enum import Enum


## Element in the math problem expression
class Element:

    ## The constructor
    #  @param self The object pointer
    def __init__(self, element_type, length, value):
        self.type = element_type
        if element_type is Type.NUMBER:
            self.value = float(value)
        else:
            self.value = value
        self.len = length

    ## Get value from the element
    #  @param self The object pointer
    def get_value(self):
        return self.value

    ## Get type from the element
    #  @param self The object pointer
    def get_type(self):
        return self.type


## Enum class of element types
class Type(Enum):
    UNINITIALIZED = 0
    OPERATION = 1
    NUMBER = 2
    LBRACKET = 3
    RBRACKET = 4
    SQR = 5
    SIN = 6
    COS = 7
    COMMA = 8
    FACTORIAL = 9
    EOF = 10

### End of file utilities.py ###
