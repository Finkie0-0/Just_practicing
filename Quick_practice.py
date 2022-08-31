# Making a list/To-do list


the_list = []
print("Do you want to add something to the list?")
Do_you_wish_to_add = input("> ")

if Do_you_wish_to_add.lower() == "yes":
    while True:
        print("What do you want to add?")
        add_to_list = input("> ")
        the_list.append(add_to_list)
        if add_to_list == "":
            the_list.remove("")
            break
        elif len(the_list) > 5:
            print("The area is full.")
            break
elif Do_you_wish_to_add.lower() == "no":
    print("Thank you for the visit and I hope you have a lovely day.")

else:
    print("There might be an error please run again.")

print("Here is what's in the list.")
print(the_list)