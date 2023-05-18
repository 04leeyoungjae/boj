def power(a,b):
    if b==1:
        return a%C
    else:
        temp=power(a,b//2)
        return temp*temp%C if b%2==0 else temp*temp*a%C

A,B,C=map(int, input().split())
result=power(A,B)
print(result)