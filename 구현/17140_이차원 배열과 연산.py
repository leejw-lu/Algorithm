r,c,k=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(3)]
time=0

#r연산
def R():
    global graph
    newGraph=[]
    for i in graph:
        elem=set(i) #원소만 추출
        eleCnt=[] #(e원소, cnt갯수)
        tmp=[]
        for e in elem:
            if e==0: continue
            cnt=i.count(e)
            eleCnt.append((e,cnt))
        eleCnt.sort(key=lambda x: (x[1], x[0]))

        for ec in eleCnt:
            tmp.append(ec[0])
            tmp.append(ec[1])
        tmp=tmp[:100] #100개까지

        newGraph.append(tmp)
    maxLen=max(map(len, newGraph))

    #빈칸 0만큼 채우기
    for i in range(len(newGraph)):
        while len(newGraph[i]) !=maxLen:
            newGraph[i].append(0)

    graph=newGraph

#---------main
for i in range(101):
    if r-1<len(graph) and c-1<len(graph[0]):
        if graph[r-1][c-1]==k:
            print(time)
            break

    # try:
    #     if graph[r-1][c-1] == k: #index 범위 넘어가는 경우 방지
    #         print(ans)
    #         break
    # except:pass

    #중복되니까 행-열 바꾸고 R연산
    time+=1
    if len(graph[0]) > len(graph): 
        graph = list(map(list,zip(*graph)))
        R()
        graph = list(map(list,zip(*graph)))
    else:
        R()
else:
    print(-1)