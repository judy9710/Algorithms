def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_find(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
n,m=map(int,input().split()) #학생 팀번호와 연산의 수
parent=[0]*(n+1)

for i in range(1,n+1):
    parent[i]=i
result=[]
for i in range(m):
    operation,a,b=map(int,input().split())
    if operation==0:
        union_find(parent,a,b)
    elif operation==1:
        if find_parent(parent,a)==find_parent(parent,b):
            result.append("Yes")
        else:
            result.append("No")
for i in result:
    print(i)
