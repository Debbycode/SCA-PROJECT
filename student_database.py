#Importing Modules
import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox




#Connecting to SQLITE Database 
con = sqlite3.connect("student.db")




#Creating Student Table
con = sqlite3.connect("student.db")
con.execute("CREATE TABLE IF NOT EXISTS student(first_name TEXT, last_name TEXT, age INTEGER, email TEXT, course TEXT, username TEXT);")
con.commit()





#Inserting Data Into Tables Created
def insert_data(first_name, last_name, age, email, course, username):
    conn = sqlite3.connect("student.db")
    conn.execute("INSERT INTO student(first_name, last_name, age, email, course, username) VALUES( '" + first_name + "', '" + last_name +
                 "', '" + age + "', '" + email + "', '" + course + "', '" + username + "' );")
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data Saved Successfully.")


#Defining Entry labels for the Tkinter GUI Framework 
def insert():
    add_window = tk.Tk()
    add_window.title("Add Student Details")
    tk.Label(add_window).grid(row=0, column=0, columnspan=2)
    tk.Label(add_window, text="First Name:").grid(row=1, column=0)
    first_name_entry = tk.Entry(add_window, width=50)
    first_name_entry.grid(row=1, column=1, padx=25)
    tk.Label(add_window, text="Last Name:").grid(row=2, column=0)
    last_name_entry = tk.Entry(add_window, width=50)
    last_name_entry.grid(row=2, column=1, padx=25)
    tk.Label(add_window, text="Age:").grid(row=3, column=0)
    age_entry = tk.Entry(add_window, width=50)
    age_entry.grid(row=3, column=1, padx=25)
    tk.Label(add_window, text="Email Address:").grid(row=4, column=0, padx=20)
    email_entry = tk.Entry(add_window, width=50)
    email_entry.grid(row=4, column=1, padx=25)
    tk.Label(add_window, text="Course:").grid(row=5, column=0)
    course_entry = tk.Entry(add_window, width=50)
    course_entry.grid(row=5, column=1, padx=25)
    tk.Label(add_window, text="Username:").grid(row=6, column=0)
    username_entry = tk.Entry(add_window, width=50)
    username_entry.grid(row=6, column=1, padx=25)
                        
    tk.Button(add_window, text='Submit', activebackground='grey', activeforeground='white', command=lambda: submit()).grid(row=7, column=0, columnspan=2, pady=10)

#The SUBMIT button for Inserting Data to Student Table
    def submit():
        if  first_name_entry.get() == "" or last_name_entry.get() == "" or age_entry.get() == ""  or email_entry.get() == "" or course_entry.get() == "" or username_entry.get() == "" :
            messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            age = age_entry.get()
            email = str(email_entry.get())
            course = course_entry.get()
            username = str(username_entry.get())
            insert_data(first_name, last_name, age, email, course, username)
            add_window.destroy()
        add_window.mainloop()




