t=int(input())
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if x>=0 and x<=n-1 and y>=0 and y<=m-1:
        if array[x][y]==1:
            array[x][y]=0
            possible_direction=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
            for i in possible_direction:
                dfs(i[0],i[1])
            return True
        return False

for _ in range(t):
    m,n,k=map(int,input().split())
    array=[[0]*m for _ in range(n)]
    #print(array)
    for _ in range(k):
        i,j=map(int,input().split())
        array[j][i]=1
    #print(array)
    count=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                count+=1
    print(count)

