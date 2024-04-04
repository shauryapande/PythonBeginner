import math
class libfunction:
    def task():
        x = int(input("Enter a number"))
        print("The square root is ",math.sqrt(x))
        print("The cube root is ",math.cbrt(x))
        print("The factorial is ",math.factorial(x))
obj=libfunction
obj.task()