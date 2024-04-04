import math
class quadratic:
    def task():
        a = int(input("Enter the value of a"))
        b = int(input("Enter the value of b"))
        c = int(input("Enter the value of c"))
        discr = math.pow(b,2)-4*a*c
        if (discr < 0):
            print("There are no solutions")
        else:
            solna = (-b + (math.sqrt(discr))) / (2*a)
            solnb = (-b - (math.sqrt(discr))) / (2*a)
            print(solna)
            print(solnb)
obj=quadratic
obj.task()
