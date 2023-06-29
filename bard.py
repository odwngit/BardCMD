from bardapi import Bard
import os
import sys
if sys.argv[1] == "key":
    if sys.argv[2] == "get":
        f = open(r'C:/BardCMD/key', 'r')
        print(f.read())
        f.close()
    elif sys.argv[2] == "set":
        f = open(r'C:/BardCMD/key', 'w')
        f.write(sys.argv[3])
        f.close()
        print(f"Bard API Key (Cookie 1PSID) set to: {sys.argv[3]}")
elif sys.argv[1] == "answer":
    f = open(r'C:/BardCMD/key', 'r')
    request = " ".join(sys.argv[2:])
    bard = Bard(token = f.read())
    print(bard.get_answer(request)['content'])
    f.close()