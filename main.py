# TODO 1: USERNAME AND FILE SETUP FOR DATABASE AND KEEP TRACK OF BOOK READING
USERSDB = {"victor": {"first_name": "Victor", "last_name": "Ponce"}}

def username_setup():
    """
    Checks the user setup status, if it's a user in DATABASE or needs to be added.
    """
    user = input("Please enter your username: ")
    global USERSDB
    if user in USERSDB:
        return f"Welcome to book tracker again {USERSDB[user]['first_name']}"
    else:
        first_name = input("It looks like you have not created your account, please enter your first name: ")
        last_name = input("Please enter your last name: ")
        username = input("Please confirm your username: ")
        USERSDB[username] = {"first_name": first_name, "last_name": last_name}
        print(f"Welcome to book tracker {USERSDB[user]['first_name']}")

# test the user creation
# print(username_setup())

# TODO 2: GOALS FOR THE USER EG//BOOKS PER YEAR
#
def define_goals(user):
    pass


# TODO 3: TRACK DAILY PROGRESS (BOOK TITLE, PAGES, HOURS)

# TODO 4: STATISTICS (%READ OF THE BOOK, GOAL PROGRESS, HOW MANY BOOKS/PAGES READ, PAGES/MIN)
