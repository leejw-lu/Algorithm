n=int(input())
digit=[]

for _ in range(n):
    contents=input()
    num=''
    for idx, c in enumerate(contents):
        if c.isdigit():
          num+=c
          if idx==len(contents)-1:
              digit.append(num)
        else:
            if num!='':
                digit.append(num)
            num=''

#0 제거 후 정렬
for i in range(len(digit)):
    digit[i]=int(digit[i])

digit.sort()
for d in digit:
    print(d)