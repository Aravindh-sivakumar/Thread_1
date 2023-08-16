print("******************PBMS****************")
pb={}
while True:
    print("1: Add contact")
    print("2: Display contact")
    print("3: Search contact")
    print("4: Delete contact")
    print("5: Edit contact")
    print("0: Exit")


    ch = int(input("Enter your choice:  "))

    if(ch == 1):
        print("Adding a contact")
        new_name= input("Enter Name: ")
        new_num= int(input("Enter Number: "))
        pb[new_name] = new_num
        print("New contact is added")
        print(pb)


    elif(ch == 2):
        print("Displaying a contact")
        for k,v in list (pb.items()):
         print("Name", k)
         print("Ph num", v)
         print("********************")


    elif(ch == 3):
        print("searching a contact")
        name = input("Enter name: ")
        if name in pb:
            print(f"Name: {new_name}, Number: {pb[new_name]}")

    elif(ch == 4):
        print("Deleting a contact")
        if new_name in pb: 
            del pb [new_name]  

    elif(ch == 5):
        print("Editing a contact")    
        name = input("Enter name: ")
        if name in pb:
            new_number= int(input("Enter new number:")) 
            pb[name] = new_number     
    elif(ch == 0):
        print("Exiting a contact")
        break
    else:
        print("Wrong choice")    