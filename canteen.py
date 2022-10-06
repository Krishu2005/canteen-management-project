import csv
import pickle
import os
a=open('admin1.csv','r')
s=open('stflg.csv','r')
ar=csv.reader(a)
sr=csv.reader(s)
admin=[]
staff=[]
x=0
for i in ar:
    if x!=0:
        admin.append(i)
    x=x+1
y=0
for i in sr:
    if y!=0:
        staff.append(i)
    y=y+1
print(admin)
print(staff)


print('WELCOME TO CANTEEN MANAGEMENT SYSTEM')
def two(admin):
    print('please verify your id')
    k=(input('enter login id')).upper()
    print(k)
    z=int(input('enter login password'))
    l=str(z)
    print(l)
    c=0
    for i in admin:
        print(i[0])
        print(i[1])
        if k==i[0]:
            c=c+1
            if l==i[1]:
                c=c+1
            else:
                print('password is incorrect')
                two(admin)
        else:
            print('id is incorrect')
            two(admin)
    if c==2:
        print('gajab')
    else:
        print('hatt')
    
def one(admin,staff):
    print('please select your login type')
    print('press 1 for admin\n''press 2 for staff')
    k=int(input('enter your choice'))
    if k==1:
        two(admin)
one(admin,staff)
