# 퀵 정렬 (많이 정렬되어있을수록 시간 오래 걸림, O(NlogN) 시간 복잡도를 가짐)
# 왼쪽과 오른쪽 다시 정렬하는 재귀함수 사용

array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    pivot=start
    left=start+1
    right=end
    while left<=right:
        while left<=end and array[left]<=array[pivot]:
            left+=1
        while right>start and array[right]>=array[pivot]:
            right-=1
        if left>right: #엇갈렸으면
            array[pivot],array[right]=array[right],array[pivot]
        else: #엇갈리지 않았으면
            array[left],array[right]=array[right],array[left]
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)
        
quick_sort(array,0,9)
print(array)
            
# 파이썬의 장점을 살려서 조금 더 직관적인 방법으로 코딩해보기

array2=[5,7,9,0,3,1,6,2,4,8]

def quick_sort2(array2):
    if len(array2)<=1:
        return array2
    pivot=array2[0]
    tail=array2[1:]
    left=[x for x in tail if x<pivot]
    right=[x for x in tail if x>=pivot]

    return quick_sort2(left)+[pivot]+quick_sort2(right)

print(quick_sort2(array2))

# 계수 정렬 (count sort): 계수 정렬은 비교 기반 알고리즘이 아니고 형식이
# 제한되어 있는 경우만, 데이터 크기 커도 중복이 많으면 유리하다

array3=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 배열의 원소가 0보다 크거나 같다고 가정하면,
# 모든 범위를 포함하는 리스트를 선언한다.(모든 값은 0으로 초기화)
count=[0]*(max(array)+1)

for i in range(len(array3)):
    count[array3[i]]+=1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i,end=' ') 
