import random
pwdr=input("Enter the new five digit numeral password")

i1=j1=0
finlst=[]
if len(pwdr)==5:
    pwdrl=list(pwdr)
    encpylst=["!","1","2","3","4",'5','6','7','8','9','0','@','#']
    while i1<=50:
        if i1 in [3,20,31,38,45]:
            finlst.append(pwdrl[j1])
            j1+=1
            i1+=1
        else:
            finlst.append(encpylst[random.randint(0,12)])
            i1+=1
print(finlst)
