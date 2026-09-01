clock_value = 45
remaining = clock_value

bit_1 = remaining % 2
remaining = remaining //2
bit_2 = remaining % 2
remaining = remaining //2
bit_4 = remaining % 2
remaining = remaining //2'
bit_8 = remaining % 2
remaining = remaining //2
bit_16 = remaining % 2
remaining = remaining //2
bit_32 = remaining % 2
remaining = remaining //2

print(bit_32, bit_16, bit_8, bit_4, bit_2, bit_1)

seconds = 59
next_seconds = (seconds + 1) % 60
print(next_seconds)

selected_index = 2

clock_values = [13, 42, 17]
label = "seconds"