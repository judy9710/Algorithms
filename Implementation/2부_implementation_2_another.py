# 앞서 입력받은 문자를 각각 정수로 바꿔주는 작업은 체스의 크기가 커질수록 비효율적이다.
# 그러므로 문자의 uni code를 이용하는 아이디어를 이용하면 다음과 같다
# 문자의 uni code를 리턴하는 파이썬 내장함수 ord()를 사용하여 문제 해결 가능

input_data=input().split()
row=int(input_data[1])
column=int(ord(input_data[0])) -int(ord('a'))+1 # a 의 아스키 코드는 65이다.

steps=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(2,-1),(2,1)]

result=0
for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result+=1
print(result)
