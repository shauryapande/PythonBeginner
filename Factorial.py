class Factorial:
    @staticmethod
    def task():
        fac = 1
        x = int(input("Enter a number"))
        for i in range(1, x + 1):
            fac = i * fac
        print(fac)


obj = Factorial
obj.task()
