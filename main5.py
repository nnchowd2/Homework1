print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

service1 = input("Select first service:\n")
service2 = input("Select second service:\n\n")

servicelist = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

if service2 == "-":
    print("Davy's auto shop invoice\n")
    print("Service 1:", service1 + ",", "$%d" % servicelist[service1])
    print("Service 2: No service")
elif service1 == "-":
    print("Davy's auto shop invoice\n")
    print("Service 1: No service")
    print("Service 2:", service2 + ",", "$%d" % servicelist[service2])
else:
    print("Davy's auto shop invoice\n")
    print("Service 1:", service1 + ",", "$%d" % servicelist[service1])
    print("Service 2:", service2 + ",", "$%d" % servicelist[service2])

print("\nTotal:", "$%d" % (servicelist[service1]+servicelist[service2]))
