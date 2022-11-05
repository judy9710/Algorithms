# 본 문제는 순차탐색하면서 특정한 문자열의 위치를 찾는 문제입니다 (몇 번째)

def sequential_search(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i+1

print("n과 문자열을 입력하세요")
n,target=input().split()
n=int(n)
print("문자열 배열을 생성하세요 한 칸씩 띄웁니다")
array=input().split()

print(sequential_search(n,target,array))
