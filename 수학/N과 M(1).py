import itertools

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)] 
#[1,2,3,4]

p_array = itertools.permutations(nums, m)
#[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

#(4, 3)
for i in p_array:
    for j in i:  
        print(j, end = ' ') #4 3
    print()
