result=[]
n=int(input())
coins=list(map(int,input().split()))

from itertools import combinations

for i in range(1,n+1):
    money=list(combinations(coins,i))
    for every in money:
        result.append(sum(every))

result.sort()

i=1

for value in set(result):
    if i==value:
        i+=1
    else:
        print(i)
        break
    
# 이 방법은 파이썬의 itertools 내의 combinations를 사용한 것이다
