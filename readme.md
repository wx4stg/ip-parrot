# IP Parrot
-----

Installation: 

`git clone https://github.com/wx4stg/ip-parrot`

This will download the repository to your raspberry pi. Once this is done, use a text editor such as `nano` to add the Pi's name to `PI_NAME` and your groupme bot API key to `API_KEY`. You can obtain a groupme bot API key from https://dev.groupme.com/bots

`cd ip-parrot`

`cp ip-parrot.py /home/pi/`

`sudo cp ip-parrot.service /etc/systemd/system/`

`sudo systemctl enable ip-parrot.service`


