#After you are done modifying the input array ~

from collections import deque
class Solution:
    def compress(self, chars: List[str]) -> int:
        result=0
        i=0

        while i<len(chars):
            cur=chars[i]
            count=0
            while i<len(chars) and chars[i]==cur:
                count+=1
                i+=1
            chars[result]=cur
            result+=1
            if count>1:
                for c in str(count): #10이상인 경우 split 할 수 있게.
                    chars[result]=c
                    result+=1

        return result

        # if len(chars)==1:
        #     return 1

        # result=[]
        # count=1 

        # for i in range(1,len(chars)):
        #     if chars[i-1]!=chars[i]:
        #         if count==1: #중복원소 없을 경우 숫자X
        #             result.append(chars[i-1])
        #         else:
        #             result.append(chars[i-1])
        #             #count 10이상이면 split
        #             if count>=10:
        #                 result.append(str(count//10))
        #                 result.append(str(count%10))
        #             else:
        #                 result.append(str(count))
        #         count=1 # 초기화
        #     else:
        #         count+=1
        #         if i==len(chars)-1:
        #             result.append(chars[i-1])
        #             if count>=10:
        #                 result.append(str(count//10))
        #                 result.append(str(count%10))
        #             else: 
        #                 result.append(str(count))
                    
        # #print(result)
        # idx=len(result)
        # return idx