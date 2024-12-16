import random
import string

def generate_password(length=8, use_uppercase=True, use_numbers=True, use_special=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''
    
    # Combine the character sets based on user preferences
    all_characters = lowercase + uppercase + numbers + special
    
    # Ensure at least one character set is selected
    if len(all_characters) == 0:
        raise ValueError("At least one character set must be selected.")
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    # User input for password criteria
    try:
        length = int(input("Enter the desired password length (e.g., 8): "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")