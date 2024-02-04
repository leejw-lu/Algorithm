class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums[1], nums[0] + nums[2])
    
        dp = [0] * n
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]

        for i in range(3,n):
            dp[i]=max(dp[i-3],dp[i-2]) + nums[i]

        return max(dp[-1],dp[-2])

        # 다른 방법
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # return dp[n-1]