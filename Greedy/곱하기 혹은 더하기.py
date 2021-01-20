s=input()
operation=[]
result=0
string=[]
for i in s:
    string.append(int(i))
print(string)

temp=0

for i in string:
    if i==0 or i==1:
        result+=i
    else:
        temp=result*i
        if temp==0:
            result+=i
        else:
            result=temp
            
print(result)
