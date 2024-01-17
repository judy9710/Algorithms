answer=''
def recursive(n):
    global answer
    if n==1:
        answer=answer+str(1)
        return
    elif n==2:
        answer=answer+str(2)
        return
    elif n==3:
        answer=answer+str(4)
        return
    else:
        if n%3==1:
            answer=answer+str(1)
            recursive(n//3)
        elif n%3==2:
            answer=answer+str(2)
            recursive(n//3)
        elif n%3==0:
            answer=answer+str(4)
            recursive((n//3)-1)
    return answer
def solution(n):
    global answer
    #아무래도 재귀적인 문제인 것 같다
    #그리고 dp적인 문제이지 않을까 --> 근데 5000만 만큼 할수 없으니 아닐듯하다
    if n==1:
        answer=str(1)
    elif n==2:
        answer=str(2)
    elif (n==3):
        answer=str(4)
    else:
        answer=recursive(n)
    result=""
    for i in range(len(answer)):
        result=result+answer[len(answer)-1-i]
    return result
