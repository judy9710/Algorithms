def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
n=int(input())
parent=[0]*(n+1)

edges=[]
result=0

for i in range(1,n+1):
    parent[i]=i

x=[]
y=[]
z=[]

for i in range(1,n+1):
    data=list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i)) # 각각 x y z 좌표를 입력받아서 저장한다. 추가로 행성 번호도 저장

x.sort()
y.sort()
z.sort() # 한꺼번에 sort 하기 어려운 경우는 따로 저장해서 sort하는 방법을 생각하기

# 인접한 노드들로부터 간선 정보를 추출하여 정리
for i in range(n-1):
    # 비용순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 정리
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1])) # 두 행성끼리의 거리정보와 행성의 정보
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort() #간선을 비용순으로 정리

# 간선을 하나씩 확인하며
for edge in edges:
    cost,a,b=edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
print(result)