#Viewing all Students Data Inserted to Table Created
def display():
    connn = sqlite3.connect("student.db")
    display_window = tk.Tk()
    display_window.title("Students Database")
    table = ttk.Treeview(display_window)
    table["columns"] = ("one", "two", "three", "four", "five", "six")
    table.heading("one", text="First Name")
    table.heading("two", text="Last Name")
    table.heading("three", text="Age")
    table.heading("four", text="Email")
    table.heading("five", text="Course")
    table.heading("six", text="Username")
    cursor = connn.execute("SELECT rowid,* FROM student;")
    i = 0
    for row in cursor:
        table.insert('', i, text="SCA320" + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        i = i + 1
    table.pack()
    connn.close()





#Updating Student's Information and defining Entry labels in GUI Tkinter Framework
def update():
    update_window = tk.Tk()
    update_window.title("Update Student Details")
    tk.Label(update_window, text="Select the ID of student to be Updated:").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)
    s_id = tk.Entry(update_window, width=50)
    s_id.grid(row=1, column=0, sticky="W", padx=10, columnspan=2)
    tk.Label(update_window, text="\nEnter the new values:").grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)
    tk.Label(update_window, text="First Name:").grid(row=3, column=0, sticky="W", padx=10, pady=10)
    s_first_name = tk.Entry(update_window, width=50)
    s_first_name.grid(row=3, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Last Name:").grid(row=4, column=0, sticky="W", padx=10, pady=10)
    s_last_name = tk.Entry(update_window, width=50)
    s_last_name.grid(row=4, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Age:").grid(row=5, column=0, sticky="W", padx=10, pady=10)
    s_age = tk.Entry(update_window, width=50)
    s_age.grid(row=5, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Email:").grid(row=6, column=0, sticky="W", padx=10, pady=10)
    s_email = tk.Entry(update_window, width=50)
    s_email.grid(row=6, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Course:").grid(row=7, column=0, sticky="W", padx=10, pady=10)
    s_course = tk.Entry(update_window, width=50)
    s_course.grid(row=7, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="Username:").grid(row=8, column=0, sticky="W", padx=10, pady=10)
    s_username = tk.Entry(update_window, width=50)
    s_username.grid(row=8, column=1, sticky="W", padx=10, pady=10)
    tk.Button(update_window, text="Update", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=9, column=0, padx=10, pady=10, columnspan=2)
    
#The SUBMIT button for Updating Student Data 
    def submit():
        sid = s_id.get()
        sfirst_name = s_first_name.get()
        slast_name = s_last_name.get()
        sage= s_age.get()
        semail = s_email.get()
        scourse = s_course.get()
        susername = s_username.get()
        if  s_first_name.get() == "" or s_last_name.get() == "" or s_age.get() == ""  or s_email.get() == "" or s_course.get() == "" or s_username.get() == "" :
            messagebox.showwarning('', 'Please Complete The Required Field', icon="warning")
        else:
            
            scon = sqlite3.connect("student.db")
            scon.execute("UPDATE student SET first_name = '" + sfirst_name + "', last_name = '" + slast_name + "', age = '" + sage +
                     "', email = '" + semail + "', course = '" + scourse + "', username = '" + susername + "' WHERE rowid = " + sid + ";")
            scon.commit()
            scon.close()
            messagebox.showinfo("Success", "Data Updated Successfully.")
            update_window.destroy()
        update_window.mainloop()




#Deleting Student Data  and defining Entry labels in GUI Tkinter Framework
def delete():
    delete_window = tk.Tk()
    delete_window.title("Delete Student ")
    tk.Label(delete_window, text="Enter Student Name whose details are to be removed:").grid(row=0, column=0, padx=10, pady=10)
    d_name = tk.Entry(delete_window, width=50)
    d_name.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(delete_window, text="Delete Details", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    tk.Label(delete_window).grid(row=2, column=0, columnspan=2)

#The SUBMIT button for Deleting the student Data
    def submit():
        messagebox.askquestion('', 'Are you sure you want to delete this record?', icon="warning") 
        dfirst_name = d_name.get()
        dcon = sqlite3.connect("student.db")
        dcon.execute("DELETE FROM student WHERE first_name = '" + dfirst_name + "';")
        dcon.commit()
        dcon.execute("VACUUM;")
        dcon.commit()
        dcon.close()
        messagebox.showinfo("Success", "Deleted Successfully.")
        delete_window.destroy()
    delete_window.mainloop()




#Search for  a particular Student with the firstname
def search():
    search_window = tk.Tk()
    search_window.title("Search Student Details")
    tk.Label(search_window, text="Enter the name of Student whose details are to be searched:").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    f_first_name = tk.Entry(search_window, width=50)
    f_first_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window).grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window)
    details["columns"] = ("one", "two", "three", "four", "five", "six")
    details.heading("one", text="First Name")
    details.heading("two", text="Last Name")
    details.heading("three", text="Age")
    details.heading("four", text="Email")
    details.heading("five", text="Course")
    details.heading("six", text="Username")
    
#The SUBMIT button for Searching for Student Information
    def submit():
        for row in details.get_children():
            details.delete(row)

        ffirst_name = f_first_name.get()
        fcon = sqlite3.connect("student.db")
        cursor = fcon.execute("SELECT rowid,* from student WHERE first_name = '" + ffirst_name + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="SCA320" + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5], row[6]))
            i = i + 1

        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        fcon.close()
    search_window.mainloop()


con.close()