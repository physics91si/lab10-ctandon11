#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    while True:
        try:
            a= int(input("Please enter a number a: "))
            b=int(input("Please enter a number b: "))
            c= int(input("Please enter a number c: "))
            2/a
            break
        except ValueError:
            print("Oops!  That was no valid number. Try again...")
        except ZeroDivisionError:
            print("Oops!  Make sure a is not zero. Try again...")
    x1, x2 = find_roots(int(a), int(b), int(c))
    print ("This is x1:", x1)
    print ("This is x2:", x2)


def find_roots(a,b,c):
    mid = b**2 - (4*a*c)
    sqrt_mid = mid**(1/2)
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2

if __name__=="__main__":
    main()