import sys
input=sys.stdin.readline
no_hear=[]
no_see=[]
hear,see=map(int,input().split())
for i in range(hear):
    no_hear.append(input())
for j in range(see):
    no_see.append(input())

no_hear=set(no_hear)
no_see=set(no_see)
no_hear_see=list((set.intersection(no_hear,no_see)))
no_hear_see.sort()
print(len(no_hear_see))
for _ in no_hear_see:
    print(_,end="")