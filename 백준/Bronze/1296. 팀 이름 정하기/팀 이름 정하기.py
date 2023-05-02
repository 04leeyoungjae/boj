def win_percent(y_name,team_name):
    L=y_name.count("L")+team_name.count("L")
    O=y_name.count("O")+team_name.count("O")
    V=y_name.count("V")+team_name.count("V")
    E=y_name.count("E")+team_name.count("E")
    return(((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100)

def who_is_biggest(the_list):
    tied=[]
    big_name=the_list[0]
    biggest=win_percent(y_name_input,the_list[0])
    for i in range(len(the_list)):
        if win_percent(y_name_input,the_list[i])>biggest:
            tied=[] #공동순위 초기화
            big_name=the_list[i]
            tied.append(big_name)
            biggest=win_percent(y_name_input,the_list[i])
        if win_percent(y_name_input,the_list[i])==biggest:
            tied.append(the_list[i])
    tied.sort()
    return(tied[0])


y_name_input=input()
lst=[]
for test_case in range(int(input())): #테스트케이스 입력
    lst.append(input())
print(who_is_biggest(lst))