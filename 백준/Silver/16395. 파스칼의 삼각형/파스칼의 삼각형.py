def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def combination(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r)) if n>=r else 0

n,k=list(map(int,input().split(" ")))
print(combination(n-1,k-1))