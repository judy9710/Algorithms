array=[7,5,9,0,3,1,6,2,4,8]

# 선택정렬

def selection_sort(array):
    for i in range(len(array)):
        min_index=i
        for j in range(i+1,len(array)):
            if array[j]<array[min_index]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]

    print(array)

selection_sort(array)

array2=[7,5,9,0,3,1,6,2,4,8]

# 삽입정렬

def insertion_sort(array2):
    for i in range(1,len(array2)):
        for j in range(i,0,-1):
            if array2[j]<array2[j-1]:
                array2[j],array2[j-1]=array2[j-1],array2[j]
            else:
                break
    print(array2)

insertion_sort(array2)

