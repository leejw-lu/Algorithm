import sys
read= sys.stdin.readline

A,P=map(int,read().split())
arr=[A]

while(True):
    res=0
    for s in str(arr[-1]): #index 음수로 지정하면, arr배열 뒤쪽부터 indexing 할 수 있다. ex) arr=[1,2,3,4,5]이면 arr[-1]=5
        res += int(s) **P

    if res in arr:
        break

    arr.append(res)

print(arr.index(res))