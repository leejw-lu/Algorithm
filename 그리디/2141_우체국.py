n=int(input())
town=[]
people=0

for i in range(n):
    loc,peo=map(int,input().split())
    town.append((loc,peo))
    people+=peo #사람 총합
town.sort(key=lambda x: x[0])

mid=people/2
count=0

for loc,peo in town:
    count+=peo
    if count>=mid:
        print(loc)
        break