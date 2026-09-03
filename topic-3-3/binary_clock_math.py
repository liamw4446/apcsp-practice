clock_value = 45
remaining = clock_value

bit_1 = remaining % 2
remaining = remaining // 2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2
remaining = remaining // 2

print(bit_32, bit_16, bit_8, bit_4, bit_2, bit_1)

seconds = 59
next_seconds = (seconds + 1) % 60
print(next_seconds)

clock_values = [13, 42]
labels = ["hours", "minutes"]

clock_values.append(17)
labels.append("seconds")

selected_index = 2

clock_value = clock_values[selected_index]
label = labels[selected_index]

remaining = clock_value
bit_1 = remaining % 2
remaining = remaining // 2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2
remaining = remaining // 2

bits = [bit_32, bit_16, bit_8, bit_4, bit_2, bit_1]

bit_text = str(bits[0])
bit_text = bit_text + str(bits[1])
bit_text = bit_text + str(bits[2])
bit_text = bit_text + str(bits[3])
bit_text = bit_text + str(bits[4])
bit_text = bit_text + str(bits[5])

check_value = (bits[0] * 32 + bits[1] * 16 + bits[2] * 8
			   + bits[3] * 4 + bits[4] * 2 + bits[5] * 1)

# Expected seconds: 17 -> 010001; actual output should match.
print(label + ": " + str(clock_value) + " -> " + bit_text)
print("original:", clock_value)
print("reconstructed:", check_value)
