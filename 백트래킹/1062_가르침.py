import sys
input=sys.stdin.readline

n,k=map(int,input().split())
words=[set(input().rstrip()) for _ in range(n)]
alphabet=[False]*26
result=0
  #  words.append(s[4:-4]) #anta _ tica 제외 

def dfs(start, depth):
    global result

    if depth==k:
        tmp=0
        for word in words:
            flag=True
            for s in word:
                if not alphabet[ord(s)-ord('a')]: #배우지 않은 단어
                    flag=False
                    break

            #배운 글자로 단어 읽을 수 있는 경우
            if flag:
                tmp+=1
        result=max(result,tmp)
        return
    
    for i in range(start,26):
        if not alphabet[i]:
            alphabet[i]=True
            dfs(i, depth+1)
            alphabet[i]=False

if k<5:
    print(0)
    exit(0)
elif k==26:
    print(n)
    exit(0)

for c in ('a','c','i','n','t'): #a,n,t,i,c 5개는 무조건 배워야.
    alphabet[ord(c)-ord('a')]=True
    
dfs(0,5) #5글자는 이미 배움.
print(result)

