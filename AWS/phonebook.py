a = {'a':'123','b':'456','c':'321'}
b = a.items()
print() 
for i in a.keys():
    print(i, "-", a[i])
x = True
print()
while x == True:
    print('What Do you want to do?',"1. Create new log","2. Edit an existing log", "3. Delete a log","4. Display current entries", "5. Exit", sep="\n")
    choice = int(input('Your choice : '))
        if choice == 1:
        cr1 = input('Enter name :')
        cr2 = input('Phone Number :')
        a[cr1] = cr2
        print(cr1,cr2,"Already added your phone book")
    elif choice == 2:
        ed = input("Which log? :")
        ed1 = input("Enter new name : ")
        ed2 = input("Input new number : ")
        del a[ed]
        a[ed1] = ed2
    elif choice == 3:
        rm = input("Which log? :")
        del a[rm]
        print(rm, "Deleted succesfully")
    elif choice == 4:
        for i in a.keys():
            print(i, "-", a[i])
    elif choice not in range (1,6):
        print()
        print("Please enter your choice between (1-5)")
        print()
    elif choice == 5:
        x = False
