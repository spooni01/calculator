############################################################################
# Project: IVS 2022 - Calculator
# File: test_operations.py
# Date: 4.4.2022
# Last modify: 24.4.2022
# Author: Jakub Vilcek <xvilce00@stud.fit.vutbr.cz>
# Author: Adam Dzurilla <xdzuri00@stud.fit.vutbr.cz>
#
# Description: Operations Test
############################################################################

"""
@file test_operations.py

@brief Tests for operations
@author Jakub Vilcek
@author Adam Dzurilla
"""

import unittest
from operations import *

PI = math.pi


class TEST_Factorial(unittest.TestCase):
    """
    @brief Tests for operation: Factorial
    """

    def test_low_numbers(self):
        self.assertEqual(1, opp_factorial(1))
        self.assertEqual(1, opp_factorial(0.00))
        self.assertEqual(1, opp_factorial(-0))
        self.assertEqual(2, opp_factorial(2.0))
        self.assertEqual(24, opp_factorial(4))
        self.assertEqual(120, opp_factorial(5.0))
        self.assertEqual(720, opp_factorial(6))

    def test_big_numbers(self):
        self.assertEqual(3628800, opp_factorial(10))
        self.assertEqual(479001600, opp_factorial(12))
        self.assertEqual(87178291200, opp_factorial(14))
        self.assertEqual(6402373705728000, opp_factorial(18))
        self.assertEqual(2432902008176640000, opp_factorial(20))

    def test_decimal(self):
        with self.assertRaises(TypeError):
            opp_factorial(2.6)
        with self.assertRaises(TypeError):
            opp_factorial(13.5)
        with self.assertRaises(TypeError):
            opp_factorial(3.71)
        with self.assertRaises(TypeError):
            opp_factorial(2.1)
        with self.assertRaises(TypeError):
            opp_factorial(2.01)
        with self.assertRaises(TypeError):
            opp_factorial(6.66)

    def test_negative(self):
        with self.assertRaises(ValueError):
            opp_factorial(-5)
        with self.assertRaises(ValueError):
            opp_factorial(-100)
        with self.assertRaises(ValueError):
            opp_factorial(-14.8)
        with self.assertRaises(ValueError):
            opp_factorial(-1)
        with self.assertRaises(ValueError):
            opp_factorial(-354)
        with self.assertRaises(ValueError):
            opp_factorial(-8)

    def test_no_exist(self):
        with self.assertRaises(ValueError):
            # Negative number
            opp_factorial(-5)
        with self.assertRaises(ValueError):
            # Negative number
            opp_factorial(-100)
        with self.assertRaises(TypeError):
            # The number has to be integer
            opp_factorial(1.5)


class TEST_Add(unittest.TestCase):
    """
    @brief Tests for operation: Addition
    """

    def test_positive(self):
        self.assertEqual(120, opp_add(110, 10))
        self.assertEqual(25, opp_add(10, 15))
        self.assertEqual(60, opp_add(20, 40))
        self.assertEqual(-5, opp_add(0, -5))
        self.assertEqual(581884779, opp_add(125452364, 456432415))
        self.assertAlmostEqual(492.92, opp_add(36.45, 456.47))
        self.assertAlmostEqual(78.2442, opp_add(32.5974, 45.6468))
        self.assertAlmostEqual(1, opp_add(0.5, 0.5))

    def test_negative(self):
        self.assertEqual(100, opp_add(110, -10))
        self.assertEqual(-5, opp_add(10, -15))
        self.assertEqual(-1980, opp_add(-2020, 40))
        self.assertEqual(-581884779, opp_add(-125452364, -456432415))
        self.assertAlmostEqual(0, opp_add(-0.5, 0.5))

    def test_decimal(self):
        self.assertEqual(14.24, opp_add(5.23, 9.01))
        self.assertEqual(-0.29, opp_add(-5, 4.71))
        self.assertEqual(-1.01, opp_add(78.78, -79.79))
        self.assertEqual(7.0000306, opp_add(2.00003, 5.0000006))
        self.assertEqual(1419784.14, opp_add(784569.75, 635214.39))


class TEST_Sub(unittest.TestCase):
    """
    @brief Tests for operation: Substitution
    """

    def test_positive(self):
        self.assertEqual(120, opp_sub(110, -10))
        self.assertEqual(25, opp_sub(10, -15))
        self.assertEqual(60, opp_sub(20, -40))
        self.assertEqual(581884779, opp_sub(125452364, -456432415))
        self.assertAlmostEqual(381.006, opp_sub(456.47, 75.464))

    def test_negative(self):
        self.assertEqual(100, opp_sub(110, 10))
        self.assertEqual(-5, opp_sub(10, 15))
        self.assertEqual(-2060, opp_sub(-2020, 40))
        self.assertEqual(-581884779, opp_sub(-125452364, 456432415))
        self.assertAlmostEqual(-13.0494, opp_sub(32.5974, 45.6468))

    def test_decimal(self):
        self.assertEqual(-1.75, opp_sub(5.43, 7.18))
        self.assertEqual(-67.99953, opp_sub(10.001, 78.00053))
        self.assertEqual(0, opp_sub(1.1, 1.1))
        self.assertEqual(0.1446, opp_sub(0.223, 0.0784))
        self.assertEqual(6.6767, opp_sub(0.1446, -6.5321))


