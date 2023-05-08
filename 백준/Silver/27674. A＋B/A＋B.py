for i in range(int(input())):
    input()
    N=list(input())
    N.sort(reverse=True)
    A,B=[],[int(N[-1])]
    for i in range(len(N)-1):
        A.append(int(N[i]))

    total=B[0]

    for i in range(len(A)):
        total+=(A[i])*(10**(len(A)-i-1))

    print(total)