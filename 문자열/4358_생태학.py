import sys
from collections import defaultdict
read=sys.stdin.readline


tree_list=defaultdict(int) #key-value에서 기본value 값이 0인 dictionary
count=0

while True:
    tree=read().rstrip()
    if tree=='':
        break

    tree_list[tree] +=1
    count+=1

tree_list=sorted(tree_list.items()) #정렬

for k,v in tree_list:
    print('%s %.4f' %(k, (v/count)*100))

