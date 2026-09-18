label = input()

shape = label[0:4]
color = label[4:7]
size = int(label[7:10])
mass = int(label[10:14])
condition = label[14]

if condition == "D" or size > 50 or mass > 2000:
    destination = "INSPECT"
elif shape == "BALL":
    if color == "RED" and size > 10:
        destination = "B"
    else:
        destination = "A"
elif shape == "CUBE":
    if (color == "BLU" or color == "GRN") and size <= 10:
        destination = "C"
    else:
        destination = "D"
else:
    destination = "E"

print(destination)