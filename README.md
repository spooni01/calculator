# Calculator
Project for course IVS/2022

Team: oznuk_1

The calculator app is an app for solving some basic and slightly difficult mathematical problems. The app provides standard mathematical operations and more.

## Environment

- Ubuntu 64bit
- Windows 64bit

## About

Project was developed in languages: Python.
The project was developed by team **oznuk_1**.

This calculator has root option √ -> in this file marked as ROOT

## Features

- Standard mathematical functions
- More functions as: SIN, COS, ROOT, POWER AND FACTORIAL
- Decimal numbers allowed
- The calculator disposes by history of calculations
- The calculator remembers last answer at its 'Ans' button
- The clear button for cleaning the whole input line
- The calculator proceeds factorial numbers, even if the number before factorial is in closed brackets.
- The calculator is able to proceeds integer and float numbers and operations between them infinitely and catches [OverflowError](https://docs.python.org/3/library/exceptions.html#OverflowError) and [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError).

### All the functions

These functions can be applied on numbers in this calculator

- Addition: `+`
- Substitution: `-`
- Multiplication: `*`
- Division: `/`
- Power: `x^y`
- Sinus: `sin`
- Cosine: `cos`
- Root: `√`
- Factorial: `x!`

## Calculator restrictions

- The calculator rounds results in operations Addition, Substitution, Multiplication, Division, Root and Power to 9 decimal places
- COMMA is used only to divide two expressions in ROOT function

### Function notations for operations

- ADD: `<expression> + <expression>`
- SUB: `<expression> - <expression>`
- MUL: `<expression> * <expression>`
- DIV: `<expression> / <expression>`
- POW: `<expression> ^ <expression>`
- SIN: `SIN ( <expression> )`
- COS: `COS ( <expression> )`
- ROOT: `√NUM` or `√( <expression> , <expression> )`
	+ First one is Root with base 2
	+ Second one is Root with base NUM2
- FACT: `<expression>!`

### Installation

First download the `calculator_1.0_amd64.deb` package.
After downloading the package unpack it by typing `sudo dpkg -i calculator_1.0_amd64.deb`.
Install potential dependencies by running `sudo apt-get -f install`.
Software is now installed under /opt/calculator folder and a helper script `calculator` is installed under /usr/bin, 
so you are now able to run the calculator app by just typing `calculator` from anywhere in the system.
Uninstall the app by running `sudo apt-get remove calculator`.

### License

Licensed under GNU GPL v3  
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

### AUTHORS

Team: oznuk_1
- Adam Dzurilla, xdzuri00<br>
- Adam Ližičiar, xlizic00<br>
- Tomáš Hak, xhakto01<br>
- Jakub Vilček, xvilce00<br>
