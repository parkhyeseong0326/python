class gg(): 
    def n1():
        a = int(input())
        b = a
        c = 0
        for i in range(a+1):
            b -= 1
            c += 1
            print(" "*c,"*"*(b+1))
    def n2():
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
    def n3():
        f = int(input())
        for i in range(f):
            print("*"*f)
    def n4():
        g = int(input())
        for i in range(g):
            print("* "*g)
    def n5():
        t = int(input())
        for i in range(t):
            print("*"*(i+1))
    def n6():
        u = int(input())
        b = 0
        c = u
        for i in range(u) :
            b += 1
            c -= 1
            print(" "*(c),"*"*(b+i))
k = int(input("역직삼각형이면 1 , 마름모면 2 , 직사각형이면 3 , 정사각형이면 4 , 직삼각형이면 5 , 정삼각형이면 6 :"))
if k == 1:
    gg.n1()
elif k == 2:
    gg.n2()
elif k == 3:
    gg.n3()
elif k == 4:
    gg.n4()
elif k == 5:
    gg.n5()
elif k == 6:
    gg.n6()