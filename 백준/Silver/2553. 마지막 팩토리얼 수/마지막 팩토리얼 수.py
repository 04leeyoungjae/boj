n=int(input())
lst=[1]
tmp=1
for i in range(1,n+1):
    tmp*=i
    tmp%=10000000
    while tmp%10==0:
        tmp=int(tmp/10)
print(tmp%10)