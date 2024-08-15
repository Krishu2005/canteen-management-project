import csv
import pickle
import os
a=open('admin1.csv','r')
s=open('stflg.csv','r')
ar=csv.reader(a)
sr=csv.reader(s)
admin=[]
staff=[]
for i in ar:
    admin.append(i)
for i in sr:
    staff.append(i)
print(admin)
print(staff)

print("WELCOME TO CANTEEN MANAGEMENT SYSTEM")


def viewhistory(admin,staff,k):
    file=k+'.csv'
    s=open(file,'r')
    csvr=csv.reader(s)
    l=[]
    for i in csvr:
        print(i)
        l.append(i)
    i=1
    t=0
    while i<len(l):
        k=int(l[i][-1])
        t=t+k
        i=i+1
    print('NET TOTAL=',t)
    s.close()
    staffperms(admin,staff,k)



def checkint(k):
    if k.isdigit()==True:
        return int(k)
    else:
        return 100
    
# for admin to get order details of staffs
def orderhistory(admin,staff):
    k=str(input('enter the staff ID to display order history\n'
                ' press B to return back to the previous menu\n'
                'press E to exit app'))
    if k in 'Ee':
        exitapp(admin,staff)
    if k in 'Bb':
        adminperms(admin,staff)
        
    file=k+'.csv'
    if (os.path.exists(file) and os.path.isfile(file)):
        s=open(file,'r')
        csvr=csv.reader(s)
        l=[]
        for i in csvr:
            print(i)
            l.append(i)
        i=1
        t=0
        while i<len(l):
            k=int(l[i][-1])
            t=t+k
            i=i+1
        print('NET TOTAL=',t)
        a=input('do you want to reset it?\n''press Y for yes and N for no')
        if a in 'Yy':
            l1=l[0]
            with open(file,'w+',newline='') as f:
                csvw=csv.writer(f)
                csvw.writerow(l1)
            print('RESET DONE!!')
        s.close()
    else:
        print('ID NOT AVAILABLE')
    orderhistory(admin,staff)
        
# For staff to order food     
def placeorder(admin,staff,k):
    m=open('menu.csv','r')
    mr=csv.reader(m)
    menu1=[]
    for i in mr:
        menu1.append(i)
    print('MENU:-')
    print("['SL.NO.','ITEM NAME','PRICE']")
    for i in menu1:
        print(i)
    filename=k+'.csv'
    rows=[]
    ans='y'
    while ans=='y':
        a1=input('enter the sl no. of item to be ordered')
        a=str(checkint(a1))
        z=int(a)
        if z<=len(menu1):
            for i in menu1:
                if i[0]==a:
                    r=int(i[-1])
                    d=i[-2]
            b=str(int(input('enter the quantity')))
            c=str(r*int(b))
            l=[d,b,c]
            rows.append(l)
        else:
            print('invalid SL NO.')
            placeorder(admin,staff,k)
        ans=(input('Do you want to order another item?\n'
                   'press Y for yes and N for no')).lower()
    f=open(filename,'r')
    csvr=csv.reader(f)
    f1=[]
    for i in csvr:
        f1.append(i)
    f.close()
    m.close()
    f2=f1+rows
    with open(filename,'w+',newline='') as f:
        csvw=csv.writer(f,delimiter=',')
        csvw.writerows(f2)
    print('order placed successfully')
    staffperms(admin,staff,k)
    
    
def digits(a):
    c=0
    while a!=0:
        c=c+1
        a=a//10
    return c             
            
# For displaying menu            
def displaymenu(admin,staff,k):
    m=open('menu.csv','r')
    mr=csv.reader(m)
    menu1=[]
    for i in mr:
        menu1.append(i)
    print('MENU:-')
    print("['SL.NO.','ITEM NAME','PRICE']")
    for i in menu1:
        print(i)
    staffperms(admin,staff,k)
    
# For staff    
def staffperms(admin,staff,k):
    print("STAFF PERMS")
    ch1=input('press 1 to display menu\n'
              'press 2 to place order\n'
              'press 3 to view your order history\n'
              'press 4 to return back to the previous menu\n'
              'press 5 to exit the app')
    ch=checkint(ch1)
    if ch==1:
        displaymenu(admin,staff,k)
    elif ch==2:
        placeorder(admin,staff,k)
    elif ch==3:
        viewhistory(admin,staff,k)
    elif ch==4:
        three(admin,staff)
    elif ch==5:
        exitapp(admin,staff)
    else:
        print('invalid choice')
        staffperms(admin,staff,k)

#For exit out from app        
def exitapp(admin,staff):
    print('THANK YOU! VISIT AGAIN!!❤')
    os._exit(0)
