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
# Add option 5. Enter a cat's id to get it, then enter a new name, and save
# that name. For time's sake you can assume the Id entered will always be valid



# 8. DELETE A ROW
# Add option 6. Enter a cat's id to get it, then delete it. Print out a
# message that it was deleted.
