# 내가 한시간 넘게 생각한 방법의 큰 아이디어는 맞았으나, 구현 과정에서
# 아직 내가 깨닫지 못한 문제가 발생한듯하다

INF=int(1e9)

n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

# 플로이드 워셜 진행한 후에 모든 노드에 대하여 다른 노드와 서로 도달이
# 가능한지를 체크하여 문제를 해결할 수 있다

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

result=0
for i in range(1,n+1):
    count=0
    for j in range(1,n+1):
        if graph[i][j]!=INF or graph[j][i]!=INF: # 두 방향 중 하나라도 길이 있으면 비교가 가능하므로 카운트한다
            count+=1
    if count==n:
        result+=1
print(result) # 성적 순위를 정확히 알 수 있는 학생 수를 출력
