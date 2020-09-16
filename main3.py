lemon_juice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave_nectar = float(input("Enter amount of agave nectar (in cups):\n"))
serving = float(input("How many servings does this make?\n"))

print("\nLemonade ingredients - yields", '{:.2f}'.format(serving), "servings")
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave_nectar), "cup(s) agave nectar")

serving1 = int(input("\nHow many servings would you like to make?\n"))
lemon_juice1 = (serving1 * lemon_juice) / serving
water1 = (serving1 * water) / serving
agave_nectar1 = (serving1 * agave_nectar) / serving

print("\nLemonade ingredients - yields", '{:.2f}'.format(serving1), "servings")
print('{:.2f}'.format(lemon_juice1), "cup(s) lemon juice")
print('{:.2f}'.format(water1), "cup(s) water")
print('{:.2f}'.format(agave_nectar1), "cup(s) agave nectar")

lemon_juice2 = lemon_juice1 * 0.0625
water2 = water1 * 0.0625
agave_nectar2 = agave_nectar1 * 0.0625

print("\nLemonade ingredients - yields", '{:.2f}'.format(serving1), "servings")
print('{:.2f}'.format(lemon_juice2), "gallon(s) lemon juice")
print('{:.2f}'.format(water2), "gallon(s) water")
print('{:.2f}'.format(agave_nectar2), "gallon(s) agave nectar")
