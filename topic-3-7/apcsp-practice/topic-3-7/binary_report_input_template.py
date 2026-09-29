clock_values = [13, 42]
labels = ["hours", "minutes"]

clock_values.append(17)
labels.append("seconds")

selected_index = 2
label = labels[selected_index]

while True:
    try:
        clock_value = int(input(f"Enter a value for {label} (0-63): "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    if 0 <= clock_value <= 63:
        clock_values[selected_index] = clock_value
        break

    print("Please enter a number between 0 and 63.")

remaining = clock_value

bit_1 = remaining % 2
remaining //= 2
bit_2 = remaining % 2
remaining //= 2
bit_4 = remaining % 2
remaining //= 2
bit_8 = remaining % 2
remaining //= 2
bit_16 = remaining % 2
remaining //= 2
bit_32 = remaining % 2

bits = [bit_32, bit_16, bit_8, bit_4, bit_2, bit_1]
bit_text = "".join(str(bit) for bit in bits)

check_value = (
    bits[0] * 32 + bits[1] * 16 + bits[2] * 8 +
    bits[3] * 4 + bits[4] * 2 + bits[5] * 1
)

print(f"{label}: {clock_value} -> {bit_text}")
print("original:", clock_value)
print("reconstructed:", check_value)

if clock_value % 2 == 0:
    print("Even")
else:
    print("Odd")