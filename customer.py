from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1300x550+230+220")



        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()
        

        
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        img2=Image.open(r"C:\Users\sanat\Desktop\hotel_management_system\images\7d7c8afbe5f6b9bed2dd41bd71437b89.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)  #to convert high level image to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("arial",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)



        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref,font=("arial",13,"bold"),state="readonly")
        enty_ref.grid(row=0,column=1)


        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("arial",13,"bold"),)
        txtcname.grid(row=1,column=1)


        lblmname=Label(labelframeleft,font=("arial",12,"bold"),text="Mother Name",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mother,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)


        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        lblPostCode=Label(labelframeleft,font=("arial",12,"bold"),text="PostCode",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,width=29,textvariable=self.var_post,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)


        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)


        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)


        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)


        lblIdProof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)
        
        combo_Idproof=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Idproof["value"]=("adhar","DrivingLicence","Passport","Other")
        combo_Idproof.current(0)
        combo_Idproof.grid(row=8,column=1)


        lblIdnumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number",padx=2,pady=6)
        lblIdnumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)


        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)


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



        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",padx=2,font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchby=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lblSearchby.grid(row=0,column=0,sticky=W)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Moblie","Ref")
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
        Detail_table.place(x=0,y=50,width=860,height=350)


        Scroll_x=ttk.Scrollbar(Detail_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Detail_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(Detail_table,column=("Ref","Name","Mother","Gender","Post","Mobile",
                                                            "email","Nationality","IdProof","IdNumber","Address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_Details_Table.xview)
        Scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("Ref",text="REFER NO")
        self.Cust_Details_Table.heading("Name",text="NAME")
        self.Cust_Details_Table.heading("Mother",text="MOTHER NAME")
        self.Cust_Details_Table.heading("Gender",text="GENDER")
        self.Cust_Details_Table.heading("Post",text="POSTCODE")
        self.Cust_Details_Table.heading("Mobile",text="MOBILE")
        self.Cust_Details_Table.heading("email",text="MAIL")
        self.Cust_Details_Table.heading("Nationality",text="NATIONALITY")
        self.Cust_Details_Table.heading("IdProof",text="ID PROOF")
        self.Cust_Details_Table.heading("IdNumber",text="ID NUMBER")
        self.Cust_Details_Table.heading("Address",text="ADDRESS")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("Ref",width=100)
        self.Cust_Details_Table.column("Name",width=100)
        self.Cust_Details_Table.column("Mother",width=100)
        self.Cust_Details_Table.column("Gender",width=100)
        self.Cust_Details_Table.column("Post",width=100)
        self.Cust_Details_Table.column("Mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("IdProof",width=100)
        self.Cust_Details_Table.column("IdNumber",width=100)
        self.Cust_Details_Table.column("Address",width=100)
        

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        



    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_ref.get(),
                                                                                                    self.var_cust_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_id_proof.get(),
                                                                                                    self.var_id_number.get(),
                                                                                                    self.var_address.get()
                                                                      ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning","Something went wrong:(str(es))",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_row=self.Cust_Details_Table.focus()
        contents=self.Cust_Details_Table.item(cursor_row)
        row=contents["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10]) 

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,Post=%s,Mobile=%s,email=%s,Nationality=%s,IdProof=%s,IdNumber=%s,Address=%s where Ref=%s",(
                                                                                                    self.var_cust_name.get(),
                                                                                                    self.var_mother.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_post.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_nationality.get(),
                                                                                                    self.var_id_proof.get(),
                                                                                                    self.var_id_number.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_ref.get(),
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
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not deletes:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
        
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="saianil@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close() 










                                                                                        






















        

































if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop







