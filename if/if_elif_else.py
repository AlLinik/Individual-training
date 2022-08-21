a = 0
if a > 0:
    b = a + 5
    if b > 10:
        print('b>10')
    elif b == 10:
        print('b=10')
    else:
        print('b<10')
elif a < 0:
    if a == -5:
        print('a=-5')
    elif a < -5:
        print('a<-5')
    else:
        print('a>-5')
else:
    print('a=0')