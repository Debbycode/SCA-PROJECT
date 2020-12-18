## __Capstone Project - USER MANAGMENT SYSTEM (UMS)__

### STUDENT MANAGEMENT SYSTEM USING SQLITE IN PYTHON

### __INTRODUCTION__

A highly efficient method for handling multiple type of data in an organisation or business, is the Database management system. In an educational organistion for example, the admin keeps record of all students in the institution. The User Management System is a simple system developed for managing user details and for easy management of user records. 

This project aims at developing a user management system using the SQLite in python as it's database. The project enables an educational organization to maintain student's information. The system contains an administrative side from where the admin can maintain the student records easily. For example, user can order add student's name, age, course, email and username. User can also update student's data, view, delete and search student data.

Furthermore, the project file contains the python scripts (main.py(student_database.py), master.py and test.py). The scripts utilizes the standard GUI library for Python - Tkinter - that creates a pretty and simple user framework. Users will find the framework easy to navigate. Moreover, the application uses basic Python functions to generate button options, input message boxes, list and print text on the screen. 

### __DATA__

In order to program the User management system using SQLite3 database in python, the first step is to import the sqlite3 module. Following this, is to create a table in SQLite. In this projeect, We created a table student having the following attributes:

student (first_name, last_name, gender, age, email, course, username, address, contact)
(The step by step method is explained in the methodology section). To check if the table is created, We used the DB browser for SQLite to view the table. We downloaded the _studentdata.db_ file and Open file with the DB program. The table is given:

![Img0.png](attachment:Img1.png)


## __METHODOLOGY__

### __Classes and Functions Used__


 __CREATE CONNECTION__

To create a connection with SQLite which will connect us to the database for executing the SQL statements, We used the connect()function (after importing sqlite module
          
          con = sqlite3.connect("student.db")  


__CREATE TABLE__

To create a connection with SQLit that will create a database file automatically,the following code is used.  A table is created if it doesn’t already exist, and create an exception is used not to create a table, if it already exists.

        con.execute("CREATE TABLE IF NOT EXISTS student(first_name TEXT, last_name TEXT, 
        age INTEGER, email TEXT, course TEXT, username TEXT);")
        con.commit()


 __INSERT__

To insert data in a table, we used the _INSERT INTO_ student. We passed values/arguments to an INSERT statement in the execute() method . The syntax of the _INSERT_ is found in the entire _SubmitData_ class as follows:

        def insert_data(first_name, last_name, age, email, course, username):
            conn = sqlite3.connect("student.db")
            conn.execute("INSERT INTO student(first_name, last_name, age, email, course, 
            username) VALUES( '" + first_name + "', '" + last_name +
                         "', '" + age + "', '" + email + "', '" + course + "', '" + 
                         username + "' );") conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Data Saved Successfully.")

__UPDATE TABLE__

To update the table, we simply used the _UPDATE_ statement in the execute() method. Suppose that we want to update the gender of the student whose ID is 2. For updating, we will use the _UPDATE_ statement and for the student whose ID equals 2. We will use the _WHERE_ clause as a condition to select this student. The general _UpdateData_ class is given:
        
        def update():
            ...
            ...
            ...
                scon = sqlite3.connect("student.db")
                        scon.execute("UPDATE student SET first_name = '" + sfirst_name + 
                        "', 
                        last_name = '" + slast_name + "', age = '" + sage +
                                 "', email = '" + semail + "', course = '" + scourse + 
                                 "', 
                                 username = '" + susername + "' WHERE rowid = " + sid + 
                                 scon.commit()


 __DELETE TABLE__

We used the _DeleteData_ function to delete a table using the _DELETE_ statement. The syntax of the _DELETE_ statement is as follows:

         def delete():
             ...
             ...
             dcon.execute("DELETE FROM student WHERE first_name = '" + dfirst_name + 
             "';")
                dcon.commit()
                dcon.execute("VACUUM;")
                dcon.commit()



__CLOSE CONNECTION__

Once we are done with our database, we deemed it good practice to close the connection. Therefore, we closed our connection by using the close() method. To close a connection, use the connection object and call the close() method as follows:

        con.close()

### __Other Python Functions (Tkinter)__

The Tkinker is a standard GUI  for pyhton. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit. The application enable users make easy selections. To make use of the application, the Tkinker modules is imported and then the main functions are called as commands. For example, the _update_ function in the main(student_database.py) script is the _button 2_ in the master.py script(GUI):

            from tkinter import *
            import tkinter.ttk as ttk
            import tkinter.messagebox as tkMessageBox
            
    button_2 = tk.Button(mainWindow, text="Update Student Details", fg =
                'DeepPink4', command=lambda: sd.update(), padx=240, pady=25,
                activebackground='grey', activeforeground='white')
    button_2.pack()



### __How To Run Project Script__

To run this script, user must have installed Python on their PC. Then download the python scripts. After downloading the project - as zip file, follow the steps below:

Step1: Extract/Unzip the file

Step2: Locate the the project folder in (user)PC,

Step3: In the folder, open (either by double clicklinking or right-clicking mouse) and run student_database.py and master.py script. The  application will be automatically displayed after running

A script called test.py also contained in the folder is used to test code function. This script uses the __unitest__ python tester.

The Student management file includes:

- student_database.py script
- test.py, for testing the code
- SCALOGO.PNG used as logo in application

Other file are
- the report for the program
- the images used in report


### __RESULT__

The result of the code after running are as follows:

__CREATE TABLE (Image1):__
The Image GUI show that a database has been created. The GUI interface shows a student table with the required information as attributes. All student data are shown in the window(if student data have been recorded previously).

![Img1.png](attachment:Img1.png)

__INSERT STUDENT DATA (Image2):__
The image of the getting student information and inserting data into table. The GUI show a new window (Adding New Student) containing input information for new student.

![Img2.png](attachment:Img2.png)

__UPDATE STUDENT DATA (Image3):__
The image show the Update Window interface used for adding/updating existing student record. By double-clicking the selected student record, the update window pops-up. 

Note that to UPDATE student's data, the student ID e.g 1 (for the first student in list) or 2 (for second student in the list) etc, must fist be inputed in the input box

![Img3.png](attachment:Img3.png)

__DELETE STUDENT DATA (Image4):__
In the image, the _DELETE_ button on the user interface is for removing a student record from the database. A confirmation prompt is seen confirm delete option.

Note that the student's first name must be known and first be inputed to deleted the student.

![Img4.png](attachment:Img4.png)

__VIEW STUDENT DATA( Image5):__
Users can also view all student's data stored in the database. Image5 show result. From the GUI, the view button displays all student's data.

![Img5.png](attachment:Img5.png)


__SEARCH STUDENT DATA (Image5):__
The search function search student's data by inputing the student's first name. Note that the student's first name must be first inputed to serach for result. 

![Img6.png](attachment:Img6.png)

In conclusion, Images 1-4 show the result of functions used in User Management System. User can The create table for student record, insert student data, update student's data, display data of all student, deleted student's data and search student data. 



### __DISCUSSION__

Creating a User Management System may have different programming structures and methods but similar result is obtained. That is, the program can CREATE, GET, UPDATE and DELETE student data The result obtained in this project is as presented are quite satisfying.

### __CONCLUSION__

To sum up, this User Management System design can be used in an educational organisation to keep the record of student in the institution. Admin can create a student database and store information for each student. Student's information can also be updated and deleted. The program is easy to use.



```python

```


```python

```


```python

```
