import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m,k,x=map(int,input().split())
graph=[[] for i in range(n+1)]

distance=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))

def dijkstra(x):
    q=[]
    heapq.heappush(q,(0,x))
    distance[x]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(x)
count=0
for i in range(n+1):
    if distance[i]==k:
        print(i)
        count+=1
if count==0:
    print(-1)

