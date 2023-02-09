def fib(n):
    if(n<=1):
            return n
    pfib=0
    cfib=1
    for i in range(n-1):
                nfib=pfib+cfib
                pfib=cfib
                cfib=nfib
    return cfib
print(fib(5))