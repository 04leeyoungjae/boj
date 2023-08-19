def sol(n):
    d=[i for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,int(i**0.5)+1):
            if d[i]>d[i-j*j]: d[i]=d[i-j*j]+1 
    return d[n]
print(sol(int(input())))