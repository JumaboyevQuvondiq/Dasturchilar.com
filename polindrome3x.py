import sys

son1=999
son2=999
a=0
while son1>99:
    son2=999
    while son2>990:
        a=son1*son2
        b=0
        c=a
        while a:
            b=b*10+int(a%10)
            a//=10
        if(b==c):
            print('son 1= '+str(son1),'son 2 = '+str(son2),'\n',b)
            sys.exit()
        son2-=1
    son1-=1