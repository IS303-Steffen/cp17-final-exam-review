from helper_functions import clear_screen
clear_screen()

# ===========
# PEEWEE CRUD
# ===========


# 1. CREATE A PEEWEE MODEL AND SQLITE DATABASE
# Create a SQLite Database called cats.db through peewee
'''
It should have the following columns:
    - cat_id (the primary key)
    - cat_name
    - cat_age
    - owner_name
'''
import peewee as pw
db = pw.SqliteDatabase("cats.db")

class Cat(pw.Model):
    cat_id = pw.AutoField(primary_key=True)
    cat_name = pw.CharField()
    age = pw.IntegerField()
    owner_name = pw.CharField()

    class Meta:
        database = db

    @classmethod
    def create(cls, **query):
        query['cat_name'] = query['cat_name'].strip().capitalize()
        query['owner_name'] = query['owner_name'].strip().capitalize()
        return super().create(**query)
    
    def get_info(self):
        return f"{self.cat_name} is owned by {self.cat_name} and is {self.age} years old."
    
db.connect()
db.create_tables([Cat])


while True:
    print(f"Menu:")
    print(f"1: Create a new cat")
    print(f"2: See all cats")
    print(f"3: See cats of specific owner")
    print(f"4: See the youngest cat")
    print(f"5: Update a cat's info")
    print(f"6: Delete a cat")
    print(f"Exit: exit the program")
    option = input("Choose an option: ")

    if option == "1":
        name = input("Enter cat's name: ")
        age = int(input("Enter cat's age: "))
        owner = input("Enter owner's name: ")
        Cat.create(cat_name=name, owner_name=owner)
        print("Cat added successfully.\n")

    elif option == "2":
        print("\nAll cats (sorted reverse alphabetically):")
        for cat in Cat.select().order_by(Cat.cat_name.desc()):
            print(f"ID: {cat.cat_id}, Name: {cat.cat_name}, Owner: {cat.owner_name}")
        print()

    elif option == "3":
        owner_query = input("Enter the owner's name: ").strip().capitalize()
        cats = Cat.select().where(Cat.owner_name == owner_query)
        if cats:
            print(f"\nCats owned by {owner_query}:")
            for cat in cats:
                print(f"\t{cat.get_info()}")
        else:
            print(f"No cats found for owner '{owner_query}'.")
        print()

    elif option == "4":
        youngest_cat = Cat.select().order_by(Cat.age).first()
        print("This is the youngest cat:")
        print(youngest_cat.get_info())

    elif option == "5":
        cat_id = int(input("Enter cat ID to update: "))
        cat = Cat.get_by_id(cat_id)
        new_name = input("Enter new cat name: ")
        cat.cat_name = new_name.strip().capitalize()
        cat.save()
        print("Cat info updated.\n")

    elif option == "6":
        cat_id = int(input("Enter cat ID to delete: "))
        cat = Cat.get_by_id(cat_id)
        cat.delete_instance()
        print("Cat deleted successfully.\n")

    elif option.lower() == "exit":
        break

    else:
        print("Not a valid option, try again.\n")

# Cleanup
db.close()




# 2. CREATE A ROW USING INPUTS
# Ask the user for inputs for the cat_name, owner_name, and age to create new rows
# in the database



# 3. OVERRIDE THE CREATE FUNCTION
# Override the create function to make sure that every cat_name and
# owner_name gets stored as a capitalized version. (e.g. "max" or "MAX" should
# be stored as "Max") Don't stop anything from being created, just make it so
# the first letter is capitalized and that it is stored without leading or
# trailing spaces.



# 4. ADD A GET_INFO METHOD TO THE CAT CLASS
# In your Cat class, add a method called "get_info" that returns the
# cat's name, owner name and age in a nicely formatted string.



# 5. MAKE A MENU AND ADD A READ OPTION
# Make a menu. Option 1 is to add a new cat (for what you did in #1)
# Option 2 is to see all cats. When option 2 is selected, make it so that the
# cats print out in reverse alphabetical order by cat_name. The menu should
# repeat until the user enters "exit"



# 6. READ A SPECIFIC SUBSET
# Add option 3. Option 3 should ask for an owner's name. If the owner name
# exists, make it show all the cats with that owner_name. If the owner_name
# doesn't exist in the database, display a message that that owner couldn't be
# found, and go back to the menu.



# 6. FIND THE YOUNGEST CAT
# Add option 4. Option 4 should display the the get_info of the youngest cat 
# in the database. For simplicity, if there is a tie for the youngest, you 
# can just display one. (If you want a little extra challenge, feel free to
# try and write code that accounts for a tie for youngest age)



# 7. UPDATE A ROW 
# Add option 4. Enter a cat's id to get it, then enter a new name, and save
# that name. For time's sake you can assume the Id entered will always be valid



# 8. DELETE A ROW
# Add option 5. Enter a cat's id to get it, then delete it. Print out a
# message that it was deleted.
