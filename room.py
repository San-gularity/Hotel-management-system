from codecs import strict_errors
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+230+220")


        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()



        lbl_title=Label(self.root,text="ROOMBOOKING",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        img2=Image.open(r"C:\Users\sanat\Desktop\hotel_management_system\images\7d7c8afbe5f6b9bed2dd41bd71437b89.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)  #to convert high level image to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOM BOOKING DETAILS",padx=2,font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)





        lbl_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_contact.grid(row=0,column=0,sticky=W)

        enty_contach=ttk.Entry(labelframeleft,width=20,textvariable=self.var_contact,font=("arial",13,"bold"))
        enty_contach.grid(row=0,column=1,sticky=W)

        btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)


        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin,font=("arial",13,"bold"),)
        txtcheck_in_date.grid(row=1,column=1)


        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_out Date",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("arial",13,"bold"))
        txt_Check_out.grid(row=2,column=1)


        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from details")
        ide=my_cursor.fetchall()
        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_roomtype,width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Room Available",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,width=29,textvariable=self.var_roomavailable,font=("arial",13,"bold"))
        #txtRoomAvailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()
        combo_RoomNo=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),textvariable=self.var_roomavailable,width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)


        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No_Of_Days",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noofdays,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)


        lblPaid=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax",padx=2,pady=6)
        lblPaid.grid(row=7,column=0,sticky=W)
        txtPaid=ttk.Entry(labelframeleft,width=29,textvariable=self.var_paidtax,font=("arial",13,"bold"))
        txtPaid.grid(row=7,column=1)


        lblSub=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total",padx=2,pady=6)
        lblSub.grid(row=8,column=0,sticky=W)
        txtSub=ttk.Entry(labelframeleft,width=29,textvariable=self.var_actualtotal,font=("arial",13,"bold"))
        txtSub.grid(row=8,column=1)


        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)




        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)
 
        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="DELETE",command=self.deletes,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnreset.grid(row=0,column=3,padx=1)



        img3=Image.open(r"C:\Users\sanat\Desktop\hotel_management_system\images\bigstock-Hotel-Bed-1653767.jpg")
        img3=img3.resize((550,150),Image.ANTIALIAS)  #to convert high level image to low level
        self.photoimg2=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=550,height=150)

        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=200,width=860,height=260)

        lblSearchby=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room") #FFFFFFF
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        btnsearchh=Button(Table_Frame,text="SEARCH",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnsearchh.grid(row=0,column=3,padx=1)

        btnShow=Button(Table_Frame,text="SHOW ALL",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShow.grid(row=0,column=4,padx=1)

        
        
        Detail_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        Detail_table.place(x=0,y=50,width=860,height=165)


        Scroll_x=ttk.Scrollbar(Detail_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Detail_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(Detail_table,column=("contact","checkin","checkout","roomtype",
                                                    "roomavailable","meal","noOfdays","paidtax","actualtotal","total"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="contact")
        self.room_table.heading("checkin",text="checkin")
        self.room_table.heading("checkout",text="checkout")
        self.room_table.heading("roomtype",text="roomtype")
        self.room_table.heading("roomavailable",text="roomavailable")
        self.room_table.heading("meal",text="meal")
        self.room_table.heading("noOfdays",text="noOfdays")
        self.room_table.heading("paidtax",text="paidtax")
        self.room_table.heading("actualtotal",text="actualtotal")
        self.room_table.heading("total",text="total")


        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.column("paidtax",width=100)
        self.room_table.column("actualtotal",width=100)
        self.room_table.column("total",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(),
                                                                                                    self.var_meal.get(),
                                                                                                    self.var_noofdays.get(),
                                                                                                    self.var_paidtax.get(),
                                                                                                    self.var_actualtotal.get(),
                                                                                                    self.var_total.get()
                                                                                     ))
                                                                                                    
                                                                      

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:(str(es))",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6]),
        self.var_paidtax.set(row[7]),
        self.var_actualtotal.set(row[8]),
        self.var_total.set(row[9])


    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s,paidtax=%s,actualtotal=%s,total=%s where contact=%s",(
                                                                                                    self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(),
                                                                                                    self.var_meal.get(), 
                                                                                                    self.var_noofdays.get(),
                                                                                                    self.var_contact.get(),
                                                                                                    self.var_paidtax.get(),
                                                                                                    self.var_actualtotal.get(),
                                                                                                    self.var_total.get()
                                                                                                
                                                                                                     ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Updated Successully",parent=self.root)

    def deletes(self):
        deletes=messagebox.askyesno("Hotel Managemnt System","Do You Want To Delete This Customr",parent=self.root)
        if deletes>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not deletes:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        


    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)       
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
             my_cursor=conn.cursor()
             query=("select Name from customer where Mobile=%s")
             value=(self.var_contact.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()

        if row==None:
            messagebox.showerror("Error","No Number Found",parent=self.root)
        else:
            conn.commit()
            conn.close()

            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataframe.place(x=450,y=55,width=300,height=145)

            lblName=Label(showDataframe,text="Name",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)
            
            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=90,y=0)

            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            query=("select Gender from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblGender=Label(showDataframe,text="Name",font=("arial",12,"bold"))
            lblGender.place(x=0,y=30)
            
            lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl2.place(x=90,y=30)

            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            query=("select Nationality from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblnat=Label(showDataframe,text="Nationality",font=("arial",12,"bold"))
            lblnat.place(x=0,y=60)
            
            lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl3.place(x=90,y=60)


            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            query=("select email from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            lblemail=Label(showDataframe,text="Email",font=("arial",12,"bold"))
            lblemail.place(x=0,y=90)
            
            lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl4.place(x=90,y=90)

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="BreakFast" or "Lunch" or "Dinner" and self.var_roomtype.get()=="Luxury" or "Single" or "Double"):
            q1=float(300)   #BF
            q2=float(700)   #luxury
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        















































if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop