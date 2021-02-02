INF=int(1e9)

n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

maximum=0
maximum_count=0

for b in range(1,n+1):
    maximum=max(maximum,graph[1][b])

for b in range(1,n+1):
    if graph[1][b]==maximum:
        maximum_count+=1
        
for b in range(1,n+1):
    if graph[1][b]==maximum:
        print(b,graph[1][b],maximum_count)
        break

        
# 하지만 이 문제의 입력 조건이 20000 이하이므로 플로이드 방식으로 풀면 시간초과 판정
