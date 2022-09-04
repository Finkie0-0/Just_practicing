#Current price and the price update

print("What is the price for the product.")
price = int(input("> "))
print("What day is it today? Mon,Tue,Wed,Thu,Fri,Sat or Sun.")
date = str(input("> "))
if date.lower() == "monday" or date.lower() == "mon":
    print("We have a discount for today hope you have a lovely day today")
    if price >= 100:
        tot = price - (price * 0.28)
        save = price * 0.28
    else:
        tot = price - (price * 0.18)
        save = price * 0.18
    print("The total is: ${}, you saved ${}.".format(tot, save))
elif date.lower() == "tuesday" or date.lower() == "tue":
    print("No parties today but we got a discount today.")
    if price >= 100:
        tot = price - (price * 0.22)
        save = price * 0.22
    else:
        tot = price - (price * 0.12)
        save = price * 0.12
    print("The total is: ${}, you saved ${}.".format(tot, save))
elif date.lower() == "friday" or date.lower() == "fri":
    print("You know what happens when the sun goes down so strap on and get ready for the day.")
    if price >= 100:
        tot = price - (price * 0.2)
        save = price * 0.2
    else:
        tot = price - (price * 0.10)
        save = price * 0.10
    print("The total is: ${}, you saved ${}.".format(tot, save))
else:
    print("Sadly today we don't have a discount especially on Sunday so sorry about that.")
    if price >= 100:
        tot = price - (price * 0.1)
        save = price * 0.1
    else:
        tot = price
        save = 0
    print("The total is: ${}, you saved ${}.".format(tot, save))

