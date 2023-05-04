def fact(number):
    if number==0:
        return 1
    else:
        return number*fact(number-1)
def make_lst(n):
    i=0
    lst=[]
    while True:
        if fact(i)<=n:
            lst.append(fact(i))
            i+=1
        else:
            break
    return lst[::-1]

N=int(input())
lst=make_lst(N)
can="NO"
if N==0:
    pass
else:
    for i in lst:
        if N>=i:
            N-=i
        if N==0:
            can="YES"
            break
        else:
            pass
print(can)