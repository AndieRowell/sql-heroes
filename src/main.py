from database.db_connection import execute_query

# this is an example query that shows us all the hero names
def select_all_heroes():
    query = """
        SELECT * from heroes
    """
    returned_items = execute_query(query) #execute query function to perform differrent queries
    for item in returned_items:
        print(item[1]) #so we can see things returned in the terminal
    return returned_items

select_all_heroes() #runs the function
#--------------------------------------------------------------------------

#example define a function to 'add' a hero named batman

def add_batman():
    prompt = input("Do you want to add batman? Y or N: ")
    if prompt == "Y":
        query = """
                INSERT INTO heroes (name, about_me, biography)
                VALUES ('batman', 'lefty', 'big lefty')
                """
        execute_query(query)

add_batman()

#to test this in the terminal always python main.py in terminal
#a menu with a key input?
#----

#add a function to be able to "look up" and display a character
#need some way to enter the name and match it to what's in the database?
    #maybe a variable to put into the parameters?
def look_up_char():
    superhero_name = input("Who would you like to look up? Type Name Here: ")
        query = """
                SELECT *
                FROM superheroes
                WHERE name = {}").format(sql.Literal(superhero_name))
                """
        if result:
            print("Supehero Stats:")
            print("Name:", )
            print("Abilities",)

#add a function to add a character


#add a function to update a character
def edit

#add a function to delete
