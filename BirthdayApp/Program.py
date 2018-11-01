#Birthday Program
import datetime

def printH():
    User_Name = input("Hello. Welcome to the Birthday Tracker Application. Please  enter your name: ")

def GetBirthDay():
    #User Inputes Birthday
    print()
    DateY = input("Please put the year you where born [YYYY]: ")
    DateM = input("Please put the year you where born [MM]: ")
    DateD = input("Please put the year you where born [DD]: ")

    #tranform string to int.
    year = int(DateY)
    month = int(DateM)
    day = int(DateD)

    bday = datetime.date(year,month,day)

    return bday

#calculate days till birthday from today pass in 2 days
def CalDaysinDates(Original_Year,Target_Year):
    This_Year = datetime.date(Target_Year.year,Original_Year.month, Original_Year.day)

    dt = This_Year - Target_Year

    return dt.days



def printBday(days):

    if days > 0:
        print("You have {} days until your birthday!".format(-days))
    elif days < 0:
        print("Your Birthday passed {} days ago!".format(days))
    else:
        print("Happy Birthday")



#Ties all functions together in execution oder
def main():
    printH()
    bday = GetBirthDay()
    today = datetime.date.today()
    Number_of_days = CalDaysinDates(bday, today)
    printBday(Number_of_days)

main()

