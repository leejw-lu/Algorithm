h,w=map(int,input().split())
block=list(map(int,input().split()))
rain=0

for i in range(1,w-1):
    left=max(block[:i])
    right=max(block[i:])
    m=min(left,right)

    if m>block[i]:
        rain+=m-block[i]
        
print(rain)