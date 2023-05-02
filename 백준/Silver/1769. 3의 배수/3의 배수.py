def three(number,cnt):
    cnt+=1
    total=0
    for i in number:
        total+=int(i)
    if total>9:
        return three(str(total),cnt)
    elif int(total)==3 or int(total)==6 or int(total)==9:
        return "YES",cnt
    else:
        return "NO",cnt
    
n=input()
if int(n)>10:
    result,count=three(n,0)
elif int(n)==3 or int(n)==6 or int(n)==9:
    result,count="YES",0
else:
    result,count="NO",0

print(count)
print(result)