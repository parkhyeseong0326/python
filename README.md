def 직삼각형():
    a = int(input())
    b = a
    c = 0
    for i in range(a+1):
        b -= 1
        c += 1
        print(" "*c,"*"*(b+1))
def 마름모():
    v = int(input())
    b = 0
    c = v
    for i in range(v) :
        b += 1
        c -= 1
        print(" "*(c),"*"*(b+i))
    b = v
    c = 0
    for i in range(v) :
        c += 1
        b -= 1
        print(" "*c,"*"*(b+b-1))
while 1:
    k = int(input("직삼각형이면 1 , 마름모면 2 : "))
    if k == 1:
        print(직삼각형())
    elif k == 2:
        print(마름모())
    else :
        print("1 과 2중에 출력하세요")
