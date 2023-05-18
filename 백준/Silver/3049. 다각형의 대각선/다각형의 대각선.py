def factorial(n):
    return 1 if n==0 else n*factorial(n-1)

def combination(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

a=int(input())
print(0 if a<=3 else combination(a,4))