def solution(sizes):
    for i in range(len(sizes)):
        sizes[i].sort(reverse=True) #x,y중 더 큰값 x로 보내기
    
    s1,s2=0,0
    for i in range(len(sizes)):
        s1=max(s1, sizes[i][0])
        s2=max(s2, sizes[i][1])

    return s1*s2

    # w=[]
    # h=[]
    # for s in sizes:
    #     w.append(max(s))
    #     h.append(min(s))
    # print(w)
    # print(h)
    # return max(w)*max(h)