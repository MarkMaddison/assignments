a = {'Mark ':'05003002010','Edward':'05325323200','David':'05425420000'}
b = a.items()
print() 
for i in a.keys():
    print(i, "-", a[i])
x = True
print()
while x == True:
    print('What Do you want to do?',"1. Create new log","2. Edit an existing log", "3. Delete a log","4. Display current entries", "5. Exit", sep="\n")
    choice = input('Your choice : ')
    if choice not in ("1","2","3","4","5","6","7","8","9","0"):
        print("Please enter your choice between (1-5)")
    else : 
        choice = int(choice)
    if choice == 1:
        cr1 = input('Enter name : ')
        cr2 = input('Phone Number : ')
        a[cr1] = cr2
        print(cr1,cr2,"Already added your phone book")
        print()
    elif choice == 2:
        ed = input("Which log? : ")
        ed1 = input("Enter new name : ")
        ed2 = input("Input new number : ")
        del a[ed]
        a[ed1] = ed2
        print(ed1,"-",ed2, "saved")
        print()
    elif choice == 3:
        rm = input("Which log? : ")
        del a[rm]
        print(rm, "Deleted succesfully")
        print()
    elif choice == 4:
        print("-----------")
        for i in a.keys():
            print(i, "-", a[i])
        print("-----------")
    elif choice not in range (1,6):
        print()
        print("Please enter your choice between (1-5)")
        print()
    elif choice == 5:
        x = False

