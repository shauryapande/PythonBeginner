class Factor:
    @staticmethod
    def task():
        x: int = int(input("Enter a number "))
        for i in range(x + 1):
            if i > 0 and x % i == 0:
                print(i)


Factor.task()
