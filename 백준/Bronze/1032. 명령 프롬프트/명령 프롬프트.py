words=[]
for test_case in range(int(input())):
    words.append(input())
for i in range(len(words[0])): #단어의 길이만큼 반복
    cnt=True
    for j in range(len(words)-1): #단어의 개수만큼 반복
        if words[j][i]==words[j+1][i]:
            pass
        else:
            cnt=False #하나라도 다른지 확인
    if cnt==True:
        print(words[0][i],end="") #모두 같으면 그대로 출력
    else:
        print("?",end="")