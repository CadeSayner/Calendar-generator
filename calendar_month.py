
def day_of_week(day, month, year):
    w = (1 + 5*((year-1)%4) + 4*((year - 1)%100) + 6*((year-1)%400)) % 7 # Day of the week on which the first of january falls
    dayOfTheYear = day - 1

    for i in range(1, month):
        dayOfTheYear += num_days_in(i, year)

    if dayOfTheYear%7 + w > 7:
        return (dayOfTheYear + w) % 7
    return dayOfTheYear%7 + w

def is_leap(year):
    if year%100 == 0:
        if year %400 == 0:
            return True
        return False

    elif year%4 == 0:
        return True
    return False


def month_num(month_name):
    month_name = month_name.lower()
    if month_name == "january":
        return 1
    if month_name == "february":
        return 2
    if month_name == "march":
        return 3
    if month_name == "april":
        return 4
    if month_name == "may":
        return 5
    if month_name == "june":
        return 6
    if month_name == "july":
        return 7
    if month_name == "august":
        return 8
    if month_name == "september":
        return 9
    if month_name == "october":
        return 10
    if month_name == "november":
        return 11
    if month_name == "december":
        return 12


def num_days_in(month_num, year):
    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
        return 31
    elif month_num == 2:
        if is_leap(year):
            return 29
        return 28
    else:
        return 30

def num_weeks(month_num, year):
    firstDay = day_of_week(1, month_num, year)

    days_in_month = num_days_in(month_num, year)

    weeks = 1
    for i in range(1, days_in_month + 1):
        if (i + firstDay-1 )%7 == 0 and i != days_in_month:
            weeks += 1
    return weeks


def week(week_num, start_day, days_in_month):
    offset = 0
    var = ''
    if week_num == 1:
        offset = start_day - 1
        if offset > 0:
            print(" " * (3*(offset-1) + 2), end=" ")

        for i in range(1, -start_day + 9):
            if i != -start_day + 8:
                var += "{0:>2}".format(str(i)) + " "
            else:
                var += "{0:>2}".format(str(i))
    else:
        
        if (-start_day + 9) + 7*(week_num-1) > days_in_month:
            cap = days_in_month + 1
        else:
            cap = (-start_day + 9) + 7*(week_num-1)
        for i in range((-start_day + 9) + 7*(week_num - 2), cap):
            if i != (-start_day + 9) + 7 * (week_num - 1) - 1:
                var += "{0:>2}".format(str(i)) + " "
            else:
                var += "{0:>2}".format(str(i))
    return var

def main():
    month = input("Enter month:\n")
    month_number = month_num(month)
    year = eval(input("Enter year:\n"))
    start_day = day_of_week(1, month_number, year)
    lengthOfMonth = num_days_in(month_number, year)
    print(month.title())
    print("Mo Tu We Th Fr Sa Su")
    for i in range(1, num_weeks(month_number, year) + 1):
        print(week(i,start_day, lengthOfMonth))

if __name__=='__main__':
    main()


