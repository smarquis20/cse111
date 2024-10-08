"""
Author: Shaun Marquis

Purpose: This program creates a dictionary of products that can be sold and sorts through
a list of items purchased and will return the name of the item, quantity, and price.
EXTRA CREDIT: I added logic to check if it is before 11 AM and to give a 10% discount if it is.
If it is not before 11AM than it processes like normal.
"""
import csv
from datetime import datetime

def main():
    try:

        product_key_index = 0
        product_item_index = 1
        product_price_index = 2
        request_item_index = 0
        request_quantity_index = 1
    
        products_dict = read_dictionary("products.csv", product_key_index)

        print("Marquis Emporium")
     
        with open("request.csv", "rt") as shopping_list_file:
            reader = csv.reader(shopping_list_file)
            next(reader)

            total_quantity = 0
            subtotal = 0

            for row_list in reader:
                request_item_key = row_list[request_item_index]
                request_quantity = int(row_list[request_quantity_index])

                total_quantity = total_quantity + request_quantity

                product_name_key = products_dict[request_item_key]
                product_name = product_name_key[product_item_index]
                product_price = float(product_name_key[product_price_index])

                subtotal = subtotal + (product_price * request_quantity)

                print(f"{product_name}: {request_quantity} @ {product_price}")

        cdt = datetime.now()

        if cdt.hour < 11:
            
            discount = subtotal * .1
            discount_total = subtotal - discount
            sales_tax = discount_total * .06
            final_total = discount_total + sales_tax

            print(f"Number of Items: {total_quantity}")
            print(f"You Recieved a 10% discount because its before 11:00 AM!")
            print(f"Discount Total: {discount:.2f}")
            print(f"Subtotal: {discount_total:.2f}")
            print(f"Sales Tax: {sales_tax:.2f}")
            print(f"Total: {final_total:.2f}")
            print(f"Thank you for shopping at the Marquis Emporium.")

            print(f"{cdt:%a %b %d %I:%M:%S %Y}")

        else:

            sales_tax = subtotal * .06
            final_total = subtotal + sales_tax

            print(f"Number of Items: {total_quantity}")
            print(f"Subtotal: {subtotal:.2f}")
            print(f"Sales Tax: {sales_tax:.2f}")
            print(f"Total: {final_total:.2f}")
            print(f"Thank you for shopping at the Marquis Emporium.")

            print(f"{cdt:%a %b %d %I:%M:%S %Y}")

    except FileNotFoundError as not_found_err:
        print(not_found_err)

    except PermissionError as perm_err:
        print(perm_err)
    
    except KeyError as key_err:
        print(f"Error: Unkown product ID in the request.csv file {key_err}")

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

        for product_list in reader:
            if len(product_list) != 0:
                key = product_list[key_column_index]
                dictionary[key] = product_list
                
    return dictionary

if __name__ == "__main__":
    main()