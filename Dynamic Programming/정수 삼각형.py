n=int(input())
triangle=[]
for _ in range(n):
    triangle.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            up_left=0
        else:
            up_left=triangle[i-1][j-1]
        if j==i:
            up=0
        else:
            up=triangle[i-1][j]
        # 최대 합을 저장
        triangle[i][j]=triangle[i][j]+max(up_left,up)

print(max(triangle[n-1]))
