# This project is building a list


list_of_names = []

while True:
    print(f"Do you want to add a name to the list?")
    answer = str(input(">>"))
    list_of_names.append(answer)
    if answer == "":
        list_of_names.remove('')
        break
    elif answer == "Arnold":
        print("Welcome back my guy")
    else:
        continue

print("The list Created: \n {}".format(list_of_names))