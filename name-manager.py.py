names = []

while True:
    print("\nMenu:")
    print("1. Add a name")
    print("2. View names")
    print("3. Cancel name addition")
    print("4. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        new_name = input("Enter a name to add: ")
        names.append(new_name)
    elif choice == '2':
        if not names: 
            print("No names to display.")
        else: 
            print("Names in the list:")
            for i , n in enumerate(names, start=1):
                print(f"{i}. {n}")
    elif choice == '3':
        if names:
            remove_name = input("Enter the name to remove: ")
            if remove_name in names:
                names.remove(remove_name)
                print(f"{remove_name} has been removed.")
            else:
                print(f"{remove_name} not found in the list.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

    

