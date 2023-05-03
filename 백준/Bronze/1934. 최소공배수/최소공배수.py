for i in range(int(input())):
    A,B=map(int,input().split())
    total=A*B
    if B>A:
        A,B=B,A
    while True:
        tmp=A
        A=B
        B=tmp%B
        if B==0:
            break
    print(total//A)