from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(name,address,phone):
    conn=psycopg2.connect(dbname="postgres", user="postgres", password="66666622",host="localhost",port = "5432",)
    cur = conn.cursor()
    query = '''INSERT INTO student(name,address,phone) VALUES (%s, %s, %s);'''
    cur.execute(query,(name,address,phone))
    print('data inserted')
    conn.commit()
    conn.close()
    search_all()

def search_byid(id):
    conn=psycopg2.connect(dbname="postgres", user="postgres", password="66666622",host="localhost",port = "5432",)
    cur = conn.cursor()
    query = '''select * from student where id=%s;'''
    cur.execute(query,(id))
    searched=cur.fetchone()
    display_search(searched)
    conn.commit()
    conn.close()

def display_search(searched):
    listbox=Listbox(frame, width=20, height=1)
    listbox.grid(row=8,column=1)
    listbox.insert(END,searched)

def search_all():
    conn=psycopg2.connect(dbname="postgres", user="postgres", password="66666622",host="localhost",port = "5432",)
    cur = conn.cursor()
    query = '''select * from student;'''
    cur.execute(query)
    row=cur.fetchall()
    listbox=Listbox(frame,width=20, height=5)
    listbox.grid(row=9,column=1)
    for i in row:
        listbox.insert(END, i)



canvas = Canvas(root, height=480,width=900)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relheight=0.8, relwidth=0.8)

label = Label(frame,text='Add Data')
label.grid(row=0,column=1)

label = Label(frame,text='Name')
label.grid(row=1,column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text='Address')
label.grid(row=2,column=0)
entry_add = Entry(frame)
entry_add.grid(row=2,column=1)

label=Label(frame, text = "Phone")
label.grid(row=3,column = 0)
entry_ph=Entry(frame)
entry_ph.grid(row=3,column=1)

button = Button(frame, text="Add", command=lambda: get_data(entry_name.get(), entry_add.get(), entry_ph.get()))
button.grid(row=4,column=1)

label=Label(frame, text = "Search by ID")
label.grid(row=7,column = 0)
entr_id=Entry(frame)
entr_id.grid(row=7,column=1)

button = Button(frame,text="Search", command= lambda: search_byid(entr_id.get()))
button.grid(row=7,column=2)
search_all()



root.mainloop()