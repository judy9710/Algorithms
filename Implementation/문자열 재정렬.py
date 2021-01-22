string=input()
numbers=['0','1','2','3','4','5','6','7','8','9']
result=0
alphabet=[]
for i in string:
    if i in numbers:
        result+=int(i)
    else:
        alphabet.append(i)

alphabet.sort()

for a in alphabet:
    print(a,end='')
print(result)
