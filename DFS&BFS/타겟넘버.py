def solution(numbers, target):
    leaves = [0]          # 모든 계산 결과를 담자      
    count = 0
    for num in numbers :
        temp = []
        for leaf in leaves :
            temp.append(leaf + num)    # 더하는 경우 
            temp.append(leaf - num)    # 빼는 경우
        leaves = temp 
    for leaf in leaves : 
        if leaf == target :
            count += 1
    return count
