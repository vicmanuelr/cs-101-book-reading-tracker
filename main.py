# TODO 1: USERNAME AND FILE SETUP FOR DATABASE AND KEEP TRACK OF BOOK READING
def username_setup():
    try:
        with open("database.txt") as file:
            database_lines = file.readlines()
    except FileNotFoundError:
        with open("database.txt", "w") as file:
            database_lines = []
    finally:
        user = input("Please enter your username to start:")
        if user in database_lines:
            print("User already exist")
        else:
            database_lines.append(user)


# TODO 2: GOALS FOR THE USER EG//BOOKS PER YEAR

# TODO 3: TRACK DAILY PROGRESS (BOOK TITLE, PAGES, HOURS)

# TODO 4: STATISTICS (%READ OF THE BOOK, GOAL PROGRESS, HOW MANY BOOKS/PAGES READ, PAGES/MIN)
