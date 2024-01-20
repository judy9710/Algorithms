#프로그래머스 메뉴 리뉴얼
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        combs=[]
        for o in orders:
            combs+=list(combinations(sorted(o),c)) #여기서 결정적인 차이가 나는거넹
        new=Counter(combs).most_common()
        #print(new)
        #print('----')
        for menu,cnt in new:
            if len(menu)==c and cnt==new[0][1] and cnt>1:
                answer+=[''.join(menu)]
    answer.sort()
    return answer
