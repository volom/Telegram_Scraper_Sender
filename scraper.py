# use this script for scraping group members info

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv
from auth_info import *

#client = TelegramClient(session_name, api_id, api_hash)
# start the process
#client.start()
chats = []
last_date = None

# set the limit of members amount
chunk_size = 10000

groups = [] 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        # if chat.megagroup == True:
        #     groups.append(chat)
        groups.append(chat)
    except:
        continue

# sort groups by alphabetic order
groups.sort(key=lambda x: x.title, reverse=False)

print('Choose a group to scrape members from:')

i = 0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Enter a Number: ")
target_group=groups[int(g_index)]

print('Fetching Members...')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=False)

print('Saving In file...')
with open("members.csv", "a", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n")
    #writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])      

print('Members scraped successfully.')