# -*- coding: utf-8 -*-
"""
A simple calculator to solve for the pythagorean theorem
"""
import math

a = str("the a leg")
b = str("the b leg")
c = str("the hypotenuse")

print("What side of the triangle are you missing")
response = input()

if response == a:
    print("what is the length of the b leg?")
    b_1 = float(input())
    print("what is the length of the hypotenuse?")
    hyp_1 = float(input())
    a_1 = hyp_1**2 - b_1**2
    anwr = math.sqrt(a_1)
    print("the value of the a leg is",anwr,".")

if response == b:
    print("what is the length of the a leg?")
    a_2 = float(input())
    print("what is the length of the hypotenuse?")
    hyp_2 = float(input())
    b_2 = hyp_2**2 - a_2**2
    anwr_2 = math.sqrt(b_2)
    print("the value of the b leg is",anwr_2,".")

if response == c:
    print("what is the length of the a leg?")
    a_3 = float(input())
    print("what is the length of the b leg?")
    b_3 = float(input())
    hyp_3 = a_3**2 + b_3**2
    anwr_3 = math.sqrt(hyp_3)
    print("the value of the hypotenuse is",anwr_3,".")
