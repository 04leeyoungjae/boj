def sol(n):
    if n in d:
        return d[n]
    else:
        d[n]=sol(n-1)+sol(n-2)
        return d[n]

d={0:0, 1:1}
n=int(input())
if n>=900: #파이썬의 기본 재귀횟수 996을 넘어가는 input이 들어오기때문
    for i in range(n//900 + 2):
        sol(900*i)
else:
    sol(n)
print(d[n])