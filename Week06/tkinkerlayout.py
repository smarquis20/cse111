import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
import mysql.connector
from datetime import datetime
from dateutil import parser

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="schoolproject"
)

cur_date = datetime.today().strftime('%Y-%m-%d')

date1 = parser.parse(cur_date)

def main():
    window = ttk.Window(themename="darkly")
    window.geometry('1024x700')
    window.title("Bishopric Speaking Assistant")

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

def populate_search_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    global output_screen

    # Create a label that displays "First and Last name:"
    lbl_first = Label(window, text="Enter First Name:")
    lbl_last = Label(window, text="Enter Last Name:")

    # Create an entry box where the user will enter first and last name.
    ent_first = ttk.Entry(window, width=40)
    ent_last = ttk.Entry(window, width=40)

    # Create the search button.
    btn_search = Button(window, text="Search", command=lambda: get_person(ent_first.get(), ent_last.get()))

    output_screen = ttk.Text(window)

    lbl_first.pack(pady=3)
    lbl_last.pack(pady=3)
    ent_first.pack(pady=3)
    ent_last.pack(pady=3)
    btn_search.pack(pady=3)
    output_screen.pack(fill = BOTH, expand = True, pady=10, padx=10)

def populate_speaker_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    global output_screen1

    # Create a label that displays "Age:"
    lbl_first = Label(window, text="Enter the number of months Since Last Spoken: ")

    # Create an integer entry box where the user will enter her age.
    ent_last_spoken = ttk.Entry(window, width=10)

    # Create the search button.
    btn_last_spoken = Button(window, text="Search", command=lambda: speaker_list(ent_last_spoken.get()))

    output_screen1 = ttk.Text(window)
    scroll = Scrollbar(window, orient='vertical')
    scroll.pack(side=RIGHT, fill='y')
    scroll.config(command=output_screen1.yview)

    lbl_first.pack(pady=3)
    ent_last_spoken.pack(pady=3)
    btn_last_spoken.pack(pady=3)
    output_screen1.pack(fill = BOTH, expand = True, pady=10, padx=10)

def populate_assign_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    global output_screen2

    # Create a label that displays "Age:"
    lbl_memid = Label(window, text="Enter Member ID of Speaker:")
    lbl_talk_date = Label(window, text="Enter the Date of the Talk:")
    lbl_topic = Label(window, text="Enter the Topic of the Talk:")

    # Create an integer entry box where the user will enter her age.
    ent_memid = ttk.Entry(window, width=40)
    ent_talk_date = ttk.Entry(window, width=40)
    ent_topic = ttk.Entry(window, width=40)

    # Create the search button.
    btn_assign = Button(window, text="Assign", command=lambda: assign_speaker(ent_memid.get(), ent_talk_date.get(), ent_topic.get()))

    output_screen2 = ttk.Text(window)

    lbl_memid.pack(pady=3)
    lbl_talk_date.pack(pady=3)
    lbl_topic.pack(pady=3)
    ent_memid.pack(pady=3)
    ent_talk_date.pack(pady=3)
    ent_topic.pack(pady=3)
    btn_assign.pack(pady=3)
    output_screen2.pack(fill = BOTH, expand = True, pady=10, padx=10)

def populate_add_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    global output_screen3

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
    btn_add = Button(window, text="Add Member", command=lambda: add_member(ent_last.get(), ent_first.get(), ent_age.get(), ent_phone.get(), ent_email.get()))

    output_screen3 = ttk.Text(window)

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

def populate_remove_window(window):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    global output_screen4

    # Create a label that displays "Age:"
    lbl_mem_id = Label(window, text="Enter the ID of the Member to Remove: ")

    # Create an integer entry box where the user will enter her age.
    ent_mem_id = ttk.Entry(window, width=10)

    # Create the search button.
    btn_remove = Button(window, text="Remove Member", command=lambda: remove_member(ent_mem_id.get()))

    output_screen4 = ttk.Text(window)
    scroll = Scrollbar(window, orient='vertical')
    scroll.pack(side=RIGHT, fill='y')
    scroll.config(command=output_screen4.yview)

    lbl_mem_id.pack(pady=3)
    ent_mem_id.pack(pady=3)
    btn_remove.pack(pady=3)
    output_screen4.pack(fill = BOTH, expand = True, pady=10, padx=10)

