class fibonacci:
    def task():
        n=int(input("Enter the number of terms "))
        a=1
        b=0
        for i in range(n+1):
            fib=a+b
            b=a
            a=fib
            print(fib)
obj=fibonacci
obj.task()