############################################################################
# Project: IVS 2022 - Calculator
# File: test_calculation.py
# Date: 21.4.2022
# Last modify: 21.4.2022
# Author: Jakub Vilcek <xvilce00@stud.fit.vutbr.cz>
#
# Description: Calculator Test
############################################################################

##
# @file test_calculation.py
#
# @brief Tests for calculation function (from calculation.py)
# @author Jakub Vilcek <xvilce00@stud.fit.vutbr.cz>

import unittest
from calculation import *


class TestExpression(unittest.TestCase):
    """
    @brief Tests for calculate function from calculation.py
    """

    def test_bracket(self):
        self.assertEqual(calculate('((((4))))()'), 4)
        self.assertEqual(calculate('((((4)))'), 4)
        self.assertEqual(calculate('(5*1)+5/(2+(5*1)/2)'), 6.111111111)
        self.assertEqual(calculate('((((5+1)-2)*3)/4)+5'), 8)

    def test_basic(self):
        self.assertEqual(calculate('4*4'), calculate('8*2'), calculate('16*1'))
        self.assertEqual(calculate('5 + 4 * 2 - 10'), 3)
        self.assertEqual(calculate('1+1'), 2)
        self.assertEqual(calculate('18-9'), 9)
        self.assertEqual(calculate('2*6'), 12)
        self.assertEqual(calculate('48/2'), 24)
        self.assertEqual(calculate('15+15'), 30)
        self.assertEqual(calculate('8-2'), 6)
        self.assertEqual(calculate('0+0+0'), 0)

    def test_minus(self):
        self.assertEqual(calculate('-2 -2 -2 -2 -2'), -10)
        self.assertEqual(calculate('-2 + 18  - 25 + 4 - 2'), -7)
        self.assertEqual(calculate('0-5'), -5)
        self.assertEqual(calculate('-1-2-3-4'), -10)
        self.assertEqual(calculate('-10-10'), -20)

    def test_mul_first(self):
        self.assertEqual(calculate('4 + 5 * 8'), 44)
        self.assertEqual(calculate('100/10 * (2 + 3)'), 50)
        self.assertEqual(calculate('2+5*2'), 12)
        self.assertEqual(calculate('15-2*3'), 9)
        self.assertEqual(calculate('10+(2*3+1)'), 17)

    def test_pow(self):
        self.assertEqual(calculate('2^5'), 32)
        self.assertEqual(calculate('5^6'), 15625)
        self.assertEqual(calculate('5^1'), 5)
        self.assertEqual(calculate('6^3'), 216)
        self.assertEqual(calculate('5^0'), 1)
        self.assertEqual(calculate('5^(6)'), 15625)

    def test_dec_pow(self):
        self.assertEqual(calculate('2^(-2)'), 0.25)
        self.assertEqual(calculate('6^0.5'), 2.449489743)
        self.assertEqual(calculate('10^-3'), 0.001)
        self.assertEqual(calculate('10^-1'), 0.1)
        self.assertEqual(calculate('54^-3'), calculate('1/157464'))

    def test_root(self):
        self.assertEqual(calculate('√4'), 2)
        self.assertEqual(calculate('√(8, 3)'), 2)
        self.assertEqual(calculate('√(-8, 3)'), -2)
        with self.assertRaises(TypeError):
            calculate('3√4')

    def test_dec_root(self):
        self.assertAlmostEqual(calculate('√2'), 1.414213562)
        self.assertAlmostEqual(calculate('√2+2'), 3.414213562)
        self.assertAlmostEqual(calculate('√2 / √2'), 1)
        self.assertAlmostEqual(calculate('√0.25'), 0.5)

    def test_nested_root(self):
        self.assertEqual(calculate('√(4*4,2)'), 4)
        self.assertEqual(calculate('√(80+1,2)'), 9)
        self.assertEqual(calculate('2*√(30-9/3,1+1+1) + 8'), 14)
        self.assertEqual(calculate('√((sin(90)*4*√64*(4--4)),(50-48+1*2)) + 8'), 12)

    def test_fact(self):
        self.assertEqual(calculate('5!'), 120)
        self.assertEqual(calculate('0!'), 1)
        self.assertEqual(calculate('1!'), 1)
        self.assertEqual(calculate('sin(90)!'), 1)
        self.assertEqual(calculate('cos(90)!'), 1)
        self.assertEqual(calculate('5!-3!'), 114)
        with self.assertRaises(ValueError):
            calculate('(-1)!')
        with self.assertRaises(ValueError):
            calculate('-1!')
        self.assertEqual(calculate('17!'), 355687428096000)
        self.assertEqual(calculate('17!/16!'), 17)
        with self.assertRaises(TypeError):
            calculate('1.2!')

    def test_nested_factorial(self):
        self.assertEqual(calculate('(10-5)!'), 120)
        self.assertEqual(calculate('(45-24*2+6)!'), 6)
        self.assertEqual(calculate('3!!'), 720)
        self.assertEqual(calculate('((5!-4!)/48)!'), 2)
        self.assertEqual(calculate('(3!-2!)!'), 24)
        self.assertEqual(calculate('(3!!/360*4)!'), 40320)
        self.assertEqual(calculate('(1+1+1+1+1+1)!'), 720)
        self.assertEqual(calculate('(18/3+2!+0!)!'), 362880)

    def test_div(self):
        self.assertEqual(calculate('10/2'), 5)
        self.assertEqual(calculate('-10/-2'), 5)
        self.assertEqual(calculate('10/-2'), -5)
        self.assertEqual(calculate('0/-2'), 0)
        with self.assertRaises(ZeroDivisionError):
            calculate('10/0')
        with self.assertRaises(ZeroDivisionError):
            calculate('10/(2-2)')
        with self.assertRaises(ZeroDivisionError):
            calculate('0/0')

    def test_dec_div(self):
        self.assertAlmostEqual(calculate('10/3'), 3.333333333)
        self.assertAlmostEqual(calculate('10/100'), 0.1)
        self.assertAlmostEqual(calculate('75/26'), 2.884615385)

    def test_sin(self):
        self.assertEqual(calculate('sin(90)'), 1)
        self.assertEqual(calculate('sin(0)'), 0)
        self.assertEqual(calculate('sin(0) + 5 '), 5)
        self.assertAlmostEqual(calculate('sin(30)'), 0.5)
        self.assertAlmostEqual(calculate('sin(60)'), calculate('√3/2'))
        self.assertAlmostEqual(calculate('sin(69)'), calculate('sin(69+360*214)'))
        self.assertAlmostEqual(calculate('sin(30)'), -calculate('sin(-30)'))

    def test_nested_sin(self):
        self.assertEqual(calculate('sin(5+4+40-4)'), calculate('cos(0+45+1-2+1)'))
        self.assertEqual(calculate('sin(sin(90)*90)'), 1)
        self.assertEqual(calculate('sin(60*sin(15+15))*5'), 2.5)
        with self.assertRaises(IndexError):
            calculate('sin(sin(90')
        with self.assertRaises(TypeError):
            calculate('sin(90))sin(90)')

    def test_cos(self):
        self.assertEqual(calculate('cos(0)'), 1)
        self.assertEqual(calculate('cos(90)'), 0)
        self.assertEqual(calculate('cos(180)'), -1)
        self.assertEqual(calculate('cos(60)'), 0.5)
        self.assertEqual(calculate('98+cos(45)'), calculate('(196+√2)/2'))
        self.assertEqual(calculate('cos(60)'), -calculate('cos(120)'))
        self.assertEqual(calculate('cos(69)'), calculate('cos(69+360*341)'))

    def test_nested_cos(self):
        self.assertEqual(calculate('cos(40+40+10)'), 0)
        self.assertEqual(calculate('cos(cos(0)*60)'), 0.5)
        with self.assertRaises(IndexError):
            calculate('cos(cos(90')
        with self.assertRaises(IndexError):
            calculate('cos(cos(90)')

    def test_complex(self):
        self.assertEqual(calculate('(56+36)^2 - √81*√81'), 8383)
        with self.assertRaises(OverflowError):
            calculate('2050^250-2050^249')

    def test_negations(self):
        self.assertEqual(calculate('-5'), -5)
        self.assertEqual(calculate('-sin(30)'), -0.5)
        self.assertEqual(calculate('-√81'), -9)
        self.assertEqual(calculate('√(4--5, 2)'), 3)
        self.assertEqual(calculate('---5'), -5)
        self.assertEqual(calculate('--5'), 5)
        self.assertEqual(calculate('-5 + -5 - -10'), 0)
        self.assertEqual(calculate('-(15*2)'), -30)


class TestErrors(unittest.TestCase):

    def test_syntax_error(self):
        with self.assertRaises(TypeError):
            calculate('5.')
        with self.assertRaises(TypeError):
            calculate('3,')
        with self.assertRaises(TypeError):
            calculate('5,2 * 5')
        with self.assertRaises(TypeError):
            calculate('cos52')
        with self.assertRaises(TypeError):
            calculate('√4, 3')


if __name__ == '__main__':
    unittest.main()
