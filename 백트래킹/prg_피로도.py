from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for p in permutations(dungeons, len(dungeons)):
        cur=k #현재 남은 피로도
        count=0
        
        for least, consume in p: #최소, 소모
            if cur>=least:
                cur-=consume
                count+=1
        answer=max(answer, count)
        
    return answer