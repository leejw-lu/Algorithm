import sys

read=sys.stdin.readline
count=int(read())

data=[sum(map(int,read.split())) for _ in range(count)]

for x in range(data):
    print(x)
