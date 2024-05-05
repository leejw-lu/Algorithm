class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        # hash map
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        print(dic)

        if len(set(dic.values())) != len(set(arr)):
            return False
        return True