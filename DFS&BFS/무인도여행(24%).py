counts=[]
def dfs(x,y,n,m,map,count,visited):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    if x>=0 and x<=n-1 and y>=0 and y<=m-1:
        if map[x][y]=='X':
            #print(map[x][y])
            if visited[x][y]==False:
                visited[x][y]=True
            return False
        elif map[x][y]!='X':
            #print(map[x][y])
            if visited[x][y]==False:
                count+=int(map[x][y])
                counts.append(count)
                visited[x][y]=True
                possible_direction=[[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
                flag=0
                flags=[]
                for i in possible_direction:
                    dfs(i[0],i[1],n,m,map,count,visited)
                    flag+=1
                    flags.append(flag)
                print(flags)
                for f in flags:
                    if f>=4:
                        counts.append('end of recursive')
                    
            return True
                                                 
        return False

def solution(maps):
    # 전형적인 bfs/dfs 문제이다
    n = len(maps)
    m = len(maps[0])
    map=[[] for i in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            map[i].append(maps[i][j])
    visited=[[False]*m for _ in range(n)]  
    #print(visited)
    answer=[]
    for i in range(n):
        for j in range(m):
            dfs(i,j,n,m,map,count,visited)
        
    #print(visited)
    #print(counts)
    for i in range(len(counts)):
        if counts[i]=='end of recursive': #parsing 하는 방법 re로 import 하는 방법 찾기
            #print(counts[i-1])
            answer.append(counts[i-1])
    print(counts)
    answers=[]
    for a in answer:
        if a!='end of recursive' and a!=0:
            answers.append(a)
    print(answer)
    print(answers)
    answerss=sorted(answers)
    if answers==[]:
        answerss.append(-1)
    print(answerss)
    return answerss

