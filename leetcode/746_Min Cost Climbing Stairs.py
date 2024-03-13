class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*len(cost) # i번째 계단 최소 비용
        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2, len(cost)):
            dp[i]=min(dp[i-2],dp[i-1])+cost[i]
        #print(dp)
        return min(dp[-1],dp[-2])