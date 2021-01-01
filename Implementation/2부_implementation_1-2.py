n=int(input())
count=0
m_s=[3,13,23,30,31,32,33,34,35,36,37,38,39,43,53]
h=[3,13,23]

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if (k in m_s) or (j in m_s) or (i in h) :
                count+=1

print(count)


# if 절에서 문자열로 변경한 시각에 '3'이 포함되어 있다면
# 카운트 증가시키는 방법을 사용해도 된다. 그러면 m_s, h 따로 정의할 필요 X

# if '3' in str(i)+str(j)+str(k) 

