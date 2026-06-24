#Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'SPCA_adoption_list.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

#creating a user interface based on the database my makig a list
# Menu repeats until user chooses Z
while True:
    try:
        adoption_info = input(
            "\nSPCA Pet Adoption Database\n"
            "A: Budget friendly pets available in the store\n"
            "B: The number of animals available in each animal type\n"
            "C: Adult cats that are of the domestic breed\n"
            "D: Expensive dogs and cats\n"
            "E: The number of longstay animals\n"
            "F: How many pets are available from each city\n"
            "G: Pets from youngest to oldest\n"
            "H: The most expensive pet available\n"
            "Z: Exit\n"
            "Type option here: "
        )

        adoption_info = adoption_info.upper()

        if adoption_info == "A":
            print("You selected budget friendly pets")
            print_query("cheap_pets")

        elif adoption_info == "B":
            print("You selected number of animals in each animal type")
            print_query("animal_type_count")

        elif adoption_info == "C":
            print("You selected adult domestic cats")
            print_query("adult_domestic_cats")

        elif adoption_info == "D":
            print("You selected expensive dogs and cats")
            print_query("expensive_dogs_and_cats")

        elif adoption_info == "E":
            print("You selected longstay animals")
            print_query("longstay_animals")

        elif adoption_info == "F":
            print("You selected pets from each city")
            print_query("pets_from_each_city")

        elif adoption_info == "G":
            print("You selected pets from youngest to oldest")
            print_query("youngest_to_oldest_pets")

        elif adoption_info == "H":
            print("You selected most expensive pet")
            print_query("most_expensive_pet")

        elif adoption_info == "Z":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose A, B, C, D, E, F, G, H or Z.")

    except:
        print("Something went wrong. Please try again.")
