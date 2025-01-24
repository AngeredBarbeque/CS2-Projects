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
            DOESNT WORK WITH CHECKING CONTINUE HERE
        if nums == 'y':
            if has_nums(password):
                pass
            else:
                continue
        if caps == 'y':
            if has_caps(password):
                pass
            else:
                continue
        if lows == 'y':
            if has_lower(password):
                pass
            else:
                continue
        if spec == 'y':
            if has_spec(password):
                pass
            else:
                continue
        password = ''.join(password)
        return password
        


def main():
    #determines the requirements for the random passwords
    print("Welcome to your random password generator!")
    nums = input("Do you want your password to include numbers? y/n:\n")
    caps = input("Do you want your password to include capital letters? y/n:\n")
    lows = input("Do you want your password to include lowercase letters? y/n:\n")
    spec = input("Do you want your password to include special characters? y/n:\n")
    length = int(input("How long do you want your password to be?"))
    times = int(input("How many passwords do you want generated?"))
    #generates a password as many times as the user asked
    for i in range(times):
        print(gen_pass(nums, caps, lows, spec, length, password))
main()

