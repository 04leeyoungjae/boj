import sys
input=sys.stdin.readline

lst=[] #각 후보자 득표
for people_num in range(int(input())): #후보자수
    lst.append(int(input()))
cnt=0

while True:
    if len(lst)==1:
        break
    if lst[0]==max(lst):
        copy_lst=list(lst)
        copy_lst.sort(reverse=True)
        if copy_lst[0]==copy_lst[1]:
            cnt+=1
        break
    lst[lst.index(max(lst))]-=1
    lst[0]+=1
    cnt+=1
print(cnt)