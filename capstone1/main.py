'''
    Description: Tool to analyze user requests.
    Author(s): Andre Ferreira
    Version 1.0
    Last updated: 18/03/2023
'''

import ipaddress


# Main function to welcome the user and invoke other functions
def welcomeView():
    iOs = input(str("\nOperating System: "))
    # Requirement 1 - Create a request:
    #The application must be able to create a request and store it in a file
    # createRequest(iUrl, iHostip, iUserip, iLocation, iOs, iDevice)

    #Requirement 2 - Read a request:
    #The application must be able to read the request from a file
    # readRequest(iUrl, iHostip, iUserip, iLocation, iOs, iDevice)

    #Requirement 3 - Determine if the request is malicious
    #The application must be able to take that request file and determine if the request is malicious.
    #Requirement 4 - Add malicious requests to "blocked list"
    #The application must be able to take malicious requests and add them to a separate “blocked list”
    # checkingRequest(iUrl, iHostip, iUserip, iLocation, iOs, iDevice)

    #Requirement 5- View blocked requests
    #The application finally must be able to show a list of blocked requests
    # blockedList()

def checkingRequest(iUrl, iHostip, iUserip, iLocation, iOs, iDevice):

    # Baseline constants
    URL = "www.allsafe.io/security/tunnel/POD:2208"
    
    host_ip = int(ipaddress.IPv4Address(host_ip))
    HOST_MIN = int(ipaddress.IPv4Address("10.0.24.123"))
    HOST_MAX = int(ipaddress.IPv4Address("12.1.23.164"))

    user_ip = int(ipaddress.ip_address(user_ip))
    USER_MIN = int(ipaddress.ip_address("234.305.0.21"))
    USER_MAX = int(ipaddress.ip_address("430.640.1.63"))

    LOCATION = "Toronto"
    OS = "Windows"
    DEVICE = "Desktop"
    BLOCKED = "blocked"


    class Request:
        def __init__(self, iUrl, iHostip, iUserip, iLocation, iOs, iDevice):
            self.url = iUrl
            self.host_ip = iHostip
            self.user_ip = iUserip
            self.location = iLocation
            self.os = iOs
            self.device = iDevice
      
        def osCheck(self):
            if iOs == "Windows":
                os = Request(OS)
                print(self.os)
                return os
                # os.osCheck()
            else:
                print(BLOCKED)
                

    # if url == URL:
    #     return url
    # else:
    #     url = BLOCKED
    #     print(url)

    # if host_ip in range(HOST_MIN, HOST_MAX+1):
    #     return str(ipaddress.ip_address(host_ip))
    # else:
    #     host_ip = BLOCKED
    #     print(host_ip)

    # if user_ip in range(USER_MIN, USER_MAX+1):
    #     return str(ipaddress.ip_address(user_ip))
    # else:
    #     user_ip = BLOCKED
    #     print(user_ip)

    # if location == LOCATION:
    #     return location
    # else:
    #     location = BLOCKED
    #     print(location)

    # if iOs == OS:
    #     os = Request(OS)
    #     return os
    #     # os.osCheck()
    # else:
    #     print(BLOCKED)
         

    # if device == DEVICE:
    #     return device   
    # else: 
    #     device = BLOCKED
    #     print(device)


# def createRequest(iUrl, iHostip, iUserip, iLocation, iOs, iDevice):
#     print("\nCreate a request: ")
#     iUrl = input(str("\nReferrer URL: "))
#     iHostip = input(str("\nHost-IP: "))
#     iUserip = input(str("\nUser-IP: "))
#     iLocation = input(str("\nUser Location: "))
#     iOs = input(str("\nOperating System: "))
#     iDevice = input(str("\nDevice: "))

#     checkingRequest(iUrl, iHostip, iUserip, iLocation, iOs, iDevice)

# def readRequest():
#     pass

# def blockedList():
#     block = open("write.txt", "a")
#     block.write()


welcomeView()