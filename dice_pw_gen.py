#!/usr/bin/env python3

### Diceware Password generator by Leon M ###
### version 1                             ###

import json
from secrets import SystemRandom

random = SystemRandom()
script_dir = __file__.rsplit("/", 1)[0]
wordlist = json.loads(open(f"{script_dir}/diceware.json", 'rt').read())

# lambda function to roll 6 dice and join into string.
num_test = lambda: "".join([str(random.randint(1, 6)) for _ in range(5)])
# lambda function to join y number of words into a passphrase
password = lambda y: "".join([wordlist.get(num_test()) + str(random.randint(0, 9)) for _ in range(y)])

print(f"{password(4)}")