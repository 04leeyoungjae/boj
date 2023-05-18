while "rinysis":
    try:
        s,t=map(list,input().split())
        chk=s.pop(0)
        while True:
            if len(t)==0:
                print("No")
                break
            elif t[0]==chk:
                t.remove(t[0])
                if len(s)==0:
                    print("Yes")
                    break
                else:
                    chk=s.pop(0)
            else:
                t.remove(t[0])
    except:
        break