import sys
input=sys.stdin.readline
N=int(input())
lst=[]
a,b,c=list(map(int,input().split(" ")))
lst.append([[a,a],[b,b],[c,c]])
lst.append("rinysis") #IndexError 방지
for i in range(N-1):
    a,b,c=list(map(int,input().split(" ")))
    lst[1]=([[a,a],[b,b],[c,c]])
    lst[1][0][0]+=max(lst[0][0][0],lst[0][1][0])
    lst[1][1][0]+=max(lst[0][0][0],lst[0][1][0],lst[0][2][0])
    lst[1][2][0]+=max(lst[0][1][0],lst[0][2][0])
    lst[1][0][1]+=min(lst[0][0][1],lst[0][1][1])
    lst[1][1][1]+=min(lst[0][0][1],lst[0][1][1],lst[0][2][1])
    lst[1][2][1]+=min(lst[0][1][1],lst[0][2][1])
    lst[0]=(lst[1])
    
print(max(lst[0],key=lambda x:x[0])[0],min(lst[0],key=lambda x:x[1])[1])
