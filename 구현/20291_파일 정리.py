import sys
read=sys.stdin.readline

N=int(read())
extension={} #2차원 배열 쓰면 시간초과 떠서 딕셔너리 써야함

for _ in range(N):
    file_name=read().rstrip()
    arr = file_name.split('.')
    file_name= arr[1] #확장자 저장

    if file_name in extension:
        extension[file_name]+=1
    else:
        extension.setdefault(file_name,1)

extension=sorted(extension.items())

for i in extension:
    print(i[0],i[1])