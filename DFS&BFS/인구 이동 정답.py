from collections import deque

n,l,r=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=0

def process(x,y,index):
    # (x,y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united=[]
    united.append((x,y))
    # bfs 사용할거임 (국경을 접하는 나라이므로 인접한것 먼저 탐색하는 bfs가 적합)
    # 큐 자료구조 정의
    q=deque()
    q.append((x,y))
    union[x][y]=index # 현재 연합의 번호를 할당
    summary=graph[x][y] # 현재 연합의 전체 인구 수
    count=1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x,y=q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                # 옆에 있는 나라와 인구 차이가 l명 이상 r명 이하면
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    q.append((nx,ny))
                    # 연합에 추가
                    union[nx][ny]=index
                    summary+=graph[nx][ny]
                    count+=1
                    united.append((nx,ny)) #연합 국가에 추가
    # 연합 국가끼리 인구를 분배
    for i,j in united:
        graph[i][j]=summary//count
    return count

total_count=0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union=[[-1]*n for _ in range(n)]
    index=0
    for i in range(n):
        for j in range(n):
            if union[i][j]==-1: #해당 나라가 아직 처리 전이면
                process(i,j,index)
                index+=1
    # 모든 인구 이동이 끝난 경우
    if index==n*n: # 끝까지 가는걸 보장
        break
    total_count+=1 # 마지막 값을 총 연합 국가의 수라고 한다
# 인구 이동 횟수 출력

print(total_count)
    