#For deleting menu
def deleteitem(admin,staff):
    m=open('menu.csv','r')
    mr=csv.reader(m)
    menu1=[]
    for i in mr:
        menu1.append(i)
    print('MENU:-')
    print("['SL.NO.','ITEM NAME','PRICE']")
    for i in menu1:
        print(i)
    k=int(menu1[-1][0])
    
    l=[]
    for i in range(1,k+1):
        l.append(str(i))
    l1=[]
    ans='y'
    while ans=='y':
        a1=input('enter the sl no. of item to be deleted')
        a=str(checkint(a1))
        k=int(a)
        if k<=len(menu1):
            for i in menu1:
                if i[0]==a:
                    l2=i
                    l1.append(l2)
        ans=(input('Do you want to delete another item?\n'
                   'press Y for yes and N for no')).lower()
    print(l1)        
    menu2=[]
    for i in menu1:
        if i not in l1:
            menu2.append(i)
    for i in menu2:
        print(i)
    print('hello',len(menu2))
    i=0
    while i<len(menu2):
        menu2[i][0]=l[i]
        i=i+1
        
    with open("menu.csv","w+",newline='') as f:
        csvw=csv.writer(f)
        csvw.writerows(menu2)
    print("done")
    f=open('menu.csv','r')
    csvr=csv.reader(f)
    for i in csvr:
        print(i)
    f.close()
    m.close()
    editmenu(admin,staff)

# For modifying MENU    
def modifyitem(admin,staff):
    m=open('menu.csv','r')
    mr=csv.reader(m)
    menu1=[]
    for i in mr:
        menu1.append(i)
    print('MENU:-')
    for i in menu1:
        print(i)
    ans='y'
    while ans=='y':
        a1=input('enter the sl. no. of item whose price is needed yo be modified')
        a=str(checkint(a1))
        b1=input('enter the new price')
        b=str(checkint(a1))
        k=int(a)
        if k<=len(menu1):
            for i in menu1:
                if i[0]==a:
                    i[-1]=b
        else:
            print('enter valid input')
            modifyitem(admin,staff)
        ans=(input('Do you want to continue?\n'
                   'press Y for yes and N for no')).lower()
    with open("menu.csv","w+",newline='') as f:
        csvw=csv.writer(f)
        csvw.writerows(menu1)
    print("done")
    f=open('menu.csv','r')
    csvr=csv.reader(f)
    for i in csvr:
        print(i)
    f.close()
    m.close()
    editmenu(admin,staff)
    
    
#for adding items in menu card    
def additem(admin,staff):
    m=open('menu.csv','r')
    mr=csv.reader(m)
    menu1=[]
    for i in mr:
        menu1.append(i)
    print('MENU:-')
    for i in menu1:
        print(i)
    l=[]
    ans='y'
    i=1
    while ans=='y':
        a=(input('enter the item to be added')).upper()
        b=input('enter the price')
        if b.isdigit()==False:
            print('numeric digit is required')
            m.close()
            additem(admin,staff)
        else:
            b=int(b)
        k=str(i+int(menu1[-1][0]))
        l1=[k,a,b]
        l.append(l1)
        i=i+1
        ans=(input('Do you want to continue?\n'
                   'press Y for yes and N for no')).lower()
    menu2=menu1+l
    with open("menu.csv","w+",newline='') as f:
        csvw=csv.writer(f)
        csvw.writerows(menu2)
    print("done")
    f=open('menu.csv','r')
    csvr=csv.reader(f)
    for i in csvr:
        print(i)
    f.close()
    m.close()
    editmenu(admin,staff) 

# for admin to edit menu    
def editmenu(admin,staff):
    ch=int(input("press 1 to add item in menu\n"
                 "press 2 to delete item in menu\n"
                 "press 3 to change the item's price in menu\n"
                 "press 4 to return back to previous menu"))
    if ch==1:
        additem(admin,staff)
    elif ch==2:
        deleteitem(admin,staff)
    elif ch==3:
        modifyitem(admin,staff)
    elif ch==4:
        adminperms(admin,staff)
    else:
        print('invalid input')
        editmenu(admin,staff)
    
def printmenu(admin,staff):
    m=open('menu.csv','r')
    mr=csv.reader(m)
    menu1=[]
    for i in mr:
        menu1.append(i)
    print('MENU:-')
    for i in menu1:
        print(i)
    m.close()
    menu(admin,staff)
    
def menu(admin,staff):
    k1=input('Press 1 to display menu\n'
             'Press 2 to edit menu\n'
             'press 3 to return to the previous menu\n'
             'Press 4 to exit')
    k=checkint(k1)
    if k==1:
        printmenu(admin,staff)
    elif k==2:
        editmenu(admin,staff)
    elif k==3:
        adminperms(admin,staff)
    elif k==4:
        exitapp(admin,staff)
    else:
        print('select valid option')
        menu(admin,staff)
        
                  
# For deleting staff details        
def delstaff(admin,staff):
    l=[]
    ans='y'
    while ans=='y':
        a=(input('enter the id to be deleted\n''press P for return back\n''press E for exit app')).lower()
        if a=='p':
            editstaff(admin,staff)
        if a=='e':
            exitapp(admin,staff)
        b=input('enter the password of that id')
        c=0
        j=0
        for i in staff:
            if i[j]==a:
                if i[j+1]==b:
                    c=1
                    z=[a,b]
                    l.append(z)
        ans=(input('Do you want to delete another ID?\n'
                   ' Press Y for yes and N for no')).lower()
        if c==0:
            print('incorrect details')
            k=(input('press R to retry and B to return back to the previous menu')).lower()
            if k=='r':
                delstaff(admin,staff)
            elif k=='b':
                editstaff(admin,staff)
        else:
            l1=[]
            for i in staff:
                if i not in l:
                    l1.append(i)
            with open("stflg.csv","w+",newline='') as f:
                csvw=csv.writer(f)
                for i in l1:
                    csvw.writerow(i)
            file=a+'.csv'
            if (os.path.exists(file) and os.path.isfile(file)):
                os.remove(file)

            print('ID successfully deleted')
    adminperms(admin,staff)
    
