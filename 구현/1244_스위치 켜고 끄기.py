import sys
input=sys.stdin.readline

def switch_onoff(idx):
    #arr[i] = 1 if arr[i] == 0 else 0 ->함수 안쓰고 가능
    if arr[idx]==0:
        arr[idx]=1
    else:
        arr[idx]=0
    return

n=int(input())
arr=[0]+list(map(int,input().split()))

k=int(input()) #사람수
for _ in range(k):
    gender,num=map(int,input().split())

    if gender==1: #남자
        #for i in range(num,n+1,num)
        for i in range(1,n//num+1): #배수 개수 만큼
            switch_onoff(num*i)

    else: #여자
        switch_onoff(num)         #num번째 바꾸기

        for i in range(n//2):
            if num-i<1 or num+i>n: #index 검사
                break
            if arr[num-i]==arr[num+i]:
                switch_onoff(num-i)
                switch_onoff(num+i)
            else:
               break

for i in range(1,n+1):
    print(arr[i], end=' ')
    if i%20==0:
        print()