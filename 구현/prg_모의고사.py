def solution(answers):
    result = []
    a=[1,2,3,4,5] #5  //*2000 하는게 아니라... [(i%5)] 
    b=[2,1,2,3,2,4,2,5] #8 * 1250 하는게 아니라 [(i%8)]해야 시간복잡도 통과
    c=[3,3,1,1,2,2,4,4,5,5] #10
    
    counts=[0,0,0]
    for i in range(len(answers)):
        if answers[i]==a[(i%5)]:
            counts[0]+=1
        if answers[i]==b[(i%8)]:
            counts[1]+=1
        if answers[i]==c[(i%10)]:
            counts[2]+=1
    
    maxCnt=max(counts)
    for i in range(3):
        if counts[i]==maxCnt:
            result.append(i+1)
            
    return result