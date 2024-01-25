def solution(s):
    answer = []
    count=0
    zeros=0
    # 재귀적 문제인감
    answer=recursive(s,zeros,count,answer)
    return answer

def recursive(s,zeros,count,answer):
    zero=0
    #if len(s)==1:
    #    return True
    # 1단계를 수행하는 과정임 (모든 0을 제거)
    for digits in s:
        if digits=='0':
            zero+=1
    zeros+=zero
    s='1'*(len(s)-zero)
    #print(s)
    # 2단계를 수행하는 과정임 (c를 2진법으로 표현한 문자열로 바꿈)
    c=len(s)
    if c==1:
        #print(count+1)
        #print(zeros)
        answer.append(count+1)
        answer.append(zeros)
        return answer
    stack=[]
    while c!=1:
        stack.append(str(c%2))
        c=c//2
    stack.append(str(c))
    stack.reverse()
    new_string=''.join(stack)
    #print(new_string)
    count+=1
    #print('-------')
    recursive(new_string,zeros,count,answer)
    return answer
