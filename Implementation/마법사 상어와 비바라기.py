# 골드 5
import sys
n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append(list(map(int,sys.stdin.readline().split())))
#print(array)
direction_x=[0,-1,-1,-1,0,1,1,1]
direction_y=[-1,-1,0,1,1,1,0,-1]
clouds=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

def move(steps_x, steps_y,clouds):
    new_clouds=[]
    new_x,new_y=0,0
    for c in clouds:
        #print(c[0])
        #print(c[1])
        x=c[0]+steps_x
        y=c[1]+steps_y
        if x < 0:
            x = n - (-x) % n
            if x == n:
                x = 0
        elif x >= n:
            x %= n
        if y < 0:
            y = n - (-y) % n
            if y == n:
                y = 0
        elif y >= n:
            y %= n
        new_clouds.append([x,y])
    return new_clouds

def rain(clouds):
    for c in clouds:
        #print(c)
        array[c[0]][c[1]]+=1
    return
def check(clouds,visited):
    dx=[-1,-1,1,1]
    dy=[-1,1,-1,1]
    for c in clouds:
        count=0
        for i in range(4):
            new_x=c[0]+dx[i]
            new_y=c[1]+dy[i]
            if new_x<n and new_x>=0 and new_y<n and new_y>=0:
                if array[new_x][new_y]!=0:
                    count+=1
        array[c[0]][c[1]]+=count
        visited[c[0]][c[1]]=True
    return array

for i in range(m):
    d,s=map(int,input().split())
    steps_x=direction_x[d-1]
    steps_y=direction_y[d-1]
    steps_x=steps_x*s
    steps_y=steps_y*s
    #print(steps_x)
    #print(steps_y)
    clouds=move(steps_x,steps_y,clouds)
    #print(clouds)
    rain(clouds)
    #print(array)
    visited=[[False]*n for _ in range(n)]
    array=check(clouds,visited)
    #print(array)
    temp=clouds
    clouds=[]
    for i in range(n):
        for j in range(n):
            if array[i][j]>=2 and visited[i][j]==False:
                clouds.append([i,j])
                array[i][j]-=2
    #print(clouds)
    #print('----')
#print(array)
#print(clouds)
answer=0
for i in range(n):
    for j in range(n):
        answer+=array[i][j]

print(answer)
