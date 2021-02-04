n,k=map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

virus=[]

for i in range(n):
    for j in range(n):
        if array[i][j]!=0:
            virus.append((i,j,array[i][j],0))

s,x,y=map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

virus.sort(key=lambda x: int(x[2])) #바이러스를 작은 번호대로 정렬

from collections import deque

def bfs():
    queue=deque(virus)
    while queue:
        x,y,v,sec=queue.popleft()
        if sec==s:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if array[nx][ny]==0:
                array[nx][ny]=v
                queue.append((nx,ny,v,sec+1))
            if array[nx][ny]!=0:
                continue
    return array

# 시간을 tracking하기 어려운 경우에는 아예 파라미터로 넘겨주는게 좋음

result=bfs()
print(result[x-1][y-1])

# queue가 sorted 되었다는 보장은 작은거부터 했으니까 작은거부터 나오겠지

