'''
Python Word Editor - Version 1.0
Author: Andre Ferreira
'''


import os
import time

'''
    Welcome screen to print the main menu for the user and prompting for an option
'''
def welcomeScreen():
    print("--------------------------------------------------")
    print("             Python Word Editor                   ")
    print("--------------------------------------------------")
    print("1) Create a file")
    print("2) Read a file")
    print("3) Update a file")
    print("4) Delete a file")
    print("--------------------------------------------------")
    user = input(str("\nEnter a number option and press ENTER or type 'q' to quit: "))
    
    # Creating file
    if user == "1":
        text = input(str("\nStart typing: "))
        file_name = input(str("\nEnter file name and press ENTER: "))
        createFile(text, file_name)
    # Reading file
    elif user == "2":
        open_file = input(str("\nEnter the file name plus its extension: "))
        readFile(open_file)
    # Update file
    elif user == "3":
        updt_method = input(str("\nTo append text to a file, press 'a'. To overwrite it, press 'w': "))
        updateFile(updt_method)
    # Deleting file
    elif user == "4":
        dlt_file = input(str("\nFile to be deleted: "))
        deleteFile(dlt_file)
    elif user == "q":
        print("\nExiting program...")
        return -1
    else:
        print("\nOption not valid, my friend! :(")
        
'''
    Function to create a file taking file_name and text as params.
'''
def createFile(text, file_name):
    try:
        text_file = open(file_name, "x")
        text_file.write(text)
        print("File created successfully.")
    except:
        print("\nFile already exists.")  
    finally:
        rtntomenu = input(str("\nPress 'x' to return to main menu: "))
        if rtntomenu.lower() == "x":
            print("\nGoing back to main menu...")
            time.sleep(1)
            os.system("clear")
            time.sleep(1)
            welcomeScreen()           
        else:
            print("Command not found. Exiting the program...")
            return -1
            
'''
    Function to open a file taking open_file as param.
'''
def readFile(open_file):
        try:
            text_file = open(open_file, "rt")
            print("\n", text_file.read())
        except:
            print("\nFile not found. Don't forget to type the extension.")                      
        finally:
            rtntomenu = input(str("\nPress 'x' to return to main menu: "))
            if rtntomenu.lower() == "x":
                print("\nGoing back to main menu...")
                time.sleep(1)
                os.system("clear")
                time.sleep(1)
                welcomeScreen()
            else:
                print("Command not found. Exiting the program...")
                return -1


'''
    Function to update a file by appending a text or overwritting the whole file content.
'''
def updateFile(updt_method):
    # To append to file
    if updt_method.lower() == "a":
        try:
            updt_file = input(str("\nEnter the file name plus its extension: "))
            text_file = open(updt_file, "a")
            updt_text = input(str("\nEnter the new text: "))
            text_file.write(updt_text)
            text_file.close()
            print("\nText added to the file.") 
        except:
            print("\nFile not found. Creating a new one...")           
        finally:
            rtntomenu = input(str("\nPress 'x' to return to main menu: "))
            if rtntomenu.lower() == "x":
                print("\nGoing back to main menu...")
                time.sleep(1)
                os.system("clear")
                time.sleep(1)
                welcomeScreen()
            else:
                print("Command not found. Exiting the program...")
                return -1
    elif updt_method.lower() == "w":
        try:
            updt_file = input(str("\nEnter the file name plus its extension: "))
            text_file = open(updt_file, "w")
            updt_text = input(str("\nEnter the new text: "))
            text_file.write(updt_text)
            text_file.close()
            print("\nFile content overwritten.")
        except:
            print("\nFile not found. Creating a new one...")               
        finally:
            rtntomenu = input(str("\nPress 'x' to return to main menu: "))
            if rtntomenu.lower() == "x":
                print("\nGoing back to main menu...")
                time.sleep(1)
                os.system("clear")
                time.sleep(1)
                welcomeScreen()
            else:
                print("Command not found. Exiting the program...")
                return -1                                                 
    else:
        print("\nOption not valid, my friend! :(")
        rtntomenu = input(str("\nPress 'x' to return to main menu: "))
        if rtntomenu.lower() == "x":
            print("\nGoing back to main menu...")
            time.sleep(1)
            os.system("clear")
            time.sleep(1)
            welcomeScreen()
        else:
            print("Command not found. Exiting the program...")
            return -1

'''
    Function to delete a file taking dlt_file as param.
'''
def deleteFile(dlt_file):
    try:
        os.remove(dlt_file)
        print("File deleted successfully.")
    except:
        print("\nFile not found")                  
    finally:         
        rtntomenu = input(str("\nPress 'x' to return to main menu: "))
        if rtntomenu.lower() == "x":
            print("\nGoing back to main menu...")
            time.sleep(1)
            os.system("clear")
            time.sleep(1)
            welcomeScreen()
        else:
            print("Command not found. Exiting the program...")
            return -1
    


# Entry-point of the program
welcomeScreen()