import sys
read=sys.stdin.readline

n,m= map(int,read().split())
arr1=set()  #시간복잡도 O(1)
arr2=set()
for _ in range(n):
    arr1.add(read().rstrip())
for _ in range(m):
    arr2.add(read().rstrip())

result=sorted(list(arr1 & arr2)) #교집합 리스트 정렬

print(len(result))
for i in result:
    print(i)
