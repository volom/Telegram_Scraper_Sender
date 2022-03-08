# use this script to send messages to several receivers from file "members.csv"

from auth_info import *
from send_msg import send_message
import os
import time

txt_msg = open(f"{os.getcwd()}//text_msg.txt", 'r').read()
def run():
    with open('members.csv', 'r') as m:
        for receiver in m.readlines()[1:]:
            receiver = receiver.split('\t')[0]
            receiver = f"@{receiver}"
            try:   
                send_message(receiver, txt_msg)
                print(f"The message was sent to {receiver}")
                time.sleep(10)
            except Exception as e:
                print("------------------------")
                print(f"The error occurred with {receiver}:")
                print(str(e))
                print("------------------------")

if __name__ == "__main__":
    run()
