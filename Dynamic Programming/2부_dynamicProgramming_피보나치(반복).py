# 대표적인 다이나믹 프로그래밍 예제인 피보나치를 반복적인 방법으로 풀기
# 보틈업=상향식=DP 테이블 사용

dp=[0]*100
dp[1]=1
dp[2]=1
def fibo(x):
    for i in range(3,x+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[x]
print("피보나치를 반복적으로 하면")
print(fibo(int(input())))
