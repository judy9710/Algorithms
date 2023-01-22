# 선택 정렬
# 선택 정렬을 매번 가장 작은 원소를 선택한다는 의미에서 이름을 따옴
# 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완성됨
array1=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array1)):
    min_index=i
    for j in range(i+1, len(array1)):
        if array1[min_index]>array1[j]:
            min_index=j
    array1[i],array1[min_index]=array1[min_index],array1[i] #파이썬에서는 스와프가 이렇게 가능함

print("선택정렬의 결과는 다음과 같다:")
print(array1)

# 삽입 정렬
# 데이터가 거의 정렬이 되어있을 때 효율적임
# 그 앞까지의 데이터는 이미 정렬되어 있다고 가정함
array2=[7,5,9,0,3,1,6,2,4,8]
for i in range(1, len(array2)):
    for j in range(i,0,-1): # 인덱스를 i부터 1까지 감소하며 반복하는 문법임(보통 range 함수는 0부터 end-1까지, 큰거에서 감소하는거면 i부터 end+1까지일것임.)
        if array2[j] < array2[j-1]:
            array2[j], array2[j-1] = array2[j-1], array2[j]
        else: # 앞의 원소까지는 이미 오름차순 정렬된 상태, 자기보다 작은 원소 만나면 stop하는 로직임
            break

print("삽입정렬의 결과는 다음과 같다:")
print(array2)

# 퀵 정렬
# 현재 알려진 정렬 알고리즘 중에서 가장 효율적인 알고리즘임
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 것임
# 피벗을 설정해서, 이를 기준으로 큰 숫자와 작은 숫자를 교환함, 호어 분할 방식으로 리스트를 분할함
# 계속 이렇게 가다가, 엇갈리는 경우에는 작은 원소와 피벗의 위치를 교환함
# 호어 분할법은 피벗을 첫번째 원소로 지정함
# 이때, 분할한 부분들의 크기는 같지 않을 수 있음
array3=[5,7,9,0,3,1,6,2,4,8]
# 재귀적 사고의 유용성: 시작 조건과 종료조건(데이터의 원소 개수가 1개 인경우 종료)
# 종료 조건을 처음에 적어준다.

def quick_sort(array3, start, end):
    if start>=end: # 원소가 1개인 경우라고 볼 수 있음
        return
    pivot = start #피벗은 1st 원소임
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복함
        while left <= end and array3[left] <= array3[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복함
        while right > start and array3[right] >= array3[pivot]:
            right -=1
        if left > right: #엇갈렸다면 피벗과 작은 원소를 교체
            array3[right],array3[pivot]=array3[pivot],array3[right]
        else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체함
            array3[left], array3[right] = array3[right], array3[left]
    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 재귀적으로 정렬을 수행함
    quick_sort(array3, start, right-1)
    quick_sort(array3, right+1, end)
# 한번 엇갈리고 나면은 right가 pivot과 바꾸니까, right 앞 뒤로 분할이 되는 개념임
quick_sort(array3, 0, len(array3)-1)
print("퀵 정렬 이후의 결과는 다음과 같습니다:")
print(array3)
# 퀵 정렬은 데이터가 이미 정렬되어 있는 경우, 매우 느리게 동작함 O(N^2) (삽입정렬과 반대임)

# 힙 정렬 (heap sort)
# 최소 혹은 최대 힙을 구성한 뒤, 정렬하는 방법임
# 1. 입력받은 리스트를 목적에 맞게 최대 힙 트리 또는 최소 힙 트리를 만든다.
# 2. 최대 힙의 루트노드와 말단 노드를 교환해줌 (한번에 하나씩 요소 (루트)를 힙에서 꺼낸 뒤,)
# 3. 꺼낸 노드를 리스트의 마지막에 저장함.
# 4. 새 루트노드에 대해 최대 혹은 최소힙을 구성함.

array4=[16,4,10,14,7,9,3,2,8,1]
def heapify(array4, index, size): #index는 루트의 인덱스를 의미함
    parent = index
    left_child= 2*index
    right_child = 2*index +1
    if left_child < size and array4[left_child]>array4[parent]:
        parent = left_child
    if right_child < size and array4[right_child]>array4[parent]:
        parent = right_child
    if (parent!=index): # parent==index면, 가장 큰 노드가 맞으므로 heapify 종료.
        array4[parent],array4[index]=array4[index],array4[parent]
        heapify(array4, parent, size)

# heapify를 하는 순서가 가장 효율적인게 있음.
# heapify는 인덱스가 전체 사이즈 나누기 2 -1부터 하는게 가장 효율적임
# 이후 만들어진 힙에서 말단 노드와 루트노드를 교환하며 (삭제하니깐) 수선을 하면 힙 정렬이 완성됨
def heap_sort(array4):
    n=len(array4)
    for i in range(n//2-1, -1, -1):
        heapify(array4, i ,n) # 최대 힙을 만드는 과정임

    for i in range(n-1, 0, -1):
        array4[0], array4[i] = array4[i], array4[0] # 루트노드와 말단노드를 교환하며
        heapify(array4, 0, i) # 수선을 하면 힙 정렬이 완성됨
    return array4 # 따로 정렬된 리스트를 선언하지 않은 경우임

print("힙 정렬이 완성된 결과는 다음과 같습니다")
print(heap_sort(array4))



# 계수 정렬 (counting sort)
# 데이터의 값들이 모두 양의 정수일 때만 동작하는 매우 빠른 알고리즘임
# 최악의 경우에도 O(N+K), N 은 데이터 개수, K 는 최대값
# 비교 기반의 정렬 알고리즘이 아님
# 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보 (계수 정보)를 담는다는 성질, 
# 리스트를 전부 초기화해야 하므로 큰 수와 작은 수가 그리 차이 나지 않는 경우에 사용하기에 적합함
# 데이터의 범위만 한정이 되어있다면 효과적으로 사용할 수 있으며 항상 빠르게 동작함
def counting_sort():
    array5=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
    count=[0]*(max(array4)+1)
    sorted=[]

    for i in range(len(array5)):
        count[array5[i]]+=1 # 각 데이터의 값에 대해서 해당하는 인덱스의 값 증가
    
    for i in range(len(count)): # 리스트에 기록된 정렬 정보의 확인
        for j in range(count[i]): # 리스트에 기록된 개수만큼 출력하도록 for문 중첩
            sorted.append(i)

    print(sorted)
print("게수 정렬의 값은 다음과 같습니다: ")
counting_sort()

# 정렬 라이브러리에서 key를 활용한 소스코드
# sorted() 라이브러리나 sort() 내장함수를 이용할 때는 key 매개변수를 입력으로 받을 수 있음
# key 값으로는 하나의 함수가 들어가야 하며 이는 정렬 기준이 됨

array=[('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result=sorted(array, key=setting)
print(result)
#결과로 출력되는 것은 정수를 키로 삼아서 순서대로 출력됨.