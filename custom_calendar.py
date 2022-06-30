from datetime import date


def is_leap(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False


def makeCalendar(year, month, date, day):
    for week in weeks:
        print(week, end="   ")
    print("\n")

    space = 0
    day_num = 0
    for i in range(7):
        if weeks[i] == day[0:2]:
            space = i
            day_num = i
            break
    space = (space * 2) + (space * 3)

    # Print Space before date 1
    print(" " * space, end="")

    print_date = 1

    for i in range(6):
        # print(i)
        if i == 0:
            for j in range(day_num, 7):
                print("{:02d}".format(print_date), end="   ")
                print_date += 1
        else:
            for j in range(7):
                print("{:02d}".format(print_date), end="   ")
                print_date += 1
                if print_date > calender[month-1][1]:
                    break
        if print_date > calender[month - 1][1]:
            break
        print("\n")


calender = [
    ('January', 31),
    ('Feburary', 28),
    ('March', 31),
    ('April', 30),
    ('May', 31),
    ('June', 30),
    ('July', 31),
    ('August', 31),
    ('September', 30),
    ('October', 31),
    ('November', 30),
    ('December', 31)
]

weeks = [
    "Mo",
    "Tu",
    "We",
    "Th",
    "Fr",
    "Sa",
    "Su"
]

current_year = date.today().year
current_month = date.today().month
# Code to get today's date
# current_date = date.today().day
# Code to get the day
current_day = date(current_year, current_month, 1).strftime("%A")


# Check Leap Year
if is_leap(2012):
    calender.remove(('Feburary', 28))
    calender.insert(1, ('Feburary', 29))

print("\n\n*************************** Calendar For Current Month [" + calender[current_month-1][0] + "] " + str(current_year) + " ***************************\n\n")

makeCalendar(current_year, current_month, 1, current_day)


choice = 1

while choice != 0:
    calender = [
        ('January', 31),
        ('Feburary', 28),
        ('March', 31),
        ('April', 30),
        ('May', 31),
        ('June', 30),
        ('July', 31),
        ('August', 31),
        ('September', 30),
        ('October', 31),
        ('November', 30),
        ('December', 31)
    ]
    
    print("\n\n")
    print("Choose From Below\n")
    print("1. Get Specified calendar")
    print("0. Exit")

    choice = int(
        input("\nEnter the Number of Operation you want to perform:: "))

    if choice == 1:
        month = int(input("Enter Month Number: "))
        year = int(input("Enter Year Number: "))
        day = date(year, month, 1).strftime("%A")
        print(day)
        if is_leap(2012):
            calender.remove(('Feburary', 28))
            calender.insert(1, ('Feburary', 29))

        print("\n\n*************************** Calendar For " + calender[month - 1][0] + " " + str(year) + " ***************************\n\n")
        makeCalendar(year, month, 1, day)

    elif choice == 0:
        exit()

    else:
        print("\n\nINVALID SELECTION...!!!\n\n")
