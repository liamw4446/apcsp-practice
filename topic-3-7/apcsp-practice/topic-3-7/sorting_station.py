label = input()

shape = label[0:4]
color = label[4:7]
size = int(label[7:10])
mass = int(label[10:14])
condition = label[14]

if condition == "D" < 50 or mass > 2000:
    print("INSPECT")
elif color == "RED" and shape == "BALL" and size > 10:
    print("B")
elif shape == "BALL":
    print("A")
elif color == "BLUE" or color == "GREEN" and size <= 10:
    print("C")
elif shape == "CUBE":
    print("D")
else:
    print("E")

