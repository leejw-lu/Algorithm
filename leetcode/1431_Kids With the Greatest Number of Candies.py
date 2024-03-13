class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #maxCandies = max(candies)
	    #return [candy+extraCandies >= maxCandies for candy in candies]

        maxV=max(candies)
        result=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >=maxV:
                result.append(True)
            else:
                result.append(False)
        return result