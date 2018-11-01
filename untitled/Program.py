#Journal Project

def printH():
    print("___________________")
    print("Journal App")
    print("-------------------")

def Run_Event_Loop():
    print("What do you want to do with your journal? ")
    Command = None
    Journal_Data = [] #List()

    while Command != "x":
        Command = input("[L]ist entries, [A]dd new entry, E[x]it Application: ")
        Command = Command.lower().strip()

        if Command == "l":
            List_entries(Journal_Data)
        elif Command == "a":
            Add_entries(Journal_Data)
        elif Command != "x":
            print("Unknown Command. Please Try Again")

def List_entries(Data):
    print("Here are all entries so far.")
    entries = reversed(Data)
    for index,entry in enumerate(entries):
        print(entry)

def Add_entries(Data):
    Text = input("Type entry here, When done press <enter>")
    Data.append(Text)
    print("Saved")

def Exit_Application():
    pass




def Main():
    printH()
    Run_Event_Loop()

Main()