#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Declare the number of letters, symbols, and numbers to be generated
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

# Declare an empty list to store the generated characters
password_list = []

# Generate random letters and add them to the password list
for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

# Generate random numbers and add them to the password list
for char in range(nr_numbers):
  password_list += random.choice(numbers)

# Shuffle the password list to randomize the order of the characters
random.shuffle(password_list)

# Declare an empty string to store the final password
password = ""

# Iterate through the password list and add each character to the final password string
for char in password_list:
  password += char

print(f"Your password is: {password}")