import sys
from collections import Counter

num_card=int(input())
card_list=list(map(int,input().split()))
check_num=int(input())
check_list=list(map(int,input().split()))

cnt=Counter(card_list)

for i in check_list:
    if i in cnt:
        print(cnt[i], end=" ")
    else:
        print(0,end=" ")