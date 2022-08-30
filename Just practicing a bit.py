# Calculator

def add():
      print("What do you want to add? ")
      a = int(input("> "))
      b = int(input("> "))
      return a + b

def sub():
      print("What do you want to sub? ")
      a = int(input("> "))
      b = int(input("> "))
      return a - b

def mul():
      print("What do you want to mult? ")
      a = int(input("> "))
      b = int(input("> "))
      return a * b

def div():
      print("What do you want to div? ")
      a = int(input("> "))
      b = int(input("> "))
      return a / b

def rem():
      print("Which numbers are divisible? ")
      a = int(input("> "))
      b = int(input("> "))
      return a % b

while True:
      print("What do you want to do? (add), (sub), (mul), (div) or (rem)")
      sign = input("> ")
      if sign.lower() == "add":
            print("Your answer is: '{}'".format(add()))
      elif sign.lower() == "sub":
            print("Your answer is: {}".format(sub()))
      elif sign.lower() == "mul":
            print("Your answer is: {}".format(mul()))
      elif sign.lower() == "div":
            print("Your answer is: {}".format(div()))
      elif sign.lower() == "rem":
            print("Your answer is: {}".format(rem()))
      elif sign.lower() == "":
            break
      else:
            continue








