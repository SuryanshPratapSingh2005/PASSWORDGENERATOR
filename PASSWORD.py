import random

def generate_password(length, complexity):
    """Generates a strong and random password of the specified length and complexity.

    Args:
        length: The length of the password.
        complexity: The complexity of the password, which can be "low", "medium", or "high".

    Returns:
        A strong and random password.
    """

    characters = []
    if complexity == "low":
        characters = ["abcdefghijklmnopqrstuvwxyz", "0123456789"]
    elif complexity == "medium":
        characters = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "!@#$%^&*()"]
    elif complexity == "high":
        characters = ["abcdefghijklmnopqrstuvwxyz", "0123456789", "!@#$%^&*()_+-=[]{};:'<,>./"]

    password = ""
    for i in range(length):
        character_set = random.choice(characters)
        password += random.choice(character_set)

    return password


def main():
    """Prompts the user to specify the desired length and complexity of the password, then generates and displays a strong and random password."""

    # Get the user input
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the desired complexity of the password (low, medium, or high): ")

    # Generate the password
    password = generate_password(length, complexity)

    # Display the password
    print("The generated password is:", password)


if __name__ == "__main__":
    main()
