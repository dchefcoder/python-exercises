"""
Write a fizzBuzz() function with a single integer parameter named upTo. 
For the numbers 1 up to and including upTo, the function prints one of four things:
 Prints 'FizzBuzz' if the number is divisible by 3 and 5.
 Prints 'Fizz' if the number is only divisible by 3.
 Prints 'Buzz' if the number is only divisible by 5.
 Prints the number if the number is neither divisible by 3 nor 5
"""

def fizzBuzz(upTo):
    for i in range(1, upTo + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")