n=int(input())
home_positions=list(map(int,input().split()))

home_positions.sort()

print(home_positions[(n-1)//2]) # 홀수개인 경우는 정확히 중간값,
# 짝수개인 경우는 두개의 choice가 있다 --> n-1/2 이나 n/2 이나 동일함
