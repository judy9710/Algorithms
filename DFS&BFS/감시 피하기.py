n=int(input())
data=[] #학생과 선생이 복도에 나와있는 정보
teachers=[]
spaces=[]

for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j]=='T':
            teachers.append((i,j))
        if data[i][j]=='X':
            spaces.append((i,j))

# 조합을 dfs 방법으로도 구현(연구소 문제)이 가능하지만, 아닌 경우로 풀어보겠음

from itertools import combinations

def watch(x,y,direction): #학생이 있으면 True 없으면 False
    if direction==0:
        while y>=0:
            if data[x][y]=='S':
                return True
            if data[x][y]=='O':
                return False
            y-=1

    if direction==1:
        while y<n:
            if data[x][y]=='S':
                return True
            if data[x][y]=='O':
                return False
            y+=1
            
    if direction==2:
        while x>=0:
            if data[x][y]=='S':
                return True
            if data[x][y]=='O':
                return False
            x-=1
            
    if direction==3:
        while x<n:
            if data[x][y]=='S':
                return True
            if data[x][y]=='O':
                return False
            x+=1
            
# 장애물이 설치된 이후에 한명이라도 학생이 감지되는지 검사

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True #학생 한명이라도 감시되면 True 리턴
    return False #모든 선생이 학생 감지 못하면 False 리턴

find=False

for datas in combinations(spaces,3):
    for x,y in datas:
        data[x][y]='O'
    if not process():
        find=True
        break

    for x,y in datas:
        data[x][y]='X' #설치된 장애물 다시 없애기

if find:
    print('YES')
else:
    print('NO')
            
