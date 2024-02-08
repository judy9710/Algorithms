# 잘한점: 최단거리의 문제임을 보자마자 bfs를 사용해야함을 떠올랐다
def solution(maps):
    answer = 0
    #방향 4가지 설정하기
    answer=bfs(0,0,maps)
    if answer==1:
        answer=-1
    return answer
    
from collections import deque

def bfs(x,y,maps):
    queue=deque()
    queue.append((x,y))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(maps)
    m=len(maps[0])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if maps[nx][ny]==0:
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                queue.append([nx,ny])
    return maps[n-1][m-1]
