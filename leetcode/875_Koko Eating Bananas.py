class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            c=0
            for p in piles:
                c+=((p-1)//mid) +1
            if c>h:
                left=mid+1
            else:
                right=mid
        return left