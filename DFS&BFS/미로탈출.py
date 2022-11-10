n,m=map(int,input().split())

maze=[]

from collections import deque

for i in range(n):
    maze.append(list(map(int,input())))

#방향 4가지 설정하기
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if maze[nx][ny]==0:
                continue
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append([nx,ny])
    return maze[n-1][m-1]

print(bfs(0,0))
                
