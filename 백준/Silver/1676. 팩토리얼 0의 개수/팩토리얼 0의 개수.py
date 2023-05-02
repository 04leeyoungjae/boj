def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

A=factorial(int(input()))
cnt=0
while True:
    if A%10==0:
        A=A//10
        cnt+=1
    else:
        break
print(cnt)