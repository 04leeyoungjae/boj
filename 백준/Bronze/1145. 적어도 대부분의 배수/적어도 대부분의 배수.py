def least_common_mutiple(a,b):
    if a>b:
        big,small=a,b
    else:
        big,small=b,a
    while small!=0:
        tmp=big
        big=small
        small=tmp%small
    return a*b//big

def lcm(a,b,c):
    return(least_common_mutiple(least_common_mutiple(a,b),least_common_mutiple(b,c)))

lst=list(map(int,input().split()))
total=lcm(lst[0],lst[1],lst[2])
for i in range(0,5):
    for j in range(0,5):
        for k in range(0,5):
            if i==j or i==k or j==k:
                pass
            else:
                if total>lcm(lst[i],lst[j],lst[k]):
                    total=lcm(lst[i],lst[j],lst[k])
print(total)