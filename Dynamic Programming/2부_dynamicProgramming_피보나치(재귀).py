# 대표적인 다이나믹 프로그래밍 예제인 피보나치를 재귀적인 방법으로 풀기
# 탑다운=하향식=메모이제이션 기법

d=[0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]
print("피보나치를 재귀적으로 하면")
print(fibo(int(input())))
    
