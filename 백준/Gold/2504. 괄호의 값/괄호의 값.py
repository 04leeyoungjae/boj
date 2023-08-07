def slicing(string,s=[]):
    if string.count("(")!=string.count(")") or string.count("[")!=string.count("]"):
        return "rinysis"
    elif not(string):
        return s
    small,big=[0,0],[0,0]
    open=string[0]
    for i in range(len(string)):
        if string[i]=="(":
            small[0]+=1
        elif string[i]==")":
            small[1]+=1
        elif string[i]=="[":
            big[0]+=1
        else:
            big[1]+=1
        if small[1]>small[0] or big[1]>big[0]:
            return "rinysis" #잘못된 문자열
        if (open=="(" and small[0]==small[1]) or (open=="[" and big[0]==big[1]):
            s.append(string[:i+1])
            return slicing(string[i+1:],s)

def calc(s,f=1,debug=0):
    if s=="rinysis":
        return 0
    global total
    tmp=0
    if s==[]:
        return 1
    for i in range(len(s)):
        p=s[i]
        const=p[0] #p의 첫글자가 ( 이면 2곱하고, [이면 3곱하기
        new_p=slicing(p[1:-1],[])
        if debug:print("현재 p:",p,"부모 s:",s)
        if debug:print("새로운 p:",new_p if new_p else "공집합")

        if const=="(":
            if debug:print("2곱하기시도","토탈에 추가할 값:",2*calc(new_p,0))
            if f:
                total+=2*calc(new_p,0)
            else:
                tmp+=2*calc(new_p,0)
            if debug:print("토탈변동감지",total)

        elif const=="[":
            if debug:print("3곱하기시도","토탈에 추가할 값:",3*calc(new_p,0))
            if f:
                total+=3*calc(new_p,0)
            else:
                tmp+=3*calc(new_p,0)
            if debug:print("토탈변동감지",total)
    return tmp

lst=slicing(input())
global total
total=0
calc(lst)
print(total)