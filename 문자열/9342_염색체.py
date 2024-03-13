# 정규표현식
# ^ 해당 패턴으로 시작
# ? 해당 패턴을 0번또는 1번
# $ 해당 패턴으로 끝
# + 해당 패턴이 하나 이상
#
# import re
# p=re.compile('^[A-F]?A+F+C+[A-F]?$')
# N = int(input())
# for _ in range(N):
#     k = input()
#     if p.fullmatch(k):
#         print('Infected!')
#     else:
#         print('Good')

####
t=int(input())
for _ in range(t):
    ss=input()

    result='Infected!'
    checks=['A','B','C','D','E','F']
    pre=''
    if ss[0] not in checks or ss[-1] not in checks:
        result='Good'
    else:
        checks=['A','F','C']
        index=0
        pre='A'
        for s in ss[1:-1]:
            if pre!=s:
                index+=1
                if checks[index]!=s:
                    result='Good'
                    break
            pre=s
    print(result)