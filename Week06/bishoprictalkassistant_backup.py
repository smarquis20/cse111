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
    
    get_first_name = input("Please enter first name: ")
    get_last_name = input("Please enter last name: ")

    person_search = get_person(get_first_name, get_last_name)
    
    for row in person_search:
        first = row[1]
        last = row[0]
        age = row[2]
        phone = row[3]
        email = row[4]

        print(f"{last} {first} {age} {phone} {email}")

    months_lookback = int(input("How many months do you want to look back: "))

    talks_to_give = speaker_list(months_lookback)

    for row in talks_to_give:
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

        print(f"{last} {first} {age} {phone} {date} {last_spoke}")

    add_first = input("Please enter first name: ")
    add_last = input("Please enter last name: ")
    add_age = input("Please enter age: ")
    add_phone = input("Please enter phone number 555-555-5555: ")
    add_email = input("Please enter email: ")

    member_added = add_member(add_last, add_first, add_age, add_phone, add_email)

    print(member_added)

    removed_member = input("Please enter member ID to remove: ")

    deleted_member = remove_member(removed_member)

    print(deleted_member)

    talk_id = input("Please enter member ID of person speaking: ")
    speaking_date = input("Please enter date of talk: ")
    speaking_topic = input("Please enter the topic for the speaker: ")

    talk_assigned = assign_speaker(talk_id, speaking_date, speaking_topic)

    for row in talk_assigned:
        first = row[3]
        last = row[2]
        date = row[1]
        topic = row[4]

        print(f"{date} {last} {first} {topic}")

def get_person(first_name = "", last_name = ""):

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
    return results


def speaker_list(date = ""):

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
    return results

def add_member(last_name, first_name, age, phone_number, email):

    mycursor = mydb.cursor()
    results = []

    sql = "INSERT INTO members (last_name, first_name, age, phone_number, email) VALUES (%s, %s, %s, %s, %s)"
    val = (last_name, first_name, age, phone_number, email)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    mycursor.execute(f"SELECT last_name, first_name, age, phone_number, email FROM members where first_name = '{first_name}' and last_name = '{last_name}'")
    for row in mycursor:
        results.append(row)

    mycursor.close()
    return results

def assign_speaker(member_id, talk_date, topic = ""):

    mycursor = mydb.cursor()
    member_info = []
    results = []

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

    print(mycursor.rowcount, "record inserted.")

    mycursor.execute(f"SELECT member_id, talk_date, last_name, first_name, topic FROM talks where member_id = {member_id}")
    for row in mycursor:
        results.append(row)

    mycursor.close()
    return results

def remove_member(member_id):

    mycursor = mydb.cursor()
    results = []

    mycursor.execute(f"SELECT member_id, last_name, first_name, age, phone_number, email from members where member_id = {member_id}")
    for row in mycursor:
        results.append(row)

    mycursor.execute(f"delete from members where member_id = {member_id}")
    mydb.commit()

    print(mycursor.rowcount, "record deleted.")

    mycursor.close()
    return results

if __name__ == "__main__":
    main()