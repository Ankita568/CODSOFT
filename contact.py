from tkinter import *
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.geometry('600x500')
root.config(bg='#f0f8ff')
root.title('Contact Book')
root.resizable(0, 0)

# Sample contact list
contactlist = [
    ['Ankita', '35487734'],
    ['Pooja', '87755098'],
    ['Neeraj', '78945614'],
    ['Yogita', '58745246'],
    ['Shubhangini', '5846975'],
    ['Ria', '5647892'],
    ['Tanuja', '89685320'],
    ['Anchal', '98564785'],
    ['Ayushi', '85967412']
]

Name = StringVar()
Number = StringVar()

# Frame and scrollbar for the listbox
frame = Frame(root)
frame.pack(side=RIGHT, padx=10, pady=30)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Arial', 14), bg="#e6f7ff", width=20, height=12, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please select a contact")
        return None
    return int(select.curselection()[0])

def AddContact():
    if Name.get() and Number.get():
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully added new contact")
    else:
        messagebox.showerror("Error", "Please fill in the information")

def UpdateDetail():
    selected_index = Selected()
    if selected_index is not None:
        if Name.get() and Number.get():
            contactlist[selected_index] = [Name.get(), Number.get()]
            Select_set()
            EntryReset()
            messagebox.showinfo("Confirmation", "Successfully updated contact")
        else:
            messagebox.showerror("Error", "Please fill in the information")

def EntryReset():
    Name.set('')
    Number.set('')

def Delete_Entry():
    selected_index = Selected()
    if selected_index is not None:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[selected_index]
            Select_set()

def VIEW():
    selected_index = Selected()
    if selected_index is not None:
        NAME, PHONE = contactlist[selected_index]
        Name.set(NAME)
        Number.set(PHONE)

def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

Select_set()

# UI Elements
Label(root, text='Name', font=("Arial", 18, "bold"), bg='#f0f8ff').place(x=30, y=30)
Entry(root, textvariable=Name, width=20, font=('Arial', 14)).place(x=200, y=30)
Label(root, text='Contact No.', font=("Arial", 18, "bold"), bg='#f0f8ff').place(x=30, y=80)
Entry(root, textvariable=Number, width=20, font=('Arial', 14)).place(x=200, y=80)

Button(root, text="ADD", font='Arial 14 bold', bg='#87ceeb', command=AddContact, width=10).place(x=30, y=140)
Button(root, text="EDIT", font='Arial 14 bold', bg='#87ceeb', command=UpdateDetail, width=10).place(x=200, y=140)
Button(root, text="DELETE", font='Arial 14 bold', bg='#87ceeb', command=Delete_Entry, width=10).place(x=30, y=200)
Button(root, text="VIEW", font='Arial 14 bold', bg='#87ceeb', command=VIEW, width=10).place(x=200, y=200)
Button(root, text="RESET", font='Arial 14 bold', bg='#87ceeb', command=EntryReset, width=10).place(x=30, y=260)
Button(root, text="EXIT", font='Arial 14 bold', bg='#ff6347', command=EXIT, width=10).place(x=200, y=260)

root.mainloop()
