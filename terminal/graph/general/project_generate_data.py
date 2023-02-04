import random
import time

CSV = True
PRETTY = True
NUMBER = 1000
MIN = 0
MAX = 1000

T = time.localtime(time.time())
with open(f"data_{T.tm_mday}_{T.tm_sec}."+"csv" if CSV else "txt","w") as f:
    if not CSV:
        f.write("0\n")
        for x in range(NUMBER):
            f.write(str(random.randrange(MIN,MAX)) + " , " + str(random.randrange(MIN,MAX)) + "\n")
    else:
        f.write("["+"".join([("\n" if PRETTY else "")+f"({random.randrange(MIN,MAX)},{random.randrange(MIN,MAX)})," for x in range(NUMBER)])[:-1] +"]")
