from auth_info import *

#Sender function
def send_message(user_details, message_content):
    #Initialise telegram client with API codes
    # start the process
    #Send the message
    client.send_message(user_details, message_content)