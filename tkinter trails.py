from tkinter import *

box=Tk()

box.title("Secure shell")
box.geometry("300x300")
text=Label(box,text="Password Analyzer")
text.pack()
t1=Label(box,text="Username: ").place(x=80,y=50)
e1=Entry(box,width=20)
e1.place(x=80,y=70)
t2=Label(box,text="Password: ").place(x=80,y=100)
e2=Entry(box,width=20)
e2.place(x=80,y=120)

def press():

    z=Label(box,text=e1.get()+"hi there ").place(x=80,y=180)
    password = e2.get()
    k = str.isalpha(password)
    q = str.isdigit(password)
    l=str.islower(password)
    u=str.isupper(password)


    if " " in password:
        f=Label(box,text="no spaces allowed").place(x=20,y=240)
    elif (">" or "<" ) in password:
        Label(box,text="Use of special characters like '>' or '<' is not allowed").place(x=20,y=240)
    elif len(password) >= 12 and ('!' in password or '@' in password or '#' in password or '$' in password or '%' in password or '^' in password or '&' in password or '*' in password)\
            and k==False and q==False and l==False and u==False:
        f=Label(box,text="your password is secure").place(x=20,y=240)

    elif k == True :
        f=Label(box,text="you have made use of only letters make sure you"
                         " use atleast 1 special character and numbers").place(x=20,y=240)
    elif q==True:
        f=Label(box,text="you have made use of only numbers, make sure you use "
                         "letters and atleast 1 special character").place(x=20,y=240)
    elif l==True:
        f=Label(box,text="Make sure to use atleast one upper case letter").place(x=20,y=240)
    elif u==True:
        f=Label(box,text="Make sure to use atleast one lower case letter").place(x=20,y=240)
    elif len(password) < 12:
        f=Label(box,text="please verify if you have 12 or more characters in your password").place(x=20,y=240)


'''z1=e1.get()
z2=e2.get()'''s

'''def clear():
    f.destroy()'''
b1=Button(box,text="Submit",width=15,command=press).place(x=80,y=150)
'''b2=Button(box,text="Reset",width=15,command=clear).place(x=80,y=200)'''

box.mainloop()