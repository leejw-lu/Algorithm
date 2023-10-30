import sys
from collections import deque
read=sys.stdin.readline

word=read().rstrip()
stack=deque()
tag=False
result=''

for i in word:
    if i == '>':
        tag = False
        result += i
    elif i == '<':
        while stack:
            result += stack.pop()
        result += i
        tag = True
    elif i == ' ':
        while stack:
            result += stack.pop()
        result += i
    elif tag: #tag 단어 일 경우
        result += i
    else:     #뒤집어야 할 단어
        stack.append(i)

while stack:
    result += stack.pop()

print(result)