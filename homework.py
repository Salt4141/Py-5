import random

num = round(random.random() * 10, 0) % 6

if num == 1:
    print("[       ]")
    print("[   0   ]")
    print("[       ]")

if num == 2:
    print("[       ]")
    print("[ 0   0 ]")
    print("[       ]")

if num == 3:
    print("[ 0     ]")
    print("[   0   ]")
    print("[     0 ]")

if num == 4:
    print("[ 0   0 ]")
    print("[       ]")
    print("[ 0   0 ]")

if num == 5:
    print("[ 0   0 ]")
    print("[   0   ]")
    print("[ 0   0 ]")

if num == 6:
    print("[ 0   0 ]")
    print("[ 0   0 ]")
    print("[ 0   0 ]")