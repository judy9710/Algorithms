N=int(input())
students=[]
for i in range(N*N):
    students.append(list(map(int,input().split())))
#print(students)
seat=[[0]*N for _ in range(N)]
#print(seat)

def liking(likes):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1] # 상하좌우
    result=[]
    for i in range(N):
        for j in range(N):
            a=0
            b=0
            if seat[i][j]==0: #비어있는 경우면
                for k in range(4): #상하좌우 체크
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if nx<0 or nx>=N or ny<0 or ny>=N:
                        continue # 벗어나는 경우면 패스
                    else:
                        if seat[nx][ny] in likes:
                            a+=1 # 좋아하는 사람이면
                        if seat[nx][ny]==0:
                            #print(nx)
                            #print(ny)
                            b+=1 # 비어있는 경우면
                result.append([a,b,(i,j)])
    return result

for s in students:
    # 비어있는 칸 중에서 상하좌우의 좋아하는 학생들의 명수 체크하기
    # 그 중에서 최대값 뽑아내고
    # 그게 중복되게 여러 개이면 비어있는 칸의 개수 체크하기
    # 행의 번호 열의 번호 가장 작은
    # 기준별로 sorting 하는 코드가 필요할듯
    number=s[0]
    likes=s[1:]
    temp=liking(likes)
    #print(temp)
    #print('------')
    temp.sort(key=lambda x: (x[0],x[1],-x[2][0],-x[2][1]),reverse=True)
    #print(temp)
    #print('******')
    x=temp[0][2][0]
    y=temp[0][2][1]
    seat[x][y]=number

#print(seat)
new_dict={}
for s in students:
    new_dict[s[0]]=s[1:]
#print(new_dict)

def satisfy(number):
    return new_dict[number]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
values=[]
for i in range(N):
    for j in range(N):
        student=seat[i][j]
        value=0
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            else:
                if seat[nx][ny] in satisfy(student):
                    value+=1
        values.append(value)
total=0
for v in values:
    if v==0:
        continue
    elif v==1:
        total+=1
    elif v==2:
        total+=10
    elif v==3:
        total+=100
    elif v==4:
        total+=1000
print(total)


