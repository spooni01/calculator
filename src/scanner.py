############################################################################
# Project: IVS 2022 - Calculator
# File: scanner.py
# Date: 16.4.2022
# Last modify: 17.4.2022
# Author: Adam Dzurilla xdzuri00@stud.fit.vutbr.cz
#
# Description: Lexical analyser
############################################################################

from utilities import *


## The states for lexical analysis
class State(Enum):
    START = 0
    NUMBER = 1
    DECIMAL = 2
    FLOAT = 3


## List of elements
class Elements:

    ## The constructor
    #  @param self The object pointer
    def __init__(self):
        self.list = []

    ## Adds the element to the list
    #  @param self The object pointer
    #  @param item Item which will be added
    def add(self, item):
        self.list.append(item)

    ## Gets the list with the elements
    #  @param self The object pointer
    def get_list(self):
        return self.list


## Gets next element from expression
#  @param expression String of math problem
#  @return Element class item
def get_next(expression):
    current_state = State.START
    value = ''
    # Scan chars
    while len(expression) != 0:
        char = expression[0]
        expression = expression[1:]
        # According to the state, make operation
        if current_state is State.START:
            if char == ' ':
                continue
            elif char == ')':
                return Element(Type.RBRACKET, 1, ')')
            elif char == '(':
                return Element(Type.LBRACKET, 1, '(')
            elif '0' <= char <= '9':
                value += char
                current_state = State.NUMBER
            elif char == '+' or char == '-' or char == '*' or char == '/' or char == '^':
                return Element(Type.OPERATION, 1, char)
            elif char == 's':
                return Element(Type.SIN, 3, "sin")
            elif char == 'c':
                return Element(Type.COS, 3, "cos")
            elif char == ',':
                return Element(Type.COMMA, 1, ',')
            elif char == '!':
                return Element(Type.FACTORIAL, 1, '!')
            elif char == '√':
                return Element(Type.SQR, 1, '√')
            else:
                raise TypeError('Unknown character')
        elif current_state is State.NUMBER:
            if '0' <= char <= '9':
                value += char
            elif char == '.':
                if len(expression) == 1:
                    raise TypeError('The number can not end with decimal point')
                current_state = State.DECIMAL
                value += char
            else:
                return Element(Type.NUMBER, len(value), value)
        elif current_state is State.DECIMAL:
            if '0' <= char <= '9':
                value += char
                current_state = State.FLOAT
            else:
                raise ValueError('Number expected')
        elif current_state is State.FLOAT:
            if '0' <= char <= '9':
                value += char
            else:
                return Element(Type.NUMBER, len(value), value)

    # Returns a final element
    return Element(Type.EOF, 0, '\0')


## Translates expression into list of elements
#  @param expression String evaluation of expression
#  @return List of elements
def get_elements(expression):
    elements = Elements()

    # Remove whitespaces
    expression = expression.replace(" ", "")+" "
    element = get_next(expression)
    if element is False:
        raise SystemExit("Empty line")
    while element.type is not Type.EOF:
        elements.add(element)
        expression = expression[element.len:]
        element = get_next(expression)

    elements.add(element)

    return elements.get_list()

### End of file scanner.py ###
