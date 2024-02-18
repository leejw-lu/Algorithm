class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1=set(nums1)
        s2=set(nums2)
        #return [list(s1-s2), list(s2-s1)]

        result=[[],[]]

        for i in s1:
            if i not in s2:
                result[0].append(i)
        for j in s2:
            if j not in s1:
                result[1].append(j)

        return result