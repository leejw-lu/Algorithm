import sys
read=sys.stdin.readline

money =int(read())
stock=list(map(int,read().split()))

moneyA=money #junhyun->A  
moneyB=money #sungmin->B
countA=0
countB=0

#준현case
for i in range(len(stock)):
    count=moneyA//stock[i]
    if count>0:
        countA+=count
        moneyA%=stock[i]

#성민case
for i in range(len(stock)-3):
    if stock[i]<stock[i+1] and stock[i+1]<stock[i+2]: #주가상승->전부 매도
        moneyB+= countB* stock[i+3]
        countB=0
    if stock[i]>stock[i+1] and stock[i+1]>stock[i+2]: #주가하락->전부 매수
        countB+=moneyB//stock[i+3]
        moneyB%=stock[i+3]

#자산비교
junhyun=moneyA + stock[-1]*countA
sungmin=moneyB + stock[-1]*countB

if junhyun>sungmin:
    print("BNP")
elif sungmin>junhyun:
    print("TIMING")
else:
    print("SAMESAME")

        

            
    
    



