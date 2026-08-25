mins_available = int(input("minutes available: "))
breaks = int(input("number of breaks: "))
break_minutes = int(input("minutes per break: "))
transportation_minutes = int(inputs("Minutes for transportation"))

work_minutes = minutes_available - breaks * break_minutes - transportation_minutes

print("focused work minutes: ", work_minutes)