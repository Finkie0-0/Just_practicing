#Heads I study a little bit and Tails im done for the day
import random

coin = ["heads", "tails"]
length = 1
result = "".join(random.sample(coin,length))

if result == "heads":
    print("It is '{}'.".format(result))
else:
    print("It is '{}'.".format(result))