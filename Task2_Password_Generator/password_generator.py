import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbol = string.punctuation

def get_length():
    while True:
        try:
            length = int(input("Enter password length📏 : "))
            if length < 8 :
                print("Length must be at least 8 characters.")
                continue
            return length
        except Exception as e:
            print("Please enter a valid number." , e)

def get_continuous_choices():
    print("\nChoose character types (type yes/no for each)")
    print()
    use_upper = input("Include UPPERCASE letters🔠 ? (yes/no) : ").lower() == 'yes'
    use_lower = input("Include lowercase letters🔡 ? (yes/no) : ").lower() == 'yes'
    use_digits = input("Include Digits letters🔢 ?   (yes/no) : ").lower() == 'yes'
    use_symbol = input("Include Symbols letters🔣 ?  (yes/no) : ").lower() == 'yes'

    selection = sum([ use_upper , use_lower , use_digits , use_symbol])
    if selection < 2:
        print("You must select at least 2 character types.")
        return get_continuous_choices()
    return use_upper , use_lower , use_digits , use_symbol

def generate_password(length , use_upper , use_lower , use_digits ,use_symbol):
    character = ""
    if use_upper:
        character += uppercase
    if use_lower:
        character += lowercase
    if use_digits:
        character += digits
    if use_symbol:
        character += symbol

    password = "".join(random.choice(character) for _ in range(length))
    return password

print()
print("========== RANDOM PASSWORD GENERATOR ==========")
print()

while True:
    length = get_length()
    use_upper , use_lower , use_digits , use_symbol = get_continuous_choices()
    password = generate_password(length , use_upper , use_lower , use_digits , use_symbol)
    print("\nGenerated Password:🔑")
    print(password)
    print()

    again = input("Generate another password? (yes/no) : ").lower()
    if again != 'yes':
        print("Thanks🙏 Check out Generated password above☝️  Bye!")
        break




