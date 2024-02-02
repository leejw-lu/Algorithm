#반복되는 문자가 없는 가장 긴 부분 문자열
#슬라이딩 윈도우
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        start=end=0
        arr=set()

        while start<len(s) and end<len(s):
            if s[end] not in arr:
                arr.add(s[end])
                length=max(length,end-start+1)
                end+=1
            else:
                arr.remove(s[start])
                start+=1
        return length