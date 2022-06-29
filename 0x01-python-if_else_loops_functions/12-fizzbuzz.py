#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 15 == 0:
            print("FizzBuzz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{} ".format(number), end="")