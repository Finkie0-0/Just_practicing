#Make a retirement calculater
from datetime import date

print("At what age do you want to retire?")
retirement_age = int(input("> "))
print("What is your current age?")
present_age = int(input("> "))

print("What is the current year?")
current_year = date.today()

print("The year is {}".format(current_year.year))

years_till_retirement = retirement_age - present_age
year_of_retirement = current_year.year + years_till_retirement

if years_till_retirement < 0:
    print("You are already retired")
    print("You retired in {}".format(year_of_retirement))
elif years_till_retirement > 0:
    print("You want to retire when you're {} and that will be in {} years from now.".format(retirement_age, years_till_retirement))
    print("The year will be {}".format(year_of_retirement))
else:
    print("Error")