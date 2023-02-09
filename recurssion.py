def printing(n):
    if n == 1:
        print(1)
        return
    print(n)
    printing(n-1)
    
# printing(10)

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
# print(fact(3))