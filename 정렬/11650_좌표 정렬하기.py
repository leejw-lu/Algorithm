import sys
read=sys.stdin.readline

def compare(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] == b[0]:
        if a[1] > b[1]:
            return 1
        else:
            return 0
    else:
        return 0

def merge_sort(arr):
        if len(arr) < 2:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        merged_arr = []
        l = r = 0
        while l < len(left) and r < len(right):

            if left[l] < right[r]:
                merged_arr.append(left[l])
                l += 1
            elif left[l]>right[r]:
                merged_arr.append(right[r])
                r += 1
            else:
                if compare(left[l], right[r]) == 1:
                    merged_arr.append(right[r])
                    r += 1
                else:
                    merged_arr.append(left[l])
                    l += 1

        merged_arr += left[l:]
        merged_arr += right[r:]
        return merged_arr


N=int(read())
array = []  # 입력 받을 배열
for _ in range(N):
    array.append(tuple(map(int, input().split())))  # 좌표들 입력받기
array = merge_sort(array)  # 정렬
for x, y in array:  # 정렬된 좌표들 출력
    print(x, y, sep=' ')



########### sort 이용해서 푸는 방법
#arr=[]

#for _ in range(N):
  #   x, y= map(int,read().split())
 #    arr.append((x,y))
#arr.sort()

#for i in arr:
 #    print(i[0],i[1])

