n,m=map(int,input().split())

result=0

for i in range(n):
    data=list(map(int,input().split()))
    # 처음에는 잘못 생각한 부분이 한줄씩 입력받는 부분이었다.
    min_value=min(data)
    result=max(result,min_value)

print(result)
