def solution(brown, yellow):
    answer = []
    yx,yy=0,0
    
    for i in range(1,yellow+1): #i는 yellow의 약수
        if yellow %i ==0:
            yx=int(yellow//i)
            yy=i
            
            if 2*yx + 2*yy + 4 == brown:
                answer.append(yx+2)
                answer.append(yy+2)
                break
                
    answer=sorted(answer, reverse=True)
    return answer