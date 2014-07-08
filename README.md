bsjtfgrue
=========

My solution for the BSJTF Grue Challenge

Puzzle 1: You might want to turn on your flashlight

Puzzle 2: You needed to fuzz the keypad, it only checked the first charictors for "admin", and trimed that. Fuz with spaces

Puzzle 3: 
- Take the matches
- Helps to light the match before the candle
- Light the Candle
- Moving the carpet shows a lock, you can't pick your nose, or the lock :(
- Lighting the candle yielded some numbers. I just brute forced the code. See lock-bruteforce.log

Puzzle 4: 
- Look at the paper!
- Call the phone number
- Decode modem sounds using minimodem
-- I had a problem here with the version of minimodem - needed 0.8.1
-- See room.txt
- You needed to press the buttons in the order of the Konami code - you can press buttons more then once
- Finally, press the green button

Puzzle 5:
- ls to find the knockknock.py file
- cat to see and copy/paste the file (You can't run it on the "laptop")
- Google "First Hacker rats" and find this page: http://wizzley.com/first-hacker-marconi-wireless-1903/
- Rats goes into the DitDaw veriable, use RATS in ditdaw ...--- Style
- Note, https://github.com/coolacid/bsjtfgrue/blob/master/knockknock.py#L18 does some interesting things at 00 and 30secs.
- "Laptop" has date command to get the date!
- Send the required information, and date from "laptop" into the getaccess function
- use the 'history' command on the "laptop" and see a netcat command
- Send the generated password to the "server"

Profit.

