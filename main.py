from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB import Database
db = Database("bom.DB")
root = Tk()
root.title("ASSET MANAGEMENT SYSTEM")
root.geometry("1920x1080+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")
Product_Name = StringVar()
Quantity= StringVar()
Serial_No = StringVar()
Part_phase = StringVar()
Procurement_Spec = StringVar()
Level = StringVar()
Comments = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Bill of Materials", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
#table details and content
lblProduct_Name = Label(entries_frame, text="Product_Name", font=("Calibri", 16), bg="#535c68", fg="white")
lblProduct_Name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtProduct_Name = Entry(entries_frame, textvariable=Product_Name, font=("Calibri", 16), width=30)
txtProduct_Name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lblQuantity = Label(entries_frame, text="Quantity", font=("Calibri", 16), bg="#535c68", fg="white")
lblQuantity.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txtQuantity = Entry(entries_frame, textvariable=Quantity, font=("Calibri", 16), width=30)
txtQuantity.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblSerial_No = Label(entries_frame, text="Serial_No", font=("Calibri", 16), bg="#535c68", fg="white")
lblSerial_No.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtSerial_No = Entry(entries_frame, textvariable=Serial_No, font=("Calibri", 16), width=30)
txtSerial_No.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblProcurement_Spec = Label(entries_frame, text="Procurement_Spec", font=("Calibri", 16), bg="#535c68", fg="white")
lblProcurement_Spec.grid(row=2, column=2, padx=10, pady=10, sticky="w")
comboProcurement_Spec = ttk.Combobox(entries_frame, textvariable=Procurement_Spec, font=("Calibri", 16), width=28, state="readonly")
comboProcurement_Spec['values'] = ("Purchased", "Modified", "Custom")
comboProcurement_Spec.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblPart_phase = Label(entries_frame, text="Part_phase", font=("Calibri", 16), bg="#535c68", fg="white")
lblPart_phase.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboPart_phase = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=Part_phase, state="readonly")
comboPart_phase['values'] = ("Design", "Prototype", "Testing", "Production", "Assembly")
comboPart_phase.grid(row=3, column=1, padx=10, sticky="w")

lblLevel = Label(entries_frame, text="Level", font=("Calibri", 16), bg="#535c68", fg="white")
lblLevel.grid(row=3, column=2, padx=10, pady=10, sticky="w")
comboLevel = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=Level, state="readonly")
comboLevel['values'] = ("1", "2", "3", "4")
comboLevel.grid(row=3, column=3, padx=10, sticky="w")
lblComments = Label(entries_frame, text=" Comments", font=("Calibri", 16), bg="#535c68", fg="white")
lblComments.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtComments = Text(entries_frame, width=85, height=5, font=("Calibri", 16))
txtComments.grid(row=5, column=0, columnspan=4, padx=10, sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    Product_Name.set(row[1])
    Quantity.set(row[2])
    Serial_No.set(row[3])
    Procurement_Spec.set(row[4])
    Part_phase.set(row[5])
    Level.set(row[6])
    txtComments.delete(1.0, END)
    txtComments.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_detail():
    if txtProduct_Name.get() == "" or txtQuantity.get() == "" or txtSerial_No.get() == "" or comboProcurement_Spec.get() == "" \
            or comboPart_phase.get() == "" or comboLevel.get() == "" or txtComments.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtProduct_Name.get(),txtQuantity.get(), txtSerial_No.get() ,comboProcurement_Spec.get() ,comboPart_phase.get(),
              comboLevel.get(), txtComments.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()

def update_detail():
    if txtProduct_Name.get() == "" or txtQuantity.get() == "" or txtSerial_No.get() == "" or comboProcurement_Spec.get() == "" \
            or comboPart_phase.get() == "" or comboLevel.get() == "" or txtComments.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtProduct_Name.get(), txtQuantity.get(), txtSerial_No.get(), comboProcurement_Spec.get(),
              comboPart_phase.get(), comboLevel.get(),
              txtComments.get( 1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_detail():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    Product_Name.set("")
    Quantity.set("")
    Serial_No.set("")
    Part_phase.set("")
    Procurement_Spec.set("")
    Level.set("")
    txtComments.delete(1.0, END)
    
#for adding buttons(4 buttons)
btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_detail, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_detail, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_detail, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8,9), style="mystyle.Treeview")
tv.heading("1", text="Prod_ID")
tv.column("1", width=3)
tv.heading("2", text="Product Name")
tv.column("2", width=15)
tv.heading("3", text="Quantity")
tv.column("3", width=5)
tv.heading("4", text="Serial_No")
tv.column("4", width=10)
tv.heading("5", text="Procurement_spec")
tv.column("5", width=20)
tv.heading("6", text="Part_phase")
tv.column("6", width=10)
tv.heading("7", text="Level")
tv.heading("8", text="Comments")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)
dispalyAll()
root.mainloop()