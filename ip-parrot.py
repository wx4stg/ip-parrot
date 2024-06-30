#!/usr/bin/python3
# Sends IP address to Sam
# Created 13 August 2022 by Sam Gardner <stgardner4@tamu.edu>

import socket
import requests


PI_NAME = ""
API_KEY = ""

shouldTryAgain = True
while shouldTryAgain:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ipaddr = s.getsockname()[0]
        s.close()
        shouldTryAgain = False
    except:
        print("no connection yet, trying again")
dataToPost = {"text" : f"{PI_NAME}: {ipaddr}", "bot_id" : API_KEY}
print(dataToPost)
res = requests.post("https://api.groupme.com/v3/bots/post", json=dataToPost)
print(res)

