s=input()
zero=0
one=0
count=1
for i in range(1,len(s)):
    current=s[i]
    previous=s[i-1]
    if previous=='0' and previous==current:
        count=count
    elif previous=='0' and previous!=current:
        zero+=1
        count+=1
    if previous=='1' and previous==current:
        count=count
    elif previous=='1' and previous!=current:
        one+=1
        count+=1
        
if zero>one:
    for i in range(len(s)):
        if s[i]=='1':
            s[i]=='0'
    print(one)
else:
    for i in range(len(s)):
        if s[i]=='0':
            s[i]=='1'
    print(zero)

