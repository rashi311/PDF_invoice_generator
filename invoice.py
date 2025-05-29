from  tkinter import *
from fpdf import FPDF
window=Tk()
window.title("invoice generator")
invoice_items=[]
medicines={"Medicine A":10,
           "Medicine B":20,
           "Medicine C":15,
           "Medicine D":30}
def add_medicine():
    selected_medicine=medicine_listbox.get(ANCHOR)
    quantity=int(quantity_entry.get())
    price=medicines[selected_medicine]
    item_total=price*quantity
    invoice_items.append((selected_medicine,quantity,item_total))
    total_amount_entry.delete(0,END)
    total_amount_entry.insert(END,str(calculate_total()))
    update_invoice_text()

def calculate_total():
    total=0.0
    for item in invoice_items:
        total=total+item[2] 
    return total       

def update_invoice_text():
    invoice_text.delete(1.0,END)  
    for item in invoice_items:
        invoice_text.insert(END,f"Medicine : {item[0]},Quantity : {item[1]},Total : {item[2]}\n")  

def generate_invoice():
    customer_name=customer_name_entry.get() 
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica",size=12)
    pdf.cell(0,10,txt="Invoice",new_x="LMARGIN",new_y="NEXT",align="C")       
    pdf.cell(0,10,txt="Customer : "+customer_name,new_x="LMARGIN",new_y="NEXT",align="L")  
    pdf.cell(0,10,txt="",new_x="LMARGIN",new_y="NEXT") 

    for item in invoice_items:
        medicine_name,quantity,item_total=item
        pdf.cell(0,10,txt=f"Medicine : {medicine_name},Quantity : {quantity},Total : {item_total}",new_x="LMARGIN",new_y="NEXT",align="C")

    pdf.cell(0,10,txt=f"Total : "+str({calculate_total()}),new_x="LMARGIN",new_y="NEXT",align="L")  
    pdf.output("invoice_customer.pdf")        
     

medicine_label=Label(window,text="Medicine : ")
medicine_label.pack()

medicine_listbox=Listbox(window,selectmode=SINGLE)
for medicine in medicines:
    medicine_listbox.insert(END,medicine)
medicine_listbox.pack()

quantity_label=Label(window,text="Quantity")
quantity_label.pack()

quantity_entry=Entry(window)
quantity_entry.pack()

add_button=Button(window,text="Add Medicine",command=add_medicine)
add_button.pack()

total_amount_label=Label(window,text="Total amount")
total_amount_label.pack()

total_amount_entry=Entry(window)
total_amount_entry.pack()

customer_label=Label(window,text="Customer name ")
customer_label.pack()

customer_name_entry=Entry(window)
customer_name_entry.pack()

generate_button=Button(window,text="Generate Invoice",command=generate_invoice)
generate_button.pack()

invoice_text=Text(window,height=10,width=50)
invoice_text.pack()



window.mainloop()