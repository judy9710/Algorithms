def solution(s):
    answer = True
    stack=[]
    stack.append(s[0])
    for i in range(1,len(s)):
        if len(stack)==0 and s[i]==')':
            return False
        if s[i]=='(':
            stack.append(s[i])
        else:
            stack.pop()
    if len(stack)!=0:
        return False
    else:
        return True
