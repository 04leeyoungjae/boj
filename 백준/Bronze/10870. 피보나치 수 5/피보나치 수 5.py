def sol(n):
    if n in d:
        return d[n]
    else:
        d[n]=sol(n-1)+sol(n-2)
        return d[n]

d={0:0, 1:1}
n=int(input())
if n>=900: #다른 문제 코드 재활용
    for i in range(n//900 + 2):
        sol(900*i)
else:
    sol(n)
print(d[n])