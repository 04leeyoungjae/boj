for _ in range(int(input())):
    open,close,cnt=0,0,0
    for i in input():
        if i=="(":
            open+=1
        elif i==")":
            close+=1
        if close>open:
            cnt+=1
    if open!=close:
        cnt+=1
    if cnt!=0:
            print("NO")
    else:
            print("YES")