#BLL::
import pickle
class Customer:
    cuslist=[]
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mobile_no=""
    def addCustomer(self):
        Customer.cuslist.append(self)
        Customer.savetoPickle()
    def SearchCustomer(self,id):
        for e in Customer.cuslist:
            if e.id==self.id:
                self.name=e.name
                self.id=e.id
                self.address=e.address
                self.mobile_no=e.mobile_no
    def DeleteCustomer(self,id):
        for e in Customer.cuslist:
            if e.id==self.id:
                Customer.cuslist.remove(e)
                Customer.savetoPickle()

    def ModifyCustomer(self,id,name,address,mobile_no):
        for e in Customer.cuslist:
            if e.id==self.id:
                e.name=self.name
                e.address=self.address
                e.mobile_no=self.mobile_no
                Customer.savetoPickle()
    @staticmethod
    def savetoPickle():
        f = open("impo.pkl", "wb")
        pickle.dump(Customer.cuslist, f)
        f.close()
    @staticmethod
    def loadfromPickle():
        f = open("impo.pkl", "rb")
        Customer.cuslist = pickle.loads(f)
        f.close()



#     def convtoDic(obj):
#         return obj.__dict__
#     def savetoPickle():
#         f=open("e://impo.txt","w")
#         json.dump(Customer.cuslist,f,default=Customer.convtoDic)
#         f.close()
#     def convtoObj(d):
#         cus=Customer()
#         for k,v in d.items():
#             cus.__setattr__(k,v)
#         return cus
#
#     def loadfromJson():
#         f=open("e://impo.txt","r")
#         Customer.cuslist=json.load(f,object_hook=Customer.convtoObj)
# #FUNCTION
def btn_click1():
    try:
        cus=Customer()
        cus.id=var_id.get()
        cus.name=var_name.get()
        cus.address=var_address.get()
        cus.mobile_no=var_Mobile_no.get()
        cus.addCustomer()
        tkinter.messagebox.showinfo("Success", "Customer Added Successfully")
    except Exception as ae:
         tkinter.messagebox.showerror("ERROR",ae)
def btn_click2():
    try:
        cus=Customer()
        cus.id=var_id.get()
        cus.SearchCustomer(cus.id)
        var_name.set(cus.name)
        var_address.set(cus.address)
        var_Mobile_no.set(cus.mobile_no)
        tkinter.messagebox.showinfo("Success", "Customer Search Successfully")

    except Exception as ae:
        tkinter.messagebox.showerror("ERROR", ae)

def btn_click3():
    try:
        cus=Customer()
        cus.id=var_id.get()
        cus.DeleteCustomer(cus.id)
        tkinter.messagebox.showinfo("Success", "Customer Delete Successfully")
    except Exception as ae:
        tkinter.messagebox.showerror("Error",ae)

def btn_click4():
    try:
        cus=Customer()
        cus.id=var_id.get()
        cus.name=var_name.get()
        cus.address=var_address.get()
        cus.mobile_no=var_Mobile_no.get()
        cus.ModifyCustomer(cus.id,cus.name,cus.address,cus.mobile_no)
        tkinter.messagebox.showinfo("Sucess","Customer Modify Successfully")
    except Exception as we:
        tkinter.messagebox.showerror("Error",we)
def btn_click5():
    newWindow = tkinter.Toplevel()
    lbl1 = tkinter.Label(master=newWindow, text="New Label")
    rowno = 0
    columnno = 0
    cus = Customer()
    #Code for Header
    for e in cus.__dict__.items():
        lbl = tkinter.Label(master=newWindow, text=e[0], width=10)
        lbl.grid(row=rowno, column=columnno)
        columnno += 1



    #Code for Data
    rowno += 1
    for newCus in Customer.cuslist:
        columnno = 0
        for e in newCus.__dict__.items():
            lbl = tkinter.Label(master=newWindow, text=e[1], width=10)
            lbl.grid(row=rowno, column=columnno)
            columnno += 1
        rowno += 1
import tkinter
import PIL
from PIL import Image,ImageTk
import tkinter.messagebox
root=tkinter.Tk()
root.title("CUSTOMER MANAGEMENT SYSTEM")
img_load=Image.open("CMS11.png")
img_load=img_load.resize((root.winfo_screenwidth(),root.winfo_screenheight()),Image.ANTIALIAS)
img_png=ImageTk.PhotoImage(img_load)
label_1=tkinter.Label(master=root,image=img_png)
label_1.img=img_png
label_1.pack(side='top',expand=True,fill='both')
# print(root.winfo_screenwidth())
# print(root.winfo_screenheight())
#label
label_w=tkinter.Label(master=label_1,text="Customer Id",width=24)
label_w.grid(row=0,column=0,padx=10,pady=10,columnspan=2)
label_2=tkinter.Label(master=label_1,text="Customer Name",width=24)
label_2.grid(row=1,column=0,padx=10,pady=10,columnspan=2)
label_3=tkinter.Label(master=label_1,text="Customer Address",width=24)
label_3.grid(row=2,column=0,padx=10,pady=10,columnspan=2)

label_4=tkinter.Label(master=label_1,text="Customer Mobile_No",width=24)
label_4.grid(row=3,column=0,padx=10,pady=10,columnspan=2)
#Entry
var_id=tkinter.IntVar()
var_id.set('')
txt_1=tkinter.Entry(master=label_1,textvariable=var_id)
txt_1.grid(row=0,column=2,padx=10,pady=10,columnspan=2)
var_name=tkinter.StringVar()
txt_2=tkinter.Entry(master=label_1,textvariable=var_name)
txt_2.grid(row=1,column=2,padx=10,pady=10,columnspan=2)
var_address=tkinter.StringVar()
txt_3=tkinter.Entry(master=label_1,textvariable=var_address)
txt_3.grid(row=2,column=2,padx=10,pady=10,columnspan=2)
var_Mobile_no=tkinter.StringVar()
txt_4=tkinter.Entry(master=label_1,textvariable=var_Mobile_no)
txt_4.grid(row=3,column=2,padx=10,pady=10,columnspan=2)
#Button::
btn_1=tkinter.Button(master=label_1,text="Add",width=10,bg='red',command=btn_click1)
btn_1.grid(row=4,column=1,padx=8,pady=8)

btn_2=tkinter.Button(master=label_1,text="Search",width=10,bg='red',command=btn_click2)
btn_2.grid(row=4,column=2,padx=8,pady=8)

btn_3=tkinter.Button(master=label_1,text="Modify",width=10,bg='red',command=btn_click4)
btn_3.grid(row=5,column=1,padx=8,pady=8)

btn_3=tkinter.Button(master=label_1,text="Delete",width=10,bg='red',command=btn_click3)
btn_3.grid(row=5,column=2,padx=8,pady=8)


btn_4=tkinter.Button(master=label_1,text="Display All Customers",width=20,bg='red',command=btn_click5)
btn_4.grid(row=6,column=1,padx=8,pady=8)
root.mainloop()
