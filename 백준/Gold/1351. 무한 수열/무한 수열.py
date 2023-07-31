def gauss(n):
    return n//1

def infsqn(n):
    if n in d:
        return d[n]
    else:
        d[n]=infsqn(gauss(n/p))+infsqn(gauss(n/q))
        return d[n]

n,p,q=list(map(int,input().split()))
d={}
d[0]=1
print(infsqn(n))