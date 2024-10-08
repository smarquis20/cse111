import csv
def main():

    inumber_index = 0
    student_index = 1
    
    inumber_dict = read_dictionary("students.csv", inumber_index)
     
    user_inumber = input("Please enter an I-Number (xxxxxxxxx): ")

    if user_inumber not in inumber_dict:
        print("No such Student")
    else:
        student_key = inumber_dict[user_inumber]
        student_name = student_key[student_index]

        print(student_name)



def read_dictionary(filename, key_column_index):
        """Read the contents of a CSV file into a compound
        dictionary and return the dictionary.
        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
        """
        dictionary = {}

        with open(filename, "rt") as csv_file:
             
            reader = csv.reader(csv_file)
            next(reader)

            for student_list in reader:
               if len(student_list) != 0:
                    key = student_list[key_column_index]
                    dictionary[key] = student_list
                
        return dictionary

if __name__ == "__main__":
    main()