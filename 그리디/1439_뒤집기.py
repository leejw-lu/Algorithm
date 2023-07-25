import sys
read=sys.stdin.readline

s=read().rstrip()
count=0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        count+=1
print((count+1)//2)



######첫시도 코드
#str=read().rstrip()
#arr=list(str)
#print(arr)  >> ['0', '0', '0', '1', '1', '0', '0']

#count0=arr.count('0')
#count1=arr.count('1')

#result=0
#for i in range(len(arr)):
 #   if count0>=count1:
  #      if arr[i]=='1':
   #         arr[i]='0'
    #        result+=1
    #else:
     #   if arr[i]=='0':
      #      arr[i]='1'
       #     result+=1
#print(result)        

