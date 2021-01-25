n,m=map(int,input().split())
graph=[[] for i in range(1,n+1)]


for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    
#print(graph)

def count_place(node,result):
    if len(graph[node])!=0:
        for n in graph[node]:
            result.append(x for x in graph[n])
            for e in graph[n]:
                count_place(e,result)
    return result

for i in range(1,n+1):
    result=count_place(i,[])
    count=len(set(result))+1
    if count==n:
        print(i)
