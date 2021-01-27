# 문자열을 가장 짧게 압축한 후의 길이 구하기

def solution(s):
    answer=len(s)
    for step in range(1,(len(s)//2)+1):
        final_string=""
        prev=s[0:step]
        count=1
        for j in range(step,len(s),step):
            if prev==s[j:j+step]:
                count+=1
            else:
                final_string+=str(count)+prev if count>=2 else prev
                prev=s[j:j+step]
                count=1
        final_string+=str(count)+prev if count>=2 else prev
        answer=min(answer,len(final_string))
    return answer

s=input()
print(solution(s))
