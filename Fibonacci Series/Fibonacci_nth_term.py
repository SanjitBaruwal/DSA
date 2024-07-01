def nth_Term(n):
    if(n<=1):
        return n
    else:
        return nth_Term(n-1) + nth_Term(n-2)

print(nth_Term(10))