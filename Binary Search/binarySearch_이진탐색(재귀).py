# 이진탐색을 재귀함수를 사용하여 구현하는 방법

def binary_search(array,start,end,target):
    if start>end:
        return None
    mid=(start+end)//2

    if array[mid]==target:
        return mid+1
    elif array[mid]>=target:
        return binary_search(array,start,mid-1,target)
    elif array[mid]<=target:
        return binary_search(array,mid+1,end,target)

n,target=map(int,input().split())
array=list(map(int,input().split()))
result=binary_search(array,0,n-1,target)
if result==None:
    print("원소가 존재하지 않습니다")
else:
    print(result)
