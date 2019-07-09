"""
                                        A program that stores this book information:

                                                        Title, Author
                                                        Year, ISBN


                                                        User can:

                                                    View all records
                                                    Search an entry
                                                    Add entry
                                                    Update entry
                                                    Delete
                                                    Close application

"""


from tkinter import *
from backend import Database

database=Database("books.db")

def getSelectedRow(event):
    try:
        global selectedTuple
        index=list1.curselection()[0]
        selectedTuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selectedTuple[1])
        e2.delete(0,END)
        e2.insert(END,selectedTuple[2])
        e3.delete(0,END)
        e3.insert(END,selectedTuple[3])
        e4.delete(0,END)
        e4.insert(END,selectedTuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END,row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selectedTuple[0])

def update_command():
    database.update(selectedTuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

window=Tk()

window.title("LibData")

"""                             For window to open in full screen mode
width_value=window.winfo_screenwidth()
height_value=window.winfo_screenheight()
window.geometry(f"{width_value}x{height_value}+0+0")

"""

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6,sticky="ns")

sb2=Scrollbar(window,orient=HORIZONTAL)
sb2.grid(row=8,column=0,columnspan=2,sticky="ew")

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)

list1.bind('<<ListboxSelect>>',getSelectedRow)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search All",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
