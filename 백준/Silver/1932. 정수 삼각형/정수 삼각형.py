import sys, copy
input=sys.stdin.readline

T=int(input())
lst=[]
for _ in range(T):
    lst.append(list(map(int,input().split(" "))))
lst_copy=copy.deepcopy(lst)

for i in range(T-1):
    for j in range(len(lst[i])):
        if lst_copy[i][j]+lst[i+1][j]>lst_copy[i+1][j]:
            lst_copy[i+1][j]=lst_copy[i][j]+lst[i+1][j]
        if lst_copy[i][j]+lst[i+1][j+1]>lst_copy[i+1][j+1]:
            lst_copy[i+1][j+1]=lst_copy[i][j]+lst[i+1][j+1]

print(max(lst_copy[-1]))