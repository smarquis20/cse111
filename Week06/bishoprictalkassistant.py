"""
Author: Shaun Marquis

Purpose: This program allows a member of the bishopric to view who has spoken and will create a view
of members who haven't spoken yet or if they have spoken it will provide the date and number of months 
since the last time they spoke.  This will also track who is assigned to speak for the current month
and the topic they are assigned.
"""
import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
import mysql.connector
from datetime import datetime
from dateutil import parser

#Connect string to connect to the project mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="tiffanyspringsward"
)

#Sets todays date to a variable in format of 2024-06-05
cur_date = datetime.today().strftime('%Y-%m-%d')

#Allows date util to do math on dates
date1 = parser.parse(cur_date)

#Main function that creates the Main window and tabbed headings
def main():
    global colors
    window = ttk.Window(themename="darkly")
    window.geometry('1600x900')
    window.title("Bishopric Speaking Assistant")
    window.place_window_center()
    colors = window.style.colors

    #Notebook creates the tabs at the top of the program and allows to switch between views
    notebook = ttk.Notebook(window)
    search_member_tab = ttk.Frame(notebook, bootstyle=INFO)
    populate_search_window(search_member_tab)
    assign_talk_tab = ttk.Frame(notebook, bootstyle=INFO)
    populate_assign_window(assign_talk_tab)
    speaker_list_tab = ttk.Frame(notebook, bootstyle=INFO)
    populate_speaker_window(speaker_list_tab)
    add_member_tab = ttk.Frame(notebook, bootstyle=INFO)
    populate_add_window(add_member_tab)
    remove_member_tab = ttk.Frame(notebook, bootstyle=INFO)
    populate_remove_window(remove_member_tab)

    notebook.add(search_member_tab, text = "Search for Member")
    notebook.add(speaker_list_tab, text = "Speaker List")
    notebook.add(assign_talk_tab, text = "Assign a Talk")
    notebook.add(add_member_tab, text = "Add a Member")
    notebook.add(remove_member_tab, text = "Remove a Member")

    notebook.pack(fill=BOTH, expand=1)

    window.mainloop()

#Will search the database for any member by First or Last or Both names
def populate_search_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        window: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "First and Last name:"
    lbl_first = Label(window, text="Enter First Name:")
    lbl_last = Label(window, text="Enter Last Name:")

    # Create an entry box where the user will enter first and last name.
    ent_first = ttk.Entry(window, width=40)
    ent_last = ttk.Entry(window, width=40)

    # Create the search button.
    btn_search = Button(window, text="Search", command=lambda: get_person(ent_first.get().capitalize(), ent_last.get().capitalize()))

    #Creates textbox to output data to
    colheader = [
        {"text": "MEMBER_ID", "stretch": False},
        {"text": "LAST_NAME", "stretch": True},
        {"text": "FIRST_NAME", "stretch": True},
        {"text": "AGE", "stretch": False},
        {"text": "PHONE_NUMBER", "stretch": False},
        {"text": "EMAIL", "stretch": True},
    ]
    rowdata = []
    table_view = ttk.tableview.Tableview(
        master=window,
        coldata=colheader,
        rowdata=rowdata,
        paginated=True,
        searchable=False,
        bootstyle=PRIMARY,
        pagesize=30,
        height=29,
    )

    # Aligns labels, entry boxes and output box
    lbl_first.pack(pady=3)
    lbl_last.pack(pady=3)
    ent_first.pack(pady=3)
    ent_last.pack(pady=3)
    btn_search.pack(pady=3)
    table_view.pack(pady=3)

    # Function will find a member by first name, last name, or both names
    def get_person(first_name = "", last_name = ""):

        mycursor = mydb.cursor()
        results = []

        # Select statement that will find a member if first and last name are both inputed 
        if first_name != "" and last_name != "":
            mycursor.execute(f"SELECT member_id, last_name, first_name, age, phone_number, email FROM members where first_name = '{first_name}' and last_name='{last_name}'")
            for row in mycursor:
                results.append(row)

        # Will return all members with the same last name
        elif last_name != "":
            mycursor.execute(f"SELECT member_id, last_name, first_name, age, phone_number, email FROM members where last_name ='{last_name}'")
            for row in mycursor:
                results.append(row)

        # Will return all members with the same first name
        else:
            mycursor.execute(f"SELECT member_id, last_name, first_name, age, phone_number, email FROM members where first_name = '{first_name}'")
            for row in mycursor:
                results.append(row)

        mycursor.close()
    
        rowdata = [list(row) for row in results]
        table_view.build_table_data(coldata=colheader,rowdata=rowdata)
        table_view.reset_table()
        ent_first.delete(0, 'end')
        ent_last.delete(0, 'end')

