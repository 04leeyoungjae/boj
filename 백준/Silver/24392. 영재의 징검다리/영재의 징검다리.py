N,M=list(map(int,input().split(" ")))
lst=[]
lst_copy=[]
for _ in range(N):
    lst.append(list(map(int,input().split(" "))))
    lst_copy.append([0]*M)
lst_copy[0]=lst[0][::]
for i in range(N):
    for j in range(M):
        if lst_copy[i][j]>=1:
            try:
                if lst[i+1][j-1]>=1 and j-1!=-1:
                    lst_copy[i+1][j-1]+=lst_copy[i][j]
            except:
                pass
            try:
                if lst[i+1][j]>=1:
                    lst_copy[i+1][j]+=lst_copy[i][j]
            except:
                pass
            try:
                if lst[i+1][j+1]>=1:
                    lst_copy[i+1][j+1]+=lst_copy[i][j]
            except:
                pass

print(sum(lst_copy[-1])%1000000007)