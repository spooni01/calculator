############################################################################
# Project: IVS 2022 - Calculator
# File: calculation.py
# Date: 16.4.2022
# Last modify: 28.4.2022
# Author: Adam Dzurilla xdzuri00@stud.fit.vutbr.cz
#
# Description: Functions for calculate expression
############################################################################

##
# @file calculation.py
#
# @brief: File containing functions to solve math problem
# @author: Adam Dzurilla <xdzuri00@stud.fit.vutbr.cz>

from scanner import *
from operations import *


## Stack of operations and left brackets
class Stack:

    ## The constructor
    #  @param self The object pointer
    def __init__(self):
        self.list = []

    ## Push number to stack
    #  @param self The object pointer
    #  @param item pushs operation or left bracket on the stack
    def push(self, item: str):
        self.list.append(item)

    ## Pop value from stack or raise Index Error if is empty
    #  @param self The object pointer
    def pop(self):
        # Checks if list is not empty
        if self.is_empty():
            raise IndexError
        else:
            return self.list.pop()

    ## Returns value from the stack top
    #  @param self The object pointer
    def top(self):
        if self.list:
            return self.list[-1]

    ## Checks if stack is empty
    #  @param self The object pointer
    def is_empty(self):
        return len(self.list) == 0


## Postfix stack
class Postfix:

    ## The constructor
    #  @param self The object pointer
    def __init__(self):
        self.list = []

    ## Pushs element to postfix stack
    #  @param self The object pointer
    #  @param element The item which will be added
    def push(self, element):
        self.list.append(element)

    ## Pops element from postfix stack or raise Index Error
    #  @param self The object pointer
    def pop(self):
        if not self.list:
            raise IndexError('Pop from empty file')
        return self.list.pop()

    ## Checks, if on the stack is just one number, if yes it returns that number
    #  @param self The object pointer
    #  @return The last number from the stack
    def get_result(self):
        if len(self.list) != 1:
            raise TypeError
        else:
            result = float(self.pop())
            if result.is_integer():
                result = int(result)
            return result

    ## By operation from parameter decides which operation will be proceeded on stack
    #  @param self The object pointer
    #  @param operation Type of the operation
    def do_operation(self, operation):
        if operation == '+':
            self.add()
        elif operation == '-':
            self.sub()
        elif operation == '*':
            self.mul()
        elif operation == '/':
            self.div()
        elif operation == '^':
            self.pow()
        elif operation == '!':
            self.fact()
        else:
            raise TypeError(operation)

    ## Addition
    #  @param self The object pointer
    def add(self):
        """
        @brief:
        """
        num2 = self.pop()
        num1 = self.pop()

        self.push(opp_add(num1, num2))

    ## Substitution
    #  @param self The object pointer
    def sub(self):
        num2 = self.pop()
        num1 = self.pop()

        self.push(opp_sub(num1, num2))

    ## Multiplication
    #  @param self The object pointer
    def mul(self):
        num2 = self.pop()
        num1 = self.pop()

        self.push(opp_mul(num1, num2))

    ## Division
    #  @param self The object pointer
    def div(self):
        num2 = self.pop()
        num1 = self.pop()

        if num2 == 0:
            raise ZeroDivisionError

        self.push(opp_div(num1, num2))

    ## Power
    #  @param self The object pointer
    def pow(self):
        num2 = self.pop()
        num1 = self.pop()

        self.push(opp_pow(num1, num2))

    ## Factorial
    #  @param self The object pointer
    def fact(self):
        num1 = self.pop()
        if num1.is_integer():
            self.push(opp_factorial(int(num1)))
        else:
            raise TypeError("Factorial can't be float")


## Gets next element from the list
#  @param elements List of the elements
#  @param position Position of the current element
#  @param move Number how many elements ite returns after current element
#  @return Element from moved position
def get_next_element(elements, position, move) -> Element:
    if position + move < len(elements):
        return elements[position + move]
    else:
        raise IndexError


## The function creates string formula until element
#  @param elements List of elements
#  @param start_position Start position in list
#  @param until_type Type where the function stops solving
#  @return math problem as string for another calculation
def get_problem_until(elements, start_position, until_type):
    iterate_element = elements[start_position]
    left_brackets = 0
    commas = 0
    skip = 1
    formula = ''
    while iterate_element.type is not until_type or left_brackets > 0 or commas > 0:
        if iterate_element.type is Type.LBRACKET:
            left_brackets += 1
        elif iterate_element.type is Type.RBRACKET:
            left_brackets -= 1
        elif iterate_element.type is Type.SQR:
            if elements[start_position + 1].type is Type.LBRACKET:
                commas += 1
        elif iterate_element.type is Type.COMMA:
            commas -= 1

        formula += str(iterate_element.value)

        skip += 1
        start_position += 1
        iterate_element = elements[start_position]

    # Add number to the end (negation case)
    if iterate_element.type is Type.NUMBER:
        formula += str(iterate_element.value)

    return formula, skip


