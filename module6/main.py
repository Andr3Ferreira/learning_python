'''
The Grocery List - Version 1.0
Author: Andre Ferreira
Description: A tool to authenticate real video games, with real parameters used to validate disks.
'''

# Dictionary to be use as reference to check the games
games = {
    "Pac Man World": '40394',
    "Game of Life": '69302', 
    "Call of Duty: Big Red One": '76034',
    "Cardinal Syn": '40395', 
    "NHL '99": '22490'
}

# Global variables to be used in the functions
game_title = False
disk_number = False
serial_number = False
result = False

# You must create an interface that accepts the following user input:
def welcomeScreen():
    # while(True):    

        print("\n")
        print("==================================================")
        print("        PythonCo. Disk Validation Checker        ")
        print("==================================================")
        name = input(str("Enter in the name of the disk name and press ENTER: "))
        number = int(input("Enter in the disk number and press ENTER: "))
        serial = input(str("Enter in the disk serial number and press ENTER: "))
        print("\n\nRESULTS")
        print("==================================================")

        '''
            Function that use conditional statements to
            validate if the user’s input matches a list of games based on the
            table above.
            @param: name
            @return: game_title
        '''
        def inList(name):
            global game_title
            if str(name).lower() in str(games).lower():
                game_title = True
                # return game_title
            else:
                game_title = False

            return game_title
            
        ''' 
            Function should accept a number from the
            user’s input and determine if said input is starting with, between
            or ending with the numbers 1496833 and 5930214.
            @param: number
            @return: disk_number
        '''
        def numberMatch(number):
            global disk_number
            if number in range(1496833, 5930215):
                disk_number = True
            else:
                disk_number = False
            
            return disk_number

        '''
            Function should use conditional statements to validate if the user’s 
            input matches a dictionary of games and serial numbers based on the table above.
            @param: serial
            @return: serial_number
        '''
        def serialMatch(serial, name):
            global serial_number
            try:
                if serial in games.values() and serial == games[name]:
                    serial_number = True
                    # return serial_number
                else:
                    serial_number = False
                    # return serial_number
            except:
                print("Try capitalizing every word of the game's name.")
            finally:
                return serial_number

        '''
            Function to check if the game title matches, number matches, as well as the serial number. 
            @param: game_title, disk_number, serial_number
            @return: result
        '''
        def results(game_title, disk_number, serial_number):
            print("On Disk List:                ", game_title)
            print("Disk Number Match:           ", disk_number)
            print("Disk Serial Number Match:    ", serial_number)

            global result
            if(game_title == True and disk_number == True and serial_number == True):
                result = True
            elif(game_title == False or disk_number == False or serial_number == False):
                result = False
            else:
                print("\nSomething went wrong. Exiting the program...")
                return -1

            return result

        '''
            Function to return the final result, indicating if the disk is genuine or a pirated copy.
            @param: result
        '''
        def veredict(result):
            if result == True:
                print("\nTHIS IS A GENUINE DISK")
            else:
                print("\nTHIS IS NOT A GENUINE DISK")
            

        # Functions calls
        inList(name)
        numberMatch(number)
        serialMatch(serial, name)
        results(game_title, disk_number, serial_number)
        veredict(result)

# Entry-point of the program
welcomeScreen()