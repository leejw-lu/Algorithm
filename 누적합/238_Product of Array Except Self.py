class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[1]*n
        pre=1 #선택된 idx 이전 결과
        post=1 #선택된 idx 이후 결과
        for i in range(n):
            result[i]*=pre
            pre=pre*nums[i]
            #print("pre: ", pre)
            result[n-i-1]*=post
            #print("result: ", result)
            post=post*nums[n-i-1]
            #print("post: ", post)
        return result
