#!usr/bin/python

# Imports
import os
import time
import random
import sqlite3 as lite

# Strings
db = 't3_class_database.db'
f_name = None
l_name = None
name = None

# Booleans
db_exists = None

# Integers and Floats
score = 0
s_class = None
question = 0
num1 = None
num2 = None
int_operator = None
main_selection = None

# Defined Functions
# clear() function.
def clear():

    # Prints 100 blank lines, clearing the screen.
    print("\n" * 100)

# Displays the title of the program.
print("Maths Test")
print("----------")

# Displays the versioning of the program.
print("Task 3 - Version 1.2a")

# States me, Jack Tench, as the developer of the program.
print("Developed by Jack Tench")

# Uses an if statement to find out if the SQL database file has been
# detected by the SQLite3 module.
if os.path.isfile(db):

    # Sets the variable for the file to be found to true, because
    # the OS module found it.
    db_exists = True

    # Because the database has been found, the program can connect
    # to it using the SQLite3 module.
    con = lite.connect(db)

else:

    # Sets the variable for if the file is detected to false, because the file
    # has not been detected by the if statement.
    db_exists = False

    # If the database file does not exist, the SQLite3 module, imported as lite,
    # creates the file to then connect to it.
    con = lite.connect(db)

    # Loops three times using the variable i, so I can run code multiple times,
    # using %s to iterate using the number.
    for i in range(1, 4):

        # Using the SQLite3 module, and the connection I created, a command
        # can be executed to create a table, an integer named ID, and set
        # it as the primary key, a string called NAME, and an integer
        # named SCORE.
        con.execute("CREATE TABLE class%s (ID INTEGER PRIMARY KEY, NAME TEXT, SCORE INTEGER);" %i)

# Using the SQLite3 module, and the connection I created, a cursor can be
# set. A cursor is used to tranverse records from the result set.
cur = con.cursor()

# Prints a single blank line on the screen.
print()

# Prints a selection screen for the user to select if they are a teacher or a student.
print("Are you a student or a teacher?")
print("1) Student")
print("2) Teacher")

# Takes the user's selection and formats it for the program to read it.
main_selection = int(input("Enter a number: "))

if main_selection == 2:
    
    clear()

    print("Teacher Control Panel")
    print("---------------------")
    selection = input("Please select a class to view: ")

    selection = int(selection)

    if selection == 1:
        print("Class 1 Selected.")
    elif selection == 2:
        print("Class 2 Selected.")
    elif selection == 3:
        print("Class 3 Selected.")
    else:
        print("Closing the program...")
        time.sleep(2)
        quit()
    
elif main_selection == 1:

    clear()

    # The user selects their class, and it is converted into an integer, and then
    # stored in the s_class variable. This code is looped until a valid class
    # number is input.
    s_class = 0
    while s_class > 3 or s_class < 1:
        print("There are classes 1, 2, and 3.")
        s_class = int(input("Please enter your class: "))

    # The user inputs their name, and it is converted into a string, and then stored
    # in the f_name and l_name variables.
    print("Please enter your name.")
    f_name = str(input("First Name: "))
    l_name = str(input("Last name: "))

    # Uses both of the variables assigned above to create a name string, containing
    # the user's full name with a space in the middle.
    name = f_name + " " + l_name

    print("Hello, " + name + "! Welcome!")

    # Iterates i three times, so I can countdown from three every second.
    for i in range(1, 4):

        # Prints the current number, and then waits a second before starting a new
        # iteration of the code.
        print("%s" %i)
        time.sleep(1)

    clear()

    # Loops until the question is question 10, because there are ten questions in my
    # test.
    while question < 10:

        # Updates the question variable to count.
        question += 1

        print("Question %s" %question)
        
        # Calculates how many characters to use to underline the text.
        if question == 10:

            # Prints enough characters to accomodate for 10 being 1 character
            # longer than any of the previous numbers.
            print("-----------")

        else:
        
            print("----------")

        # Generates both of the random numbers used to make the sum, and then stores
        # them inside the integer variables num1 and num2.
        num1 = random.randint(1, 10)       
        num2 = random.randint(1, 10)

        # Generates the random number used to make the operator, and then stores
        # it in the variable int_operator.
        int_operator = random.randint(1, 3)

        # Generated which operator to use, and then generates the answer from
        # the num1 and num2 variables, and also sets operator to the text form
        # of the operator.
        if int_operator == 1:
        
            # Plus
            ans = num1 + num2
            operator = "+"
        
        elif int_operator == 2:
        
            # Minus
            ans = num1 - num2
            operator = "-"
        
        elif int_operator == 3:

            # Times
            ans = num1 * num2
            operator = "X"

        # Proposes the question, and returns the answer as an integer to the
        # variable user_ans.
        user_ans = int(input(str(num1) + " " + operator + " " + str(num2) + " = "))

        # Checks if the answer is correct or not.
        if user_ans == ans:

            # If the answer is correct, the score is updated by adding 1 to
            # the variable score. Then, it prints the score and tells the user
            # their answer was correct.
            score = score + 1
            print("Correct! Your score is " + str(score) + "!")
        
        else:
        
            # If the answer is incorrect, the score is not updated, but the user
            # is told their score, and that their answer was incorrect.
            print("Incorrect! Your score is " + str(score) + ".")

        # Sleeps for one second, and then runs the clear() function.
        time.sleep(1)
        clear()

    # Tells the cursor to write to the database.
    table = "class%s" %s_class
    with con:
        cur.execute("INSERT INTO " + table + "(NAME, SCORE) VALUES (?, ?);", (name, score))

    # Prints out to the user to inform them of their score.
    print("You finished the test with a score of " + str(score) + "!")
    print("Your score has been recorded.")
    time.sleep(1)
    input("The test has finished. Press <Enter> to exit.")

else:

    # Prompts the user to press enter, then quits.
    input("Press <Enter> to exit.")
    quit()
