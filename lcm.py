class lcm:
    def task():
        a = int(input('Enter a positive number'))
        l=1;
        for i in range(a):
            for j in range(1,a+1):
                if(a%j==0):
                    l=l*j
                    a=a/10
obj = lcm
obj.task()