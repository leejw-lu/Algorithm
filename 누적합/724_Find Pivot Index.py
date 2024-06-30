class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0 
        total = sum(nums)

        for i, x in enumerate(nums):
            if left == total - left - x:    #left==right
                return i 
            left += x 
        return -1