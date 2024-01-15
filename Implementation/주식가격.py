def solution(prices):
    answer = []
    # 시계열 주식가격 데이터임
    for i in range(len(prices)):
        count=0
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                count+=1
            elif prices[i]>prices[j]:
                count+=1
                break
        answer.append(count)
        #print(answer)
    return answer
