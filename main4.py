import math

height = float(input("Enter wall height (feet):\n"))
width = float(input("Enter wall width (feet):\n"))
wall_area = int(height * width)

print("Wall area:", wall_area, "square feet")

paint = wall_area / 350

print("Paint needed:", '{:.2f}'.format(paint), "gallons")
print("Cans needed:", math.ceil(paint), "can(s)")

color = input("\nChoose a color to paint the wall:\n")
colorpick = {'red': 35, 'blue': 25, 'green': 23}

print("Cost of purchasing", color, "paint: $%d" % (colorpick[color]*math.ceil(paint)))