## Calculates sinus, cosines and roots from the list and replace them with number
#  @param elements List of the elements
#  @return List of the elements without sinus and cosines
def calculate_sin_cos_sqrt(elements):
    new_list = []
    skip = 0
    # Iterates through elements
    for n in range(len(elements)):
        if skip > 0:
            skip -= 1
            continue

        element = elements[n]
        if element.type is Type.SIN or element.type is Type.COS:
            lbracket = get_next_element(elements, n, 1)
            if lbracket.type is not Type.LBRACKET:
                raise TypeError

            formula, skip = get_problem_until(elements, n+2, Type.RBRACKET)
            skip += 1

            if element.type is Type.SIN:
                new_list.append(Element(Type.NUMBER, 0, opp_sin(calculate(formula))))
            else:
                new_list.append(Element(Type.NUMBER, 0, opp_cos(calculate(formula))))
        elif element.type is Type.SQR:
            next_element = get_next_element(elements, n, 1)

            if next_element.type is Type.NUMBER:
                new_list.append(Element(Type.NUMBER, 0, opp_sqrt(next_element.value, 2)))
                skip = 1
            elif next_element.type is Type.LBRACKET:
                num1, skip1 = get_problem_until(elements, n + 2, Type.COMMA)
                num2, skip2 = get_problem_until(elements, n + 2 + skip1, Type.RBRACKET)

                new_list.append(Element(Type.NUMBER, 0, opp_sqrt(calculate(num1), calculate(num2))))
                skip = skip1 + skip2 + 1
            else:
                raise TypeError
        else:
            new_list.append(element)

    return new_list


## Change numbers which had minus before as negations
#  @param elements List of the elements
#  @return List of elements without minus operations which are as negations
def calculate_negative_numbers(elements):
    new_list = []
    skip = 0
    # Iterates through elements
    for n in range(len(elements)):
        if skip > 0:
            skip -= 1
            continue

        element = elements[n]
        if element.type is Type.OPERATION and element.value == '-':
            next_element = get_next_element(elements, n, 1)
            prev_element = None
            if n != 0:
                prev_element = elements[n - 1]
            if n == 0 or prev_element.type is Type.LBRACKET or prev_element.type is Type.OPERATION:
                if next_element.type is Type.OPERATION and next_element.value == '-':
                    formula, skip = get_problem_until(elements, n+1, Type.NUMBER)
                    next_val = calculate(formula) * -1
                    new_list.append(Element(Type.NUMBER, 0, next_val))
                elif next_element.type is Type.NUMBER:
                    next_element.value = next_element.value * -1
                    new_list.append(Element(Type.NUMBER, 0, next_element.value))
                    skip = 1
                elif next_element.type is Type.LBRACKET:
                    formula, skip = get_problem_until(elements, n+2, Type.RBRACKET)
                    next_val = calculate(formula) * -1
                    new_list.append(Element(Type.NUMBER, 0, next_val))
                else:
                    raise TypeError
            else:
                new_list.append(element)
        else:
            new_list.append(element)

    return new_list


## Do operation on stack
#  @param operation Type of the operation
#  @param stack Stack with operations and left brackets
#  @param postfix Postfix stack
def do_operation(operation, stack, postfix):
    priority_top = 0
    priority = 0
    # Sets priority for top element
    if not stack.is_empty():
        top = stack.top()
        if top == '!':
            priority_top = 4
        elif top == '^':
            priority_top = 3
        elif top == '*' or top == '/':
            priority_top = 2
        elif top == '+' or top == '-':
            priority_top = 1

    # Sets priority for operation
    if operation == '!':
        priority = 4
    elif operation == '^':
        priority = 3
    elif operation == '*' or operation == '/':
        priority = 2
    elif operation == '+' or operation == '-':
        priority = 1

    # Makes operation
    if stack.is_empty():
        stack.push(operation)
    else:
        top = stack.top()
        if top == '(' or priority_top < priority:
            stack.push(operation)
        else:
            postfix.do_operation(top)
            stack.pop()
            do_operation(operation, stack, postfix)


## The program pushs operations on postfix stack
#  @param stack Stack with operations
#  @param postfix Postfix stack
def until_left_bracket(stack, postfix):
    while not stack.is_empty() and stack.top() != '(':
        top = stack.top()
        postfix.do_operation(top)
        stack.pop()

    if not stack.is_empty():
        stack.pop()


## Calculates given expression
#  @param expression Expression as string
#  @return Result number
def calculate(expression):
    # Divides expression into tokens
    elements = get_elements(expression)

    # Calculates sinus, cosines and roots as first, then negative numbers
    elements = calculate_sin_cos_sqrt(elements)
    elements = calculate_negative_numbers(elements)

    # Creates stack and postfix stack
    # and calculates expression as infix to postfix method
    stack = Stack()
    postfix = Postfix()
    for element in elements:
        if element.type is Type.NUMBER:
            postfix.push(element.value)
        elif element.type is Type.LBRACKET:
            stack.push('(')
        elif element.type is Type.RBRACKET:
            until_left_bracket(stack, postfix)
        elif element.type is Type.OPERATION:
            do_operation(element.value, stack, postfix)
        elif element.type is Type.FACTORIAL:
            do_operation('!', stack, postfix)
        elif element.type is Type.EOF:
            until_left_bracket(stack, postfix)
        else:
            raise TypeError('Unknown element: ' + str(element.type))

    # Returns result
    return postfix.get_result()

### End of file calculation.py ###
