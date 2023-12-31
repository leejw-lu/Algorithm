import sys
s=sys.stdin.readline().rstrip()

#팰린드롬 될때까지 왼쪽 문자열 개수만큼 더해주기
for i in range(len(s)):
    if s[i:]==s[i:][::-1]:
        print(len(s)+i) 
        break