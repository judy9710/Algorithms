n,x=map(int,input().split())
import sys
input=sys.stdin.readline
array=list(map(int,input().split()))

# bisect 함수를 사용하지 않고 하는 방법 -> 이진 탐색을 요구하는 고난이도 문제에서
# 자주 사용할 수 있는 테그닉으로, 사용된 코드를 잘 이해하자

def count_by_value(array,x):
    n=len(array)
    
    # x 가 처음 등장한 인덱스 계산
    a=first(array,x,0,n-1)

    # 수열에 x 가 존재하지 않는 경우
    if a==None:
        return 0 # 값이 x인 원소의 개수는 0개이므로 0 반환
    
    b=last(array,x,0,n-1)

    # 개수를 반환
    return b-a+1

# 처음 위치를 찾는 이진 탐색 메서드
def first(array,target,start,end):
    if start>end:
        return None
     mid=(start+end)//2
     # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
     if (mid==0 or target > array[mid-1]) and array[mid]==target:
         return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
     elif array[mid]>=target:
         return first(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
     else:
         return first(array,target,mid+1,end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array,target,start,end):
    if start>end:
        return None
    mid=(start+end)//2
    # 해당 값을 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid==n-1 or target<array[mid+1]) and array[mid]==target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid]>target:
        return last(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array,target,mid+1,end)

count=count_by_value(array,x)

if count==0:
    print(-1)
else:
    print(count)