def populate_speaker_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        window: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_first = Label(window, text="Enter the number of months Since Last Spoken: ")

    # Create an integer entry box where the user will enter her age.
    ent_last_spoken = ttk.Entry(window, width=10)

    # Create the search button.
    btn_last_spoken = Button(window, text="Search", command=lambda: speaker_list(ent_last_spoken.get()))

    colheader1 = [
        {"text": "MEMBER_ID", "stretch": False},
        {"text": "LAST_NAME", "stretch": True},
        {"text": "FIRST_NAME", "stretch": True},
        {"text": "AGE", "stretch": False},
        {"text": "PHONE_NUMBER", "stretch": False},
        {"text": "Date of Last Talk", "stretch": True},
        {"text": "Months Since Spoken", "stretch": True},
    ]

    rowdata1 = []
    table_view1 = ttk.tableview.Tableview(
        master=window,
        coldata=colheader1,
        rowdata=rowdata1,
        paginated=True,
        searchable=False,
        bootstyle=PRIMARY,
        pagesize=30,
        height=29,
    )

    # Aligns labels, entry boxes and output box
    lbl_first.pack(pady=3)
    ent_last_spoken.pack(pady=3)
    btn_last_spoken.pack(pady=3)
    table_view1.pack(pady=3)

    # Function that creates a list of potential speakers and will show last date spoken or not spoken
    def speaker_list(date = ""):

        mycursor = mydb.cursor()
        results = []
        temp = []

        # Gets todays date from the database
        mycursor.execute(f"select curdate()")
        today_date = mycursor.fetchone()[0]

        # Will do subtract todays date by x months entered by the user
        mycursor.execute(f"select date_sub('{today_date}', interval {date} month)")
        talk_date = mycursor.fetchone()[0]

        # Select statement will find all members who haven't spoken at all or haven't spoken in X months
        mycursor.execute(f"select members.member_id, members.last_name, members.first_name, members.age, members.phone_number, talks.talk_date from members join talks on members.member_id = talks.member_id where members.age > 17 and members.member_id in (select members.member_id from members join talks on members.member_id = talks.member_id where members.age > 17 and talks.talk_date < '{talk_date}' and members.member_id not in (select members.member_id from members join talks on members.member_id = talks.member_id where members.age > 17 and talks.talk_date > '{talk_date}')) union all select m.member_id, m.last_name, m.first_name, m.age, m.phone_number, NULL AS 'talk_date' from members m where m.age > 17 and m.member_id not in (select member_id from talks)")
        for row in mycursor:
            results.append(row)

        mycursor.close()
        for row in results:
            memid = row[0]
            last = row[1]
            first = row[2]
            age = row[3]
            phone = row[4]
            date = str(row[5])

            # If statement decides whether the member has spoken at all or how many months since they spoke
            if date == "None":
                last_spoke = "Has Not Spoken"
            else:
                date2 = parser.parse(date)
                diff = date1 - date2
                last_spoke = int(diff.days)
                last_spoke = last_spoke / 30.4166667
                last_spoke = int(last_spoke)

            temp.append([memid,last,first,age,phone,date,last_spoke])

        # Outputs data to the textbox
        rowdata1 = [list(row1) for row1 in temp]
        table_view1.build_table_data(coldata=colheader1,rowdata=rowdata1)
        table_view1.reset_table()
        ent_last_spoken.delete(0, 'end')

