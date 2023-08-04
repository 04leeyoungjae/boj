"""
주기 P라 할때
N번째 피보나치 수를 M으로 나눈 나머지는
N%P번째 피보나치 수를 M으로 나눈 나머지와 같음
주기는 M=10^k (k>=2)일때 15*10^(k-1)
"""

m=1000000
p=1500000

def sol(n):
    a,b=0,1
    for _ in range(n):
        a,b=b%m,(a+b)%m #a는 b가되고 b는 a+b가 되는데, 나머지가 반복되므로 %m으로 바로 나눠주어도 무방
    return a

n=int(input())
print(sol(n%p))