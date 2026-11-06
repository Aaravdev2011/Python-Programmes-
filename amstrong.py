
user_input = input("Enter a number: ")
num = int(user_input)

power = len(user_input)
total_sum = 0
for digit_char in user_input:
    total_sum += int(digit_char) ** power


if num == total_sum:
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is NOT an Armstrong number.")
