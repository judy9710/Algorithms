# 게임 개발

n,m=map(int,input().split())
a,b,d=map(int,input().split())
maps=[]
for i in range(n):
  maps.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

visited=[[0]*m for _ in range(n)] # 방문 정보를 저장하기 위한 리스트 생성
visited[a][b]=1 # 처음 게임 캐릭터의 위치를 방문 표시

def turn_left():
  global d
  d-=1 # 함수 밖에서 선언된 전역변수이므로
  if d==-1:
    d=3

# 시뮬레이션 시작
count=1
turn_time=0
while True:
  turn_left()
  na=a+dx[d]
  nb=b+dy[d]
  if visited[na][nb]==0 and maps[na][nb]==0: # 아직 방문하지 않았고 육지아면
    visited[na][nb]=1 # 방문처치를 한다
    a=na
    b=nb #새롭게 좌표 이동시킨다
    count+=1
    turn_time=0
    continue
  else: # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다로만 구성되어 있으면
    turn_time+=1
  # 네 방향 모두 갈 수 없는 경우
  if turn_time==4:
    na=a-dx[d]
    nb=b-dy[d]
    # 뒤로 갈 수 있다면 이동하기
    if maps[na][nb]==0:
      a=na
      b=nb
    # 뒤가 바다로 막혀있는 경우
    else:
      break
    turn_time=0

print(count)