# For editing staff details    
def editstaff(admin,staff):
    print('press 1 for adding staff details\n'
          'press 2 for removing staff details\n'
          'press 3 for going back to the previous menu')
    l1=input("Enter the selected option")
    l=checkint(l1)
    if l==1:
        addstaff(admin,staff)
            
    elif l==2:
        delstaff(admin,staff)

    elif l==3:
        adminperms(admin,staff)
    else:
        print('select valid option')
        editstaff(admin,staff)
        
# for admin 
def adminperms(admin,staff):
    print("ADMIN PERMS")
    print('press 1 for accessing for staff details\n'
          'press 2 for editing staff details\n'
          'press 3 to view order history of staff\n'
          'press 4 for menu\n'
          'press 5 to return back to the previous menu\n'
          'press 6 to exit app')
    n1=input("Enter the selected option")
    n=checkint(n1)
    if n==1:
        file=open("stflg.csv","r")
        csvreader=csv.reader(file)
        for row in csvreader:
            print(row)
        adminperms(admin,staff)
    elif n==2:
        editstaff(admin,staff)
    elif n==3:
        orderhistory(admin,staff)
    elif n==4:
        menu(admin,staff)
    elif n==5:
        one(admin,staff)
    elif n==6:
        exitapp(admin,staff)
    else:
        print('enter valid input')
        adminperms(admin,staff)
    
# for adding staffs               
def addstaff1(l,staff):
    l1=staff+l
    with open("stflg.csv","w+",newline='') as f:
        csvw=csv.writer(f)
        csvw.writerows(l1)
    print("done")
    f=open('stflg.csv','r')
    csvr=csv.reader(f)
    for i in csvr:
        print(i)
    f.close()
    for i in l:
        k=str(i[0])
        filename=k+'.csv'
        feilds=[['ITEM_NAME','UNIT','AMOUNT']]
        with open(filename,'w',newline='') as f:
            csvw=csv.writer(f,delimiter=',')
            csvw.writerows(feilds)
    adminperms(admin,staff)
    
def addstaff(admin,staff):
    l=[]
    ans='y'
    while ans=='y':
        a=input('Enter The Name')
        b1=input('Enter The Password')
        c1=input('Confirm The Password')
        if b1.isdigit()==True and c1.isdigit()==True:
            b=int(b1)
            c=int(c1)
            d=digits(b)
            e=digits(c)
            if d==3 and e==3:
                if b==c:
                    print('ID added successfully')
                    k=[a,b]
                    l.append(k)
                else:
                    print('both passwords are not same')
            else:
                print('length of password should be 3')
        else:
            print('give numeric password')
            addstaff(admin,staff)
        
        ans=(input('do you want to add another ID?\n'
                   'press Y for yes and N for no')).lower()
    addstaff1(l,staff)
    
# login system for staff
def three(admin,staff):
    print('please verify your id')
    k=(input('enter login id')).lower()
    z1=input('enter login password')
    z=checkint(z1)
    c=0
    l=str(z)
    for j in staff:
        i=j
        if k==i[0]:
            c=c+1
            if l==i[1]:
                c=c+1
                break
    if c!=0 and c==2:
        print('login successful')
        staffperms(admin,staff,k)
        
    else:
        print('incorrect login credentials')
        k=input('press R to retry login\n'
                'press B to return back to the previous menu')
        if k.lower()=='b':
            one(admin,staff)
        elif k.lower()=='r':
            three(admin,staff)
        else:
            print('invalid input')
            
# login system for admin    
def two(admin,staff):
    print('please verify your id')
    k=(input('enter login id')).upper()
    z=input('enter login password')
    l=str(z)
    c=0
    for i in admin:
        if k==i[0]:
            c=c+1

            if l==i[1]:
                c=c+1
    if c!=0 and c%2==0:
        print('login successful')
        adminperms(admin,staff)
    else:
        print('incorrect login credentials')
        k=input('press R to retry login\n'
                'press B to return back to the previous menu')
        if k.lower()=='b':
            one(admin,staff)
        elif k.lower()=='r':
            two(admin,staff)
        else:
            print('invalid input')
            two(admin,staff)
            
# login option     
def one(admin,staff):
    print('please select your login type')
    print('press 1 for admin\n'
          'press 2 for staff\n'
          'press 3 to exit')
    k1=input('enter your choice')
    k=checkint(k1)
    if k==1:
        two(admin,staff)
    elif k==2:
        three(admin,staff)
    elif k==3:
        exitapp(admin,staff)
    else:
        print('invalid input')
        one(admin,staff)
one(admin,staff)