# 딱 보니까 dfs 문제인 것 같았당 (음료수 얼려먹기와 비슷함)
def solution(n, computers):
    answer = 0
    graph=[[] for i in range(n+1)]
    print(graph)
    visited=[False]*(n+1)
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1:
                if i!=j:
                    graph[i+1].append(j+1)
    print(graph)
    count=0
    for i in range(1,n+1):
        if not visited[i]:
            answer+=dfs(graph,i,visited,count)
    return answer

def dfs(graph,v,visited,count):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited,count)
    count+=1
    return count

# 테스트 케이스 1,2,4,7은 시작 노드가 꼭 1이 아니므로 생기는 오류임
