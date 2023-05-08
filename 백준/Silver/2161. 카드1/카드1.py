def cal(lst):
    lst.append(lst.pop(1))
    return lst.pop(0)

d=list(range(1,int(input())+1))
result=[]
while len(d)>=2:
    result.append(cal(d))

print(*result,*d)