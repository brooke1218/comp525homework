"""
Brooke
02/28/18
hw1
"""

from math import pi 
import random

def circle_area(radius):
    """Calculate the area of a circle with given radius. radius non negative float. returns float"""
    radius = float(input("enter radius"))
    print ("The area of a circle with radius" + str(radius)+ "is" + str(pi * radius**2))

def miles_per_gallon(miles, gallon):
    """calculates miles per gallon: Miles: pos float: gallons: pos float"""
    miles = float(input("enter miles traveled"))
    gallons = float(input("enter gallons"))
    mpg = float("miles per gallon is" + miles/gallons)

def is_even(number):
    if number % 2 == 0:
        print("is even")
    else:
        print("is odd")

def ten_random_numbers(start, stop):
    x = random.randint(0,10)
    y= 7
    while x != y:
        print(x)
        x= random.randint(0,10)

def sum_of_odd_to(n):
    """calculates the sum of all odd numbers from 1 to given n. n: pos integer. returns: integer"""


def average_random_1_to_10(n):
    """Calculates the average of random numbers between 1 and 10 generated n times. n:pos interger -how many times random numbers are generate. returns: integer"""
