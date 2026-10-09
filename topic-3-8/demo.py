battery = int(input("Starting battery %: "))
minutes = int(input("Minutes plugged in: "))

charge_per_minute = 2

for i in range(minutes):
    battery = battery + charge_per_minute
    if battery > 100:
        battery = 100

print("Battery is now", battery, "%")