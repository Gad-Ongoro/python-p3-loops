#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    my_int = 10
    while my_int > 0:
        print(my_int)
        my_int -= 1
    print("Happy New Year!")
    #pass
#happy_new_year()

def square_integers(int_list):
    # code goes here!
    return [item * item for item in int_list]
    #pass

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if ((i % 3 == 0) and (i % 5 == 0)):
            print("FizzBuzz")
        elif (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        else:
            print(i)
        #print(i)
    #pass
fizzbuzz()