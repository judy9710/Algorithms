s=list(map(int,input().split()))
e=list(map(int,input().split()))

s_len=len(s)
e_len=len(e)

s.sort()
e.sort()

first=-1
second=-1
answer=0

for i in range(len(s)):
    if first<=s[i]:
        first=e[i]
        answer+=1
    elif second<=s[i]:
        second=first
        first=e[i]
        answer+=1

print(answer)
