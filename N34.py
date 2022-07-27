soz=input()
c=0
s=0
sanoq=0
while sanoq<len(soz):
    if soz[sanoq] !=' ':
        c+=1
        if c>s:
            s=c
            soz2=soz[sanoq-c+1:sanoq+1]
    else:
        c=0
    sanoq+=1
print(soz2)