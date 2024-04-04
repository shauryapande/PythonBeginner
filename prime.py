class prime:
    def task():
        n = int(input('Enter a number'))
        count = 0
        for i in range(1,n+1):
            for j in range(1,i):
                if(i % j == 0):
                    count=count + 1
        if (count==2):
            print(n,'is a prime number')
        else:
            print(n,'is not a prime number')
obj=prime
obj.task()