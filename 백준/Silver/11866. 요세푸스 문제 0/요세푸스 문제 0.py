N,K=map(int,input().split())
lst=list(range(1,N+1))
i=0
result=[]
while len(lst)!=0:
    i+=K-1
    while i>=len(lst):
        i-=len(lst)
    result.append(lst.pop(i))
print("<"+", ".join(map(str,result))+">")