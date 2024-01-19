###################### ver1 (1860ms)
import sys
read=sys.stdin.readline

s1=read().rstrip()
s2=read().rstrip()
dp=[[""]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+s1[i-1]
        else:
            if len(dp[i-1][j])>=len(dp[i][j-1]):
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i][j-1]

if dp[-1][-1]=="":
    print(0)
else:
    print(len(dp[-1][-1]))
    print(dp[-1][-1])

######################### ver2 (584ms)
import sys
read=sys.stdin.readline

s1=read().rstrip()
s2=read().rstrip()
dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

def lcs():
    lcs=''
    count=0
    i, j= len(s1), len(s2)
    while True:
        if count==dp[-1][-1]:
            break
        if s1[i-1]==s2[j-1]:
            lcs=s1[i-1]+lcs
            count+=1
            i-=1
            j-=1
        else:
            if dp[i][j]==dp[i-1][j]: #up
                i-=1 
            elif dp[i][j]==dp[i][j-1]: #left
                j-=1
    print(lcs)

print(dp[-1][-1])
if dp[-1][-1]!=0:
    lcs()

