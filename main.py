import datetime as dt

# TODO 1: USERNAME AND FILE SETUP FOR DATABASE AND KEEP TRACK OF BOOK READING
USERSDB = {"victor": {"first_name": "Victor", "last_name": "Ponce", "books_per_year": 10, "pages_history": [],
                      "consecutive_days": 0}}


def username_setup():
    """
    Checks the user setup status, if it's a user in DATABASE or needs to be added.
    :return: username
    """
    while True:
        user = input("Please enter your username: ")
        global USERSDB
        if user in USERSDB:
            print(f"Welcome to book tracker again {USERSDB[user]['first_name']}")
            return user
        else:
            first_name = input("It looks like you have not created your account, please enter your first name: ")
            last_name = input("Please enter your last name: ")
            username = input("Please confirm your username: ")
            if user == username:
                USERSDB[username] = {"first_name": first_name, "last_name": last_name}
                now = dt.date.today()
                USERSDB[username]["start_date"] = now
                print(f"Welcome to book tracker {USERSDB[username]['first_name']}")
                book_goals(username)
                return username
            else:
                print("Your username has not been confirmed")
                continue


# username_setup()
# print(USERSDB)

# TODO 2: GOALS FOR THE USER EG//BOOKS PER YEAR
def book_goals(user):
    """
    Initial goal setup for a recently created user.(Books per year)
    :param user: username
    :return:
    """
    books_goal = int(input("How many books in a year would you like to read?"))
    global USERSDB
    USERSDB[user]["books_per_year"] = books_goal
    avg_bookpages = 230
    total_pages = avg_bookpages * books_goal
    pages_per_day = total_pages // 365
    print(f"You should read {pages_per_day} pages in a day to read {books_goal} books in a year")


# TODO 3: TRACK DAILY PROGRESS (BOOK TITLE, PAGES, HOURS/minutes)
def daily_reading(user):
    """
    To check the reading progress daily.
    :param user: Dictionary(USERDB[kw(username)])
    :return: USERDB as global variable
    """
    global USERSDB
    pages = int(input("How many pages did you read today? "))
    USERSDB[user]["pages_history"] = []
    USERSDB[user]["pages_history"].append(pages)
    statistics_request = input("Would you like to check your book reading statistics? (Y/N)")
    if statistics_request.lower() == "n" or statistics_request.lower() == "no":
        return "Keep reading every day, have a good day!"
    else:
        print(statistics_check(user))


# TODO 4: STATISTICS (%READ OF THE BOOK, GOAL PROGRESS, HOW MANY BOOKS/PAGES READ, PAGES/MIN)
def statistics_check(user):
    global USERSDB
    pages_left = 10 * 230 - sum(USERSDB[user]["pages_history"])
    time_check = (USERSDB[user]["start_date"] - dt.date.today()).days
    if time_check > 0:
        return f"You have only {pages_left}. You still have {time_check} days left"
    else:
        return f"You have read {sum(USERSDB[user]['pages_history'])} pages already, keep reading to improve every day"


# TODO 5: Application brain
user_logged = True
while user_logged:
    user = username_setup()
    daily_reading(user)
    user_logged = False
