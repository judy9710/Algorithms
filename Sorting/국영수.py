n=int(input())
array=[]

for i in range(n):
    data=input().split()
    #이름은 문자열 그대로, 점수는 정수형으로 변환하여 저정
    array.append((data[0],int(data[1]),int(data[2]),int(data[3])))
    i=[]

# 키를 이용하여, 점수를 이용하여 정렬
array=sorted(array,key=lambda student: student[1], reverse=True)
previous=101

i=0
for student in array:
    if student[1]==previous:
        i=str(int(i))
        i.append(student)
        previous=student[1]
    else:
        i=str(int(i)+1)
        i.append(student)
        previous=student[1]
    i=int(i)

result1=[]

for i in range(i):
    i=str(int(i))
    i=sorted(i,key=lambda student: student[2])
    result1+i

previous1=0
for student in result:
    if student[2]==previous1:
        i=str(int(i)+1)
        i.append(student)
        previous1=student[2]
    else:
        i=str(int(num_of_1stGroups))
        i.append(student)
        previous=student[2]
    
    # 이렇게 하면 너무 복잡해지고 시간안에 못풀었다
