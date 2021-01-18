INF=int(1e9)
import heapq
import sys
input=sys.stdin.readline

n,m,c=map(int,input().split())
graph=[[] for i in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(c):
    q=[]
    heapq.heappush(q,(0,c))
    distance[c]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(c)

count=0
# max_distance=max(distance) -> 이렇게 하면 INF가 출력된다는 문제점
max_distance=0
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)
print(count-1,max_distance)
# 시작 노드는 제외해야 하므로 count-1을 출력
