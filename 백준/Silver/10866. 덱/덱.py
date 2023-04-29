import sys
d=[]
for i in range(int(input())):
    com=list(sys.stdin.readline().split())
    if com[0]=="push_front":
        d.insert(0,com[1])
    if com[0]=="push_back":
        d.append(com[1])
    elif com[0]=="pop_front":
        if len(d)>=1:
            print(d.pop(0))
        else:
            print(-1)
    elif com[0]=="pop_back":
        if len(d)>=1:
            print(d.pop(-1))
        else:
            print(-1)
    elif com[0]=="size":
        print(len(d))
    elif com[0]=="empty":
        if len(d)>=1:
            print(0)
        else:
            print(1)
    elif com[0]=="front":
        if len(d)>=1:
            print(d[0])
        else:
            print(-1)
    elif com[0]=="back":
        if len(d)>=1:
            print(d[-1])
        else:
            print(-1)