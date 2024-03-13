class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels= set("AaEeIiOoUu")
        arr=list(s)
        p1,p2= 0, len(arr)-1

        while p1<p2:
            if arr[p1] in vowels and arr[p2] in vowels:
                arr[p1], arr[p2]= arr[p2], arr[p1]
                p1+=1
                p2-=1

            if arr[p1] not in vowels:
                p1+=1

            if arr[p2] not in vowels:
                p2-=1
            
        return "".join(arr)