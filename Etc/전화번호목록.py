def solution(phone_book):
    answer = True
    count=0
    # 해시
    phone_book.sort(key=lambda x:len(x))
    #print(phone_book)
    for i in range(len(phone_book)-1):
        print('-----')
        for k in range(i+1,len(phone_book)):
            #print('*****')
            for j in range(len(phone_book[i])):
                #print(i,k,j)
                if phone_book[i][j]==phone_book[k][j]:
                    answer=False
                    #print(answer)
                    if j!=len(phone_book[i]):
                        continue
                    else:
                        break
                else:
                    answer=True
                    #print(answer)
                    break
            #print('end of first for ')
            if answer==False:
                count+=1
                return answer
        if answer==True:
            continue
        else:
            break
    if answer==False:
        return answer
    return answer
