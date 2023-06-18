from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+230+220")


        lbl_title=Label(self.root,text="ROOMBOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        img2=Image.open(r"C:\Users\sanat\Desktop\hotel_management_system\images\7d7c8afbe5f6b9bed2dd41bd71437b89.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)  #to convert high level image to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="NEW ROOM ADD",padx=2,font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=540,height=350)


        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        enty_floor.grid(row=0,column=1,sticky=W)


        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomno=StringVar()
        enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=20,font=("arial",13,"bold"))
        enty_RoomNo.grid(row=1,column=1,sticky=W)


        self.var_roomtype=StringVar()
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        enty_RoomType=ttk.Entry(labelframeleft,width=20,textvariable=self.var_roomtype,font=("arial",13,"bold"))
        enty_RoomType.grid(row=2,column=1,sticky=W)


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
 
        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="DELETE",command=self.deletes,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=3,padx=1)


        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=600,y=55,width=600,height=350)
        
        Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype",),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="floor")
        self.room_table.heading("roomno",text="roomno")
        self.room_table.heading("roomtype",text="roomtype")
      


        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                                    self.var_floor.get(),
                                                                                                    self.var_roomno.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    
                                                                                     ))
                                                                                                    
                                                                      

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:(str(es))",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,events=""):
        cursor_row=self.room_table.focus()
        contents=self.room_table.item(cursor_row)
        row=contents["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])

    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Floor Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomno=%s,roomtype=%s",(
                                                                                                    self.var_floor.get(),
                                                                                                    self.var_roomno.get(),
                                                                                                    self.var_roomtype.get()
                                                                                                
                                                                                                     ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Updated Successully",parent=self.root)


    def deletes(self):
        deletes=messagebox.askyesno("Hotel Managemnt System","Do You Want To Delete This Room",parent=self.root)
        if deletes>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not deletes:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")
        
                


















































if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop


