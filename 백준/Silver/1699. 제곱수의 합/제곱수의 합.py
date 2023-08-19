def sol(n):
    d=[0]*(n+1)
    for i in range(1,n+1):
        d[i]=i
        j=1
        while j*j<=i:
            d[i]=min(d[i],d[i-j*j]+1)
            j+=1
    return d[n]
print(sol(int(input())))