'''
n=eval(input(""))
m=eval(input(""))
if(n>=0 and m<0)or (m>=0 and n<0):
    print("True")
else:
    print("FALSE")

n=eval(input(""))
m=eval(input(""))
if(n>=0 )==(m>=0):
    print("true")
else:
    print("false")
'''
'''
#greatest integer number bt 2 number .

a=int(input(""))
b=int(input(""))
if(a>b):
    print(a,"is the greatest number.")
elif(b>a):
    print(b,"is the greatest number")
else:
    print(a,"and",b,"both are equal.")



#take input of age of 3 user determine oldest among them
a=int(input(""))
b=int(input(""))
c=int(input(""))
if(a>b and a>c):
    print(a,"is the oldest one.")
    if(b>c):
        print(c,"is younger one.")
    elif(c>b):
        print(b,"is younger one.")
if(b>a and b>c):
    print(b,"is the oldest one.")
    if(a>c):
        print(c,"is younger one")
    elif(c>a):
        print(a,"is younger one.")
if(c>a and c>b):
    print(c,"is the oldest one.")
    if(a>b):
        print(b,"is younger one.")
    elif(b>a):
        print(a,"is younger one.")


i=0
sum=a+b+c
while i<sum :



####################################################
a=int(input(""))
if(a>=18):
    print("eligible for voting")
else:
    print("not eligible for voting.")


####################################################

n=int(input(""))
count=0
for a in range(1,n+1):
    if(a%7==0):
        count+=1
print(count)



n=int(input(""))
if(n%4==0):
    print("yes")
else:
    print("no")


d=int(input(""))
s=str(d)
sum=int(s[1:2])+int(s[2:4])+int(s[4:])
print(sum)

'''
a=9
if(5<a<=10):
    print("class continue")
else:
    print("class stop")


























        
