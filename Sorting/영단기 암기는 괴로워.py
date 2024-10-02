# 백준 20930번
# 영단어 암기는 괴로워 (실버3)

# 우선, 단어를 sys.input.readline으로 받아온다
# pypy를 사용한다
import sys
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
words=dict()
#print(words)
for _ in range(n):
    word=input().rstrip()
    if len(word)<m:
        continue
    else:  
        if word in words:
            words[word]+=1
        else:
            words[word]=1
        
word_lst=sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in word_lst:
    print(i[0])
