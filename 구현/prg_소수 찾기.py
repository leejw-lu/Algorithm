from itertools import permutations

def solution(numbers):
    answer = set()
    arr=list(numbers)
    
    permList=set()  
    for i in range(len(arr)): #len(arr)+1아닌, len(arr)
        print("i:", i)
        #set에는 += >> |+해야함. 
        permList|=set(map(int,map("".join,permutations(arr,i+1))))  #여기서 i+1 해주기.
    
    #소수판별
    for num in permList:
        if num<2: #0,1은 소수 아님
            continue
            
        flag=True
        for i in range(2,int(num**0.5)+1): #num까지해도 되는데 제곱근+1까지만 하면 필요없는 연산 줄일 수O
            if num%i==0:
                flag=False 
                break
        if flag==True:
            answer.add(num)
                            
    return len(answer)