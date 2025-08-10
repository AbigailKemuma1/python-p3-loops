#!/usr/bin/env python3

def happy_new_year():
    y = 10
    while y > 0:
        print (y)
        y -=1
    print ("Happy New Year!")

def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list

    pass

def fizzbuzz():
    for num in range(1, 101):  # 1 to 100 inclusive
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


happy_new_year()
print(square_integers([1, 2, 3, 4, 5]))
