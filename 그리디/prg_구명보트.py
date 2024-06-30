def solution(people, limit):
    answer = 0
    people.sort()
    
    start=0
    end=len(people)-1
    
    #보트 최대 2명!!!
    #최적-> 무거운사람+ 가벼운사람
    
    while start<=end:
        if people[start]+people[end]<=limit: #2명 다 태울 수 있는 경우
            start+=1
        end-=1
        answer+=1
    
    return answer