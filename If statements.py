import random

options = ["A","B","C","D"]
lenght = 1
pick = "".join(random.sample(options,lenght))


if pick == "A":
    print(f"Your answer is {pick} and the index is {options.index(pick)}")
elif pick == "B":
    print(f"Your answer is {pick} and the index is {options.index(pick)}")
elif pick == "C":
    print(f"Your answer is {pick} and the index is {options.index(pick)}")
elif pick == "D":
    print(f"Your answer is {pick} and the index is {options.index(pick)}")