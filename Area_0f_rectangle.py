#Area of a rectangle

Const = 0.0929
print("Enter the room length in american(feet): ")
lenght_in_feet = int(input("> "))
print("Enter the width in american(feet): ")
width_in_feet = int(input("> "))
area = lenght_in_feet * width_in_feet
area_in_meters = area * Const

if area and area_in_meters < 0:
    print("Did you mistype your input?")

else:
    print("Your entered dimensions are {} by {}".format(lenght_in_feet, width_in_feet))
    print("Area in: ")
    print("Area in feet: {}".format(area))
    print("Area in meters squared: {:0>2f}".format(area_in_meters))

