import sqlite3
import tkinter
try:
    cnt=sqlite3.connect('d:/shop.db')
    print("opened database successfully!")
except:
    print("Error!")
islogin=False
#-------------------------------create users table-----------------------------
##query='''CREATE TABLE users
##    (ID INTEGER PRIMARY KEY,
##    user CHAR(25) NOT NULL,
##    password CHAR(25) NOT NULL,
##    addr CHAR(50) NOT NULL
##    )'''
##cnt.execute(query)
##cnt.close()

#-------------------------------insert date to users table----------------------

##query='''INSERT INTO users (user,password,addr)
##    VALUES ("admin","123456789","rasht")'''
##cnt.execute(query)
##cnt.commit()
##cnt.close()
#------------------------------------------functions---------------------------
def login():
    user=txt_user.get()
    pas=txt_pass.get()
    global islogin

    query='''SELECT id FROM  users WHERE user=? AND password=?'''
    result=cnt.execute(query,(user,pas))
    rows=result.fetchall()
    
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    if(len(user)==0):
        btn_delete.configure(state="disabled")
        btn_logout.configure(state="disabled")
        lbl_msg.configure(text="Please enter a right username",fg="red")
        return
    islogin=True
    btn_login.configure(state="disabled")
    btn_logout.configure(state="normal")
    btn_delete.configure(state="normal")
    lbl_msg.configure(text="welcome to your account!",fg="green")
#------------------------------------------------------------------------------
def logout():
    user3=txt_user.get()
    pas3=txt_pass.get()
    query='''SELECT id FROM  users WHERE user=? AND password=?'''
    result=cnt.execute(query,(user3,pas3))
    rows=result.fetchall()
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    btn_login.configure(state="normal")
    btn_logout.configure(state="disabled")
    lbl_msg.configure(text="Log out done!",fg="green")
#------------------------------------------------------------------------------
def submit():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
#------------------------------------------win2---------------------------------
    win2=tkinter.Toplevel(win)
    win2.geometry("300x300")
    
    lbl_user2=tkinter.Label(win2,text="Username ",font=('arial',10, 'bold'))
    lbl_user2.pack()

    txt_user2=tkinter.Entry(win2,width=15,insertwidth=1, bg='linen')
    txt_user2.pack()

    lbl_pass2=tkinter.Label(win2,text="Password ",font=('arial',10, 'bold'))
    lbl_pass2.pack()

    txt_pass2=tkinter.Entry(win2,width=15,insertwidth=1, bg='linen')
    txt_pass2.pack()

    lbl_addr=tkinter.Label(win2,text="Address ",font=('arial',10, 'bold'))
    lbl_addr.pack()

    txt_addr=tkinter.Entry(win2,width=15,insertwidth=1, bg='linen')
    txt_addr.pack()

    lbl_msg2=tkinter.Label(win2,text="",font=('arial',10, 'bold'))
    lbl_msg2.pack()

    btn_sub2=tkinter.Button(win2,text="Submit",command=sub2,bd=6,font=('arial',10, 'bold'),fg="green")
    btn_sub2.pack(pady=15)
    
    win2.mainloop()
#-------------------------------------------------------------------------
def sub2():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
    
    user2=txt_user2.get()
    pas2=txt_pass2.get()
    addr=txt_addr.get()
    
    query1='''SELECT id FROM users WHERE user=?'''
    result=cnt.execute(query1,(user2,))
    rows=result.fetchall()
    if(len(user2)==0):
        lbl_msg2.configure(text="Please enter username",fg="red")
        return
    if(len(pas2)==0):
        lbl_msg2.configure(text="Please enter password",fg="red")
        return
    for item in rows:
        if(user2 in rows):
            lbl_msg2.configure(text="This username is alredy taken")
            return
    if(len(pas2)<8):
        lbl_msg2.configure(text="password lenght should be at least 8 chars!!",fg="red")
        return
    if(len(rows)!=0):
        lbl_msg2.configure(text="This username is already taken!!",fg="red")
        return
   
    query2='''INSERT INTO users(user,password,addr)
        VALUES(?,?,?)'''
    cnt.execute(query2,(user2,pas2,addr))
    cnt.commit()
    # btn_sub2.configure(state="disabled")
    lbl_msg2.configure(text="Submit done!!",bd=6,font=('arial',10, 'bold'),fg="blue")
#------------------------------------------------------------------------------  

def delete():
    global user
    global pas
    global islogin
    global lbl_msg3
    win3=tkinter.Toplevel(win)
    win3.geometry("200x200")
    lbl_msg=tkinter.Label(win3,text="Are you sure to delete account?",font=('arial',9, 'bold'))
    lbl_msg.pack()

    btn_yes=tkinter.Button(win3,text="Yes",command=yes,bd=6,font=('arial',10, 'bold'),bg="red")
    btn_yes.pack(pady=10)

    btn_no=tkinter.Button(win3,text="No",command=no,bd=6,font=('arial',10, 'bold'),fg="red")
    btn_no.pack(pady=10)

    lbl_msg3=tkinter.Label(win3,text="")
    lbl_msg3.pack()

def yes():
    global lbl_msg3
    global user
    global pas
    global islogin
    if(islogin==True):
        query='''Delete FROM users WHERE user=? AND password=?'''
        cnt.execute(query,(user,pas))
        cnt.commit()
        btn_login.configure(state="normal")
        btn_delete.configure(state="disable")
        btn_logout.configure(state="disable")
        lbl_msg3.configure(text="your account has been deleted successfully",fg="green")
        
def no():
    global lbl_msg3
    lbl_msg3.configure(text="activity canceled",fg="red")
    return


    #-----------------------------------------Main---------------------------------
    
win=tkinter.Tk()
win.geometry("400x300")

lbl_user=tkinter.Label(text="Username ",font=('arial',10, 'bold'))
lbl_user.pack()

txt_user=tkinter.Entry(width=25,insertwidth=1, bg='linen')
txt_user.pack()

lbl_pass=tkinter.Label(text="Password ",font=('arial',10, 'bold'))
lbl_pass.pack()

txt_pass=tkinter.Entry(width=25,insertwidth=1, bg='linen')
txt_pass.pack()

lbl_msg=tkinter.Label(text="",font=('arial',10, 'bold'))
lbl_msg.pack()



btn_login=tkinter.Button(text="Log in",command=login,bd=6,font=('arial',10, 'bold'),fg="blue")
btn_login.pack(pady=5)

btn_logout=tkinter.Button(text="Log out",command=logout,bd=6,font=('arial',10, 'bold'),fg="red")
btn_logout.pack(pady=5)


btn_submit=tkinter.Button(text="Submit",command=submit,bd=6,font=('arial',10, 'bold'),fg="green")
btn_submit.pack(pady=5)

btn_delete=tkinter.Button(text="Delete",command=delete,bd=6,font=('arial',10, 'bold'),fg="red")
btn_delete.pack(pady=5)



win.mainloop()