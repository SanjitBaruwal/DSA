print(0)
print(1)
count = 2
upto = 10

def Fibonacci(first,second):
    global count,upto
    if(count<=upto):
        next = first+second
        print(next)
        first = second
        second = next
        count+=1
        Fibonacci(first,second)
    else:
        return

Fibonacci(0,1)
