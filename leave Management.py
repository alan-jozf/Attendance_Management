import math
sub =['CN   ','SE   ','DBMS ','DAA  ','WP   ','D-LAB','W-LAB']
#percentage=84.6
#leave persentage(p)=100-85=15(15.4)
#p=15 
TOTAL, CURRENTTOTAL, ATTENDED, LEAVETAKEN, LEAVEPOSSIBLE=[
                                        [56,54,55,56,51,52,59],
                                        [],[],[],[]
                                        ]
TT, day, result = [
        [
            #m,t,w,t,f
            [0,2,1,0,1],#CN
            [1,1,1,1,0],#SE
            [0,2,1,0,1],#DB
            [0,1,1,1,1],#DA
            [1,0,1,0,2],#WP
            [4,0,0,0,0],#DL
            [0,0,0,4,0],#WL
        ],
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        []
    ] 

print('\n'*2+' '*10+'~'*20+' '*4+'Leave Management'+' '*4+'~'*20+'\n'*2)

print('\nEnter Your Current Total Hours :')
for x in range(7):
    CURRENTTOTAL.append(int(input(sub[x]+' : ')))

print('\nEnter Your Attended Hours :')
for x in range(7):
    ATTENDED.append(int(input(sub[x]+' : ')))

percentage=float(input("\nFor normal eligibility (percentage) : 85\nFor condonation eligibility         : 70 or 75\n\nEnter your eligibility percentage   : "))
p=100-percentage
                     
"""print('\nEnter the Leave Hours that you have taken :')
for x in range(0,7):
    LEAVETAKEN.append(int(input(sub[x]+' : ')))"""

#Leave Hours that you have taken :
for x in range(7):
    LEAVETAKEN.append(CURRENTTOTAL[x]-ATTENDED[x])

#Possible Leave Hours Left for you :
print('\n\nPossible Leave Hours Left for you :')
for x in range(7):
    LEAVEPOSSIBLE.append(math.floor(TOTAL[x]*p/100)-LEAVETAKEN[x])
    print(sub[x]+' : ',LEAVEPOSSIBLE[x])

#Possible Leave Hours (eliminating negative values)
flag=0
for x in range(7):
    if (LEAVEPOSSIBLE[x]<0):
        flag +=1
        LEAVEPOSSIBLE[x]=0
 
#function for checking posibility
def possible(lp, day):
    for i in range(7):
        if(lp[i]<TT[i][day]):
            return False
    return True

#function for taking a day leave
def takeleave(lp, day):
    for i in range(7):
        lp[i]=lp[i]-TT[i][day]
    return lp

#core
def fun(balance, curres=[], theday=0, app=0):
    for i in range(theday, 5):
        if not possible(balance, i):
            continue
        else:
            curresCOPY=curres.copy()
            curresCOPY.append(day[i])
            balanceCOPY=balance.copy()
            takeleave(balanceCOPY, i)
            result.append([curresCOPY, balanceCOPY])
            fun(balanceCOPY, curresCOPY, i, app+1)


if (flag==1):
    print('\n\nYou are out of eligibility')

else:
    fun(LEAVEPOSSIBLE)
    maxcount=0
    for x in result:
        if len(x[0])>maxcount: maxcount=len(x[0])
    if maxcount==0:
        print('\n\nYou are not able to take anymore leaves')
    else:
        print('\n\n\n\tThe given Results are the Different Possibilities to take "MAXIMUM No of LEAVES" !!!\n')
        print('\n\t\t   Note that "change in Time Table will affect the accuracy" (;'+'\n'*2 +' '*13+'~'*70+'\n'*3)
        count =0
        for x in result:
            if len(x[0])==maxcount:
                count+=1
                print("\n",count,"\nTake Leaves  on       : ", x[0], '\nRemaining Leave Hours : ', x[1])
        if count<4:
            for x in result:
                if len(x[0])==maxcount-1:
                    count+=1
                    print("\n",count,"\nTake Leaves  on       : ", x[0], '\nRemaining Leave Hours : ', x[1])
        print('\n'*5+'\t\tThe given Results are the "Combinations of Week Days" which help you to take "MAXIMUM No of LEAVES"')    
        print('\n     The "Remaining Leave Hours" shows the hours left to take leaves for each subjects, after taking leaves as mentioned abouve')    
        print('\n'*5+' '*10+'~'*110)
        input('')
        input('')

