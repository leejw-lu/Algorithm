#내 구현 코드: 속도 느림 47ms

class Solution:
    def reverseWords(self, s: str) -> str:
        arr=deque(list(map(str,s.split())))
        reverse=''
        while arr:
            reverse+=arr.pop()
            reverse+=' '
        
        return reverse.rstrip()

        #짱 쉬운 코드 (35ms)
        #s=s.split()
        #return " ".join(s[::-1])