def populate_assign_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        window: the main frame (window)
    Return: nothing
    """
    member_info = []

    # Create a label that displays "Age:"
    lbl_memid = Label(window, text="Enter Member ID of Speaker:")
    lbl_talk_date = Label(window, text="Enter the Date of the Talk:")
    lbl_topic = Label(window, text="Enter the Topic of the Talk:")

    # Create an integer entry box where the user will enter her age.
    ent_memid = ttk.Entry(window, width=40)
    ent_talk_date = ttk.DateEntry(window, width=35, dateformat='%Y-%m-%d')
    ent_topic = ttk.Entry(window, width=40)

    # Create the search button.
    btn_assign = Button(window, text="Assign", command=lambda: assign_speaker(ent_memid.get(), ent_talk_date.entry.get(), ent_topic.get()))

    colheader2 = [
        {"text": "MEMBER_ID", "stretch": False},
        {"text": "LAST_NAME", "stretch": True},
        {"text": "FIRST_NAME", "stretch": True},
        {"text": "AGE", "stretch": False},
    ]

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT member_id, last_name, first_name, age FROM members")
    for row in mycursor:
        member_info.append(row)

    rowdata2 = [list(row) for row in member_info]

    table_view2 = ttk.tableview.Tableview(
        master=window,
        coldata=colheader2,
        rowdata=rowdata2,
        paginated=True,
        searchable=True,
        bootstyle=PRIMARY,
        pagesize=20,
        height=20,
    )

    output_screen2 = ttk.Text(window)

    # Aligns labels, entry boxes and output box
    lbl_memid.pack(pady=3)
    lbl_talk_date.pack(pady=3)
    lbl_topic.pack(pady=3)
    ent_memid.pack(pady=3)
    ent_talk_date.pack(pady=3)
    ent_topic.pack(pady=3)
    btn_assign.pack(pady=3)
    table_view2.pack(pady=3)
    output_screen2.pack(fill = BOTH, expand = True, pady=3, padx=3)

    def assign_speaker(member_id, talk_date, topic = ""):

        output_screen2.delete('1.0', END)
        mycursor = mydb.cursor()
        member_info = []

        mycursor.execute(f"SELECT last_name, first_name FROM members where member_id = {member_id}")
        for row in mycursor:
            member_info.append(row)

        for row in member_info:
            info_first = row[1]
            info_last = row[0]

        sql = "INSERT INTO talks (member_id, talk_date, last_name, first_name, topic) VALUES (%s, %s, %s, %s, %s)"
        val = (member_id, talk_date, info_last, info_first, topic)
        mycursor.execute(sql, val)
        mydb.commit()

        # Outputs data to the textbox
        output_screen2.insert(ttk.END, f"{info_first} {info_last} has been assigned to talk on {talk_date}\n")
        output_screen2.insert(ttk.END, f"{mycursor.rowcount} record inserted.")
        output_screen2.see(ttk.END)

        mycursor.close()
        ent_memid.delete(0, 'end')
        ent_topic.delete(0, 'end')

def populate_add_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        window: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_first = Label(window, text="Enter the First Name of the Member:")
    lbl_last = Label(window, text="Enter the Last Name of the Member:")
    lbl_age = Label(window, text="Enter the Age of the Member:")
    lbl_phone = Label(window, text="Enter the Phone Number 555-555-5555:")
    lbl_email = Label(window, text="Enter the Email of the Member:")

    # Create an integer entry box where the user will enter her age.
    ent_first = ttk.Entry(window, width=40)
    ent_last = ttk.Entry(window, width=40)
    ent_age = ttk.Entry(window, width=40)
    ent_phone = ttk.Entry(window, width=40)
    ent_email = ttk.Entry(window, width=40)

    # Create the search button.
    btn_add = Button(window, text="Add Member", command=lambda: add_member(ent_last.get().capitalize(), ent_first.get().capitalize(), ent_age.get(), ent_phone.get(), ent_email.get()))

    output_screen3 = ttk.Text(window)

    # Aligns labels, entry boxes and output box
    lbl_first.pack(pady=3)
    lbl_last.pack(pady=3)
    lbl_age.pack(pady=3)
    lbl_phone.pack(pady=3)
    lbl_email.pack(pady=3)
    ent_first.pack(pady=3)
    ent_last.pack(pady=3)
    ent_age.pack(pady=3)
    ent_phone.pack(pady=3)
    ent_email.pack(pady=3)
    btn_add.pack(pady=3)
    output_screen3.pack(fill = BOTH, expand = True, pady=10, padx=10)

    def add_member(last_name, first_name, age, phone_number, email):

        output_screen3.delete('1.0', END)
        mycursor = mydb.cursor()

        sql = "INSERT INTO members (last_name, first_name, age, phone_number, email) VALUES (%s, %s, %s, %s, %s)"
        val = (last_name, first_name, age, phone_number, email)
        mycursor.execute(sql, val)
        mydb.commit()

        # Outputs data to the textbox
        output_screen3.insert(ttk.END, f"{first_name} {last_name} has been added to the member directory.\n")
        output_screen3.insert(ttk.END, f"{mycursor.rowcount} record inserted.")
        output_screen3.see(ttk.END)

        mycursor.close()
        ent_first.delete(0, 'end')
        ent_last.delete(0, 'end')
        ent_age.delete(0, 'end')
        ent_phone.delete(0, 'end')
        ent_email.delete(0, 'end')

def populate_remove_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        window: the main frame (window)
    Return: nothing
    """    
    # Create a label that displays "Age:"
    lbl_mem_id = Label(window, text="Enter the ID of the Member to Remove: ")

    # Create an integer entry box where the user will enter her age.
    ent_mem_id = ttk.Entry(window, width=10)

    # Create the search button.
    btn_remove = Button(window, text="Remove Member", command=lambda: remove_member(ent_mem_id.get()))

    mycursor = mydb.cursor()
    member_info = []

    colheader = [
        {"text": "MEMBER_ID", "stretch": False},
        {"text": "LAST_NAME", "stretch": True},
        {"text": "FIRST_NAME", "stretch": True},
        {"text": "AGE", "stretch": False},
    ]

    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT member_id, last_name, first_name, age FROM members")
    for row in mycursor:
        member_info.append(row)

    rowdata2 = [list(row) for row in member_info]

    table_view = ttk.tableview.Tableview(
        master=window,
        coldata=colheader,
        rowdata=rowdata2,
        paginated=True,
        searchable=True,
        bootstyle=PRIMARY,
        pagesize=20,
        height=20,
    )

    output_screen4 = ttk.Text(window)

    # Aligns labels, entry boxes and output box
    lbl_mem_id.pack(pady=3)
    ent_mem_id.pack(pady=3)
    btn_remove.pack(pady=3)
    table_view.pack(pady=3)
    output_screen4.pack(fill = BOTH, expand = True, pady=3, padx=3)

    mycursor.close()

    # Function to remove user from the members table
    def remove_member(member_id):

        output_screen4.delete('1.0', END)
        mycursor = mydb.cursor()
        result = []

        # Gets first and last name of the user being deleted
        mycursor.execute(f"SELECT last_name, first_name FROM members where member_id = {member_id}")
        for row in mycursor:
            result.append(row)

        for row in result:
            info_first = row[1]
            info_last = row[0]

        # sql to delete user from the database and commits those changes
        mycursor.execute(f"delete from members where member_id = {member_id}")
        mydb.commit()

        # Outputs data to the textbox
        output_screen4.delete("1.0","end")
        output_screen4.insert(ttk.END, f"{info_first} {info_last} has been removed from the member directory.\n")
        output_screen4.insert(ttk.END, f"{mycursor.rowcount} record deleted.")
        output_screen4.see(ttk.END)

        mycursor.close()

        ent_mem_id.delete(0, 'end')

if __name__ == "__main__":
    main()