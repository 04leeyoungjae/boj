N=int(input())

lst=[0,0,0]
for i in range(N):
    lst_copy=lst[::]
    r,g,b=list(map(int,input().split(" ")))
    lst[0]=r+min(lst_copy[1],lst_copy[2])
    lst[1]=g+min(lst_copy[0],lst_copy[2])
    lst[2]=b+min(lst_copy[0],lst_copy[1])
print(min(lst))