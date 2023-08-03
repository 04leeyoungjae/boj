def gauss(i):
    return i//1

def sol(i):
    if i<=0:
        d[int(i)]=1
        return d[i]
    elif i in d:
        return d[i]
    else:
        d[int(i)]=sol(gauss(i/p)-x)+sol(gauss(i/q)-y)
        return d[i]

d={}
n,p,q,x,y=list(map(int,input().split(" ")))
print(sol(n))