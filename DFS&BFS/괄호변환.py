def check(p):
    check=''
    left=0
    right=0
    for i in p:
        if i=='(':
            left+=1
        elif i==')':
            right+=1
            if left>1:
                left-=1
                right-=1
        if right>left: 
            check='uncorrect'
            break
        else:
            check='correct'
    return check

def balanced_index(p):
    count=0
    for i in range(len(p)):
        if p[i]=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return i

def solution(p):
    answer=''
    if p=='':
        return answer
    index=balanced_index(p)
    u=p[:index+1]
    v=p[index+1:]
    if check(u)=='correct':
        answer=u+solution(v)
    elif check(u)=='uncorrect':
        answer='('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:len(u)-1])
        for i in range(len(u)):
            if u[i]=='(': #문자열형은 대입 연산을 못하므로 list형으로 바꾸고 해야함
                u[i]=')'
            else:
                u[i]='('
        answer+=''.join(u)
    return answer

answer=solution('()))((()')
print(answer)