class TEST_Mul(unittest.TestCase):
    """
    @brief Tests for operation: Multiplication
    """

    def test_positive(self):
        self.assertEqual(100, opp_mul(10, 10))
        self.assertEqual(8, opp_mul(2, 4))
        self.assertEqual(72, opp_mul(8, 9))
        self.assertEqual(469560, opp_mul(645, 728))

    def test_negative(self):
        self.assertEqual(-100, opp_mul(-10, 10))
        self.assertEqual(-5, opp_mul(-5, 1))
        self.assertEqual(50, opp_mul(-10, -5))
        self.assertEqual(-469560, opp_mul(-645, 728))

    def test_decimal(self):
        self.assertEqual(10.7793, opp_mul(5.31, 2.03))
        self.assertEqual(6.957, opp_mul(0.773, 9))
        self.assertEqual(23.0874, opp_mul(7.17, 3.22))
        self.assertEqual(-6.068192, opp_mul(-1.006, 6.03200))
        self.assertEqual(7638.05, opp_mul(78.5, 97.3))

    def test_zero(self):
        self.assertEqual(0, opp_mul(150, 0))
        self.assertEqual(0, opp_mul(0, 0))
        self.assertEqual(0, opp_mul(0, 3.18))
        self.assertEqual(0, opp_mul(0, -0))
        self.assertEqual(0, opp_mul(0, 7846))
        self.assertEqual(0, opp_mul(2.016461, 0))


class TEST_Div(unittest.TestCase):
    """
    @brief Tests for operation: Division
    """

    def test_positive(self):
        self.assertEqual(10, opp_div(100, 10))
        self.assertEqual(2, opp_div(4, 2))
        self.assertEqual(8, opp_div(72, 9))
        self.assertEqual(645, opp_div(469560, 728))

    def test_negative(self):
        self.assertEqual(-1, opp_div(-10, 10))
        self.assertEqual(-50, opp_div(-500, 10))
        self.assertEqual(2, opp_div(-10, -5))
        self.assertEqual(-645, opp_div(469560, -728))

    def test_no_exist(self):
        with self.assertRaises(ZeroDivisionError):
            opp_div(100, 0)

    def test_zero(self):
        self.assertEqual(0, opp_div(0, 48654))


class TEST_Pow(unittest.TestCase):
    """
    @brief Tests for operation: Power
    """

    def test_positive(self):
        self.assertEqual(125, opp_pow(5, 3))
        self.assertEqual(1296, opp_pow(6, 4))
        self.assertEqual(15625, opp_pow(5, 6))
        self.assertEqual(6561, opp_pow(9, 4))
        self.assertEqual(0, opp_pow(0, 4))

    def test_zero_pow(self):
        self.assertEqual(1, opp_pow(5, 0))
        self.assertEqual(1, opp_pow(45412, 0))
        self.assertEqual(1, opp_pow(-10, 0))
        self.assertEqual(1, opp_pow(469560, 0))

    def test_negative(self):
        self.assertEqual(0.008, opp_pow(5, -3))
        self.assertEqual(0.000000001, opp_pow(10, -9))
        self.assertEqual(-125, opp_pow(-5, 3))
        self.assertEqual(1296, opp_pow(-6, 4))


class TEST_Sqrt(unittest.TestCase):
    """
    @brief Tests for operation: Root
    """

    def test_positive(self):
        self.assertAlmostEqual(1, opp_sqrt(1, 4))
        self.assertAlmostEqual(5, opp_sqrt(5, 1))
        self.assertAlmostEqual(4, opp_sqrt(16, 2))
        self.assertAlmostEqual(5, opp_sqrt(125, 3))
        self.assertAlmostEqual(6, opp_sqrt(1296, 4))
        self.assertAlmostEqual(5, opp_sqrt(15625, 6))
        self.assertAlmostEqual(9, opp_sqrt(6561, 4))
        self.assertAlmostEqual(0, opp_sqrt(0, 4))

    def test_zero_pow(self):
        self.assertAlmostEqual(0, opp_sqrt(0, 4))

    def test_negative(self):
        self.assertAlmostEqual(125, opp_sqrt(5, 1 / 3))
        self.assertAlmostEqual(1000000000, opp_sqrt(10, 1 / 9))


class TEST_Sin(unittest.TestCase):
    """
    @brief Tests for operation: Sinus
    """

    def test_positive(self):
        self.assertEqual(opp_sin(90), 1)
        self.assertEqual(opp_sin(60), opp_sin(120))
        self.assertEqual(opp_sin(30), 0.5)
        self.assertEqual(opp_sin(45), opp_sqrt(2, 2) / 2)

    def test_negative(self):
        self.assertEqual(opp_sin(270), -1)
        self.assertEqual(opp_sin(30), -opp_sin(330))

    def test_zero(self):
        self.assertEqual(opp_sin(0), 0)
        self.assertEqual(opp_sin(180), 0)
        self.assertEqual(opp_sin(360), 0)


class TEST_Cos(unittest.TestCase):
    """
    @brief Tests for operation: Cosine
    """

    def test_positive(self):
        self.assertAlmostEqual(opp_cos(0), 1)
        self.assertAlmostEqual(opp_cos(180), -1)
        self.assertAlmostEqual(opp_cos(0), opp_cos(360))
        self.assertAlmostEqual(opp_cos(30), opp_sqrt(3, 2) / 2)
        self.assertAlmostEqual(opp_cos(45), opp_sqrt(2, 2) / 2)

    def test_negative(self):
        self.assertAlmostEqual(opp_cos(540), -1)
        self.assertAlmostEqual(opp_cos(135), -opp_sqrt(2, 2) / 2)
        self.assertAlmostEqual(opp_cos(14), -opp_cos(180-14))

    def test_zero(self):
        self.assertAlmostEqual(opp_cos(90), 0)
        self.assertAlmostEqual(opp_cos(270), 0)
        self.assertAlmostEqual(opp_cos(90 * 45), 0)


unittest.main()
