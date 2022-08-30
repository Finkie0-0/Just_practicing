#Try to make a while loop for project
To_do_list = []

while True:
    add = str(input(">> "))
    To_do_list.append(add)
    if add == "":
        To_do_list.remove("")
        break
print(f"Your list {To_do_list}")