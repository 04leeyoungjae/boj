def sol(n):
    if n in d:
        return d[n]
    else:
        d[n]=[sol(n-1)[0]+sol(n-2)[0],sol(n-1)[1]+sol(n-2)[1]]
        return d[n]


for i in range(int(input())):
    d={0:[1,0], 1:[0,1]}
    n=int(input())
    sol(n)
    print(d[n][0],d[n][1])