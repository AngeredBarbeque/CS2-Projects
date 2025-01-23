#Nicholas Larsen Password Generator
import random
password = '23d~'

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

def main():
    print("Welcome to your random number generator!")
    nums = !!!CONTINUE HERE!!!

print(has_caps(password))
print(has_lower(password))
print(has_nums(password))
print(has_spec(password))