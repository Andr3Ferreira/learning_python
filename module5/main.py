'''
The Grocery List - Version 1.0
Author: Andre Ferreira
Description: Simple grocery list program that can be viewed, and items can be added or removed as we pick them up.
'''


# List constructor accessible from anywhere within this class
groceries = list()

# Welcome screen that shows three options for the user: View Grocery List, Add groceries, and Remove Groceries
def welcomeScreen():
    while(True):    
        print("\n")
        print("--------------------------------------------------")
        print("                 Grocery List                  ")
        print("--------------------------------------------------")
        print("1) View grocery list")
        print("2) Add a item to the list")
        print("3) Remove a item from list")
        print("--------------------------------------------------")
        option = input(str("\nEnter a number option and press ENTER or type 'q' to quit: "))

        # Prints the whole list
        if option == "1":
            for i in groceries:
                print(f"> ", str(i).capitalize())
            menu = input("\nPress ENTER to return to main menu")
        # Adds a new item to the list and displays it
        elif option == "2":
            item = input(str("\nItem: "))
            if item == "":
                print("Please enter an item")
            else:
                groceries.append(item)
            
            for i in groceries:
                print(f"> ", str(i).capitalize())

            menu = input("\nPress ENTER to return to main menu")
        # Removes a item from the list and displays it
        elif option == "3":
            item = input(str("\nChoose an item to be removed: "))
            try:
                groceries.remove(item)
            except:
                print("Item not in the list")

            for i in groceries:
                print(f"> ", str(i).capitalize())

            menu = input("\nPress ENTER to return to main menu")
        # Exits the program
        elif option == "q":
            print("\nExiting program...")
            return -1
        # Invalid option
        else:
            print("\nOption not valid, my friend! :(")
            menu = input("Press ENTER to return to main menu")


# Entry-point of the program
welcomeScreen()