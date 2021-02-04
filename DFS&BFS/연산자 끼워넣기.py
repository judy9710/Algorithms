n=int(input())
array=list(map(int,input().split()))
n_add,n_sub,n_mul,n_div=map(int,input().split())

# 경우의 수 최대 9! = 482880 가지 중복이면 더 줄어들지 --> 2초안에 가능
# 모든 경우의 수 따지는게 dfs bfs 문제인가??

all_types=[]
for i in range(n_add):
    all_types.append('+')
for i in range(n_sub):
    all_types.append('-')
for i in range(n_mul):
    all_types.append('*')
for i in range(n_div):
    all_types.append('/')

from itertools import permutations

result=list(permutations(all_types,n-1))
final=[]

from collections import deque

for operators in result:
    q=deque(array)
    answer=q.popleft()
    for i in range(n-1):
        second=q.popleft()
        if operators[i]=='+':
            answer=answer+second
        elif operators[i]=='-':
            answer=answer-second
        elif operators[i]=='*':
            answer=answer*second
        elif operators[i]=='/':
            if answer<=0:
                answer=answer*(-1)
            answer=answer//second
    final.append(answer)
#print(final)
            
print(max(final))
print(min(final))
#print(len(final))
