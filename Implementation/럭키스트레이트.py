n=int(input())
string=[]
result1=0
result2=0

for i in str(n):
    string.append(i)
    
length=len(string)

while True:
    if length%2!=0:
        print("자릿수 입력은 짝수개이어야 합니다")
        break
    half=int(length/2)

    for s in string[:half]:
        result1+=int(s)

    for s in string[half:]:
        result2+=int(s)
           
    if result1==result2:
        print("LUCKY")
        break
    elif result1!=result2:
        print("READY")
        break
# 입력받은 것을 문자열로 하면 더 쉽게 가능
