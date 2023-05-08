import sys
input=sys.stdin.readline

lst=[0]*200000
error=0
for i in range(int(input())):
    a,b=map(int,input().split())
    if lst[a-1]==b:
        error+=1
    else: #lst[a-1]!=b:
        lst[a-1]=b

lst=[i for i in lst if i not in [0]]
print(error+len(lst))