#Nicholas Larsen Password Generator
import random
password = []
#checks if the password has any capital letters in it by matching the ord value of each character to the ord value of capital letters
def has_caps(password):
    for i in password:
        if ord(i) >= 65 and ord(i) <= 90:
            return True
    return False

#checks if the password has any lowercase letters in it by matching the ord value of each character to the ord value of lowercase letters
def has_lower(password):
    for i in password:
        if ord(i) >= 97 and ord(i) <= 122:
            return True
    return False

#checks if the password has numbers by individual trying to turn each character into an integer. If it doesn't work, it goes to the next character, and if it does it immediately stops and returns true. Once all characters are exausted it decides there are no numbers and returns false.
def has_nums(password):
    for i in password:
        try:
            int(i)
        except:
            pass
        else:
            return True
    return False

#Checks if the password has special characters by trying to match the ord value of each character in the password to the ord values of any special characters.
def has_spec(password):
    for i in password:
        if ord(i) >= 32 and ord(i) <= 47:
            return True
        elif ord(i) >= 58 and ord(i) <= 64:
            return True
        elif ord(i) >= 91 and ord(i) <= 96:
            return True
        elif ord(i) >= 123 and ord(i) <= 126:
            return True
    return False

#Creates the password by adding random characters and then checking if it meets all requirements.
def gen_pass(nums, caps, lows, spec, length, password):
    while True:
        password = []
        for i in range(length):
            password.append(chr(random.randint(32, 126)))
        if nums == 'y':
            if has_nums(password):
                pass
            else:
                continue
        else:
            if has_nums(password):
                continue
            else:
                pass
        if caps == 'y':
            if has_caps(password):
                pass
            else:
                continue
        else:
            if has_caps(password):
                continue
            else:
                pass
        if lows == 'y':
            if has_lower(password):
                pass
            else:
                continue
        else:
            if has_lower(password):
                continue
            else:
                pass
        if spec == 'y':
            if has_spec(password):
                pass
            else:
                continue
        else:
            if has_spec(password):
                continue
            else:
                pass
        password = ''.join(password)
        return password
        


def main():
    #determines the requirements for the random passwords
    print("Welcome to your random password generator! Type 'e' to leave the program.")
    while True:
        nums = input("Do you want your password to include numbers? y/n:\n")
        #lets the user exit the program
        if nums == 'e':
            print("Goodbye!")
            exit()
        caps = input("Do you want your password to include capital letters? y/n:\n")
        #lets the user exit the program
        if caps == 'e':
            print("Goodbye!")
            exit()
        lows = input("Do you want your password to include lowercase letters? y/n:\n")
        #lets the user exit the program
        if lows == 'e':
            print("Goodbye!")
            exit()
        spec = input("Do you want your password to include special characters? y/n:\n")
        #lets the user exit the program
        if spec == 'e':
            print("Goodbye!")
            exit()
        #Insures the user picked at least one type of character
        if nums != 'y' and caps != 'y' and lows != 'y' and spec != 'y':
            print("You must have at least one character type to continue.\n")
            continue
        if nums != 'y' and caps != 'y' and lows != 'y' and spec != 'y' and nums != 'n' and caps != 'n' and lows != 'n' and spec != 'n':
            print("Please enter 'n' or 'y' to every question.")
            continue
        #determines how long the password will be, along with how many passwords to generate.
        length = int(input("How long do you want your password to be?\n"))
        times = int(input("How many passwords do you want generated?\n"))
        #generates a password as many times as the user asked
        for i in range(times):
            print(gen_pass(nums, caps, lows, spec, length, password))
main()