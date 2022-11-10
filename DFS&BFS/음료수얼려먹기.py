n,m=map(int,input().split())
ice=[]
for i in range(n):
    ice.append(list(map(int,input())))

count=0

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if x>=0 and x<=n-1 and y>=0 and y<=m-1:
        if ice[x][y] == 0:
            ice[x][y]=1
            possible_direction=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
            for i in possible_direction:
                dfs(i[0],i[1])
            return True
        return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count+=1
print(count)
            
            
            
    
