import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="tiffanyspringsward"
)

def main():
    
    get_first_name = input("Please enter first name: ")
    get_last_name = input("Please enter last name: ")

    get_person(get_first_name, get_last_name)
    

def get_person(first_name = "", last_name = ""):

  mycursor = mydb.cursor()

  if first_name != "" and last_name != "":
    mycursor.execute(f"SELECT * FROM members where first_name = '{first_name}' and last_name='{last_name}'")
    for row in mycursor:
      print(row)

  elif last_name != "":
    mycursor.execute(f"SELECT * FROM members where last_name='{last_name}'")
    for row in mycursor:
      print(row)

  else:
    mycursor.execute(f"SELECT * FROM members where first_name = '{first_name}'")
    for row in mycursor:
      print(row)

  mycursor.close()

if __name__ == "__main__":
    main()