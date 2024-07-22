import string
import secrets

# Function to generate the password
def get_password(length: int, exclude_duplicates: bool) -> str:
    # Creating data
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+']
    numbers = [str(a) for a in range(10)]
    lowercase_characters = string.ascii_lowercase
    uppercase_characters = string.ascii_uppercase

    # Variable to hold the password
    password = ''

    # Adding one symbol
    password += secrets.choice(symbols)

    # Adding one number
    password += secrets.choice(numbers)

    # Adding one lowercase character
    password += secrets.choice(lowercase_characters)

    # Adding one uppercase character
    password += secrets.choice(uppercase_characters)

    # Now run a for loop starting from the current length of the password
    # all the way to the maximum length to fill in the remaining data
    while len(password) < length:
        # Adding all the data together into one list
        characters = lowercase_characters + uppercase_characters
        data = symbols + numbers + list(characters)

        # Getting a random character from the list
        random_char = secrets.choice(data)

        # If asked to exclude duplicates
        if exclude_duplicates:
            # If character not already inside the password
            # then add it into the password
            if random_char not in password:
                password += random_char
        else:  # If not asked to exclude duplicates
            # Then just add the character without checking
            password += random_char

    # Create a list of the password
    password_list = list(password)
    # Shuffle the list into a random sequence
    password = shuffle(password_list)

    # Returning the password
    return password

# Shuffle function based on Fisher–Yates shuffle using secrets.choice()
# as the integer selector
def shuffle(password: list) -> str:
    # n used to determine the range of loop
    n = len(password)
    for x in range(n - 1, 0, -1):
        # Set new variable y to random int within needed index
        y = secrets.choice(range(0, x + 1))
        # Swap elements at index x and index y
        password[x], password[y] = password[y], password[x]
    # Return concatenated password
    return ''.join(password)

# Main method
def main() -> None:
    # Taking the length of the password from user input
    length = int(input("Enter the length of the password: "))

    # Asking the user whether to exclude duplicates
    exclude_duplicates_input = input("Exclude duplicate characters? (yes/no): ").strip().lower()
    if exclude_duplicates_input == 'yes':
        exclude_duplicates = True
    else:
        exclude_duplicates = False

    # This will hold the final password
    password = get_password(length, exclude_duplicates)

    # Printing the password to the user
    print(f'PASSWORD: {password}')

if __name__ == '__main__':
    # Calling the main method
    main()
