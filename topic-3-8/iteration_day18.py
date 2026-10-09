n = 6
step_limit = 1000
value_limit = 1000000

steps = 0
peak = n
print(n)

while n != 1 and steps < step_limit and n <= value_limit:
    if n % 2 == 0:
        n = n // 2  
    else:
        n = 3 * n + 1    
    steps = steps + 1
    if n > peak:
        peak = n
    print(n)

print("Transformations:", steps)
print("Peak:", peak)
print("Final value:", n)
if n == 1:
    print("REACHED 1")
else:
    print("LIMIT REACHED")