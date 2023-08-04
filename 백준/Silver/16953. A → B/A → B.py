A,B=list(map(int,input().split(" ")))
check=False
cnt=1
while "rinysis":
    if A==B:
        check=True
        break
    elif A>B or B%10==3 or B%10==5 or B%10==7 or B%10==9:
        break
    else:
        cnt+=1
        if B%10==1:
            B=B//10
        else:
            B=B//2
print(cnt if check else -1)