n,m=map(int,input().split())
balls=list(map(int,input().split()))
# 조합을 계산하는 라이브러리를 사용하면 편리하다

numbers=[]
from itertools import combinations
for i in range(n):
    numbers.append(i)
    
result=list(combinations(numbers,2))
answer=len(result)

for i in result:
    if balls[i[0]]==balls[i[1]]:
        answer-=1

print(answer)
        
