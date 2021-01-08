n=int(input())
# 입력받는 이름과 점수를 튜플 형식으로 저장하는 것이 가장 좋겠다
array=[]
for i in range(n):
    name,score=input().split()
    score=int(score)
    array.append((name,score))

array=sorted(array,key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')
