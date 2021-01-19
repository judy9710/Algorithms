from collections import deque
n=int(input())
indegree=[0]*(n+1)
graph=[[] for i in range(n+1)]

for i in range(1,n+1):
    pre=list(map(int,input().split()))
    cost=pre[0]
    pre.remove(-1)
    pre=pre[1:]
    if len(pre)==0:
        graph[i].append((cost,i))
    else:
        for j in pre:
            graph[i].append([cost,j])
            indegree[i]+=1

def topology_sort():
    q=deque()
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)
    while q:
        cost=[0,0]
        now=q.popleft()
        for i in graph[now]:
            cost+=graph[i[1]][0]  #이렇게 하면 앞에 prerequisite가 많은 경우에
            # 또 재귀적으로 하지 못하게 되는 문제점 발생
            indegree[now]-=1
            if indegree[now]<=0:
                q.append(i)
        #cost+=graph[now][0][0]
        print(cost)

topology_sort()