def get_person(first_name = "", last_name = ""):

    output_screen.delete('1.0', END)
    mycursor = mydb.cursor()
    results = []

    if first_name != "" and last_name != "":
        mycursor.execute(f"SELECT last_name, first_name, age, phone_number, email FROM members where first_name = '{first_name}' and last_name='{last_name}'")
        for row in mycursor:
            results.append(row)

    elif last_name != "":
        mycursor.execute(f"SELECT last_name, first_name, age, phone_number, email FROM members where last_name ='{last_name}'")
        for row in mycursor:
            results.append(row)

    else:
        mycursor.execute(f"SELECT last_name, first_name, age, phone_number, email FROM members where first_name = '{first_name}'")
        for row in mycursor:
            results.append(row)

    mycursor.close()
    for row in results:
        first = row[1]
        last = row[0]
        age = row[2]
        phone = row[3]
        email = row[4]

        output_screen.insert(ttk.END, f"{last} {first} {age} {phone} {email} \n")
    output_screen.see(ttk.END)

def speaker_list(date = ""):

    output_screen1.delete('1.0', END)
    mycursor = mydb.cursor()
    results = []

    mycursor.execute(f"select curdate()")
    today_date = mycursor.fetchone()[0]

    mycursor.execute(f"select date_sub('{today_date}', interval {date} month)")
    talk_date = mycursor.fetchone()[0]

    mycursor.execute(f"select distinct(members.last_name), members.first_name, members.age, members.phone_number, talks.talk_date from members join talks on members.member_id = talks.member_id where members.age > 17 and members.member_id in (select distinct(members.member_id) from members join talks on members.member_id = talks.member_id where members.age > 17 and talks.talk_date < '{talk_date}' and members.member_id not in (select distinct(members.member_id) from members join talks on members.member_id = talks.member_id where members.age > 17 and talks.talk_date > '{talk_date}')) union all select m.last_name, m.first_name, m.age, m.phone_number, NULL AS 'talk_date' from members m where m.age > 17 and m.member_id not in (select member_id from talks)")
    for row in mycursor:
        results.append(row)

    mycursor.close()
    for row in results:
        first = row[1]
        last = row[0]
        age = row[2]
        phone = row[3]
        date = str(row[4])

        if date == "None":
            last_spoke = "Has Not Spoken"
        else:
            date2 = parser.parse(date)
            diff = date1 - date2

            last_spoke = int(diff.days)
            last_spoke = last_spoke / 30.4166667
            last_spoke = int(last_spoke)

        output_screen1.insert(ttk.END, f"{last} {first} {age} {phone} {date} {last_spoke}\n")
    output_screen1.see(ttk.END)

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

    output_screen2.insert(ttk.END, f"{info_first} {info_last} has been assigned to talk on {talk_date}\n")
    output_screen2.insert(ttk.END, f"{mycursor.rowcount} record inserted.")
    output_screen2.see(ttk.END)

    mycursor.close()

def add_member(last_name, first_name, age, phone_number, email):

    output_screen3.delete('1.0', END)
    mycursor = mydb.cursor()

    sql = "INSERT INTO members (last_name, first_name, age, phone_number, email) VALUES (%s, %s, %s, %s, %s)"
    val = (last_name, first_name, age, phone_number, email)
    mycursor.execute(sql, val)
    mydb.commit()

    output_screen3.insert(ttk.END, f"{first_name} {last_name} has been added to the member directory.\n")
    output_screen3.insert(ttk.END, f"{mycursor.rowcount} record inserted.")
    output_screen3.see(ttk.END)

    mycursor.close()

def remove_member(member_id):

    output_screen4.delete('1.0', END)
    mycursor = mydb.cursor()
    result = []

    mycursor.execute(f"SELECT last_name, first_name FROM members where member_id = {member_id}")
    for row in mycursor:
        result.append(row)

    for row in result:
        info_first = row[1]
        info_last = row[0]

    mycursor.execute(f"delete from members where member_id = {member_id}")
    mydb.commit()

    output_screen4.insert(ttk.END, f"{info_first} {info_last} has been removed from the member directory.\n")
    output_screen4.insert(ttk.END, f"{mycursor.rowcount} record deleted.")
    output_screen4.see(ttk.END)

    mycursor.close()

if __name__ == "__main__":
    main()
