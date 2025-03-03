#Nicholas Larsen, Advanced Notes Functions

# 1. What is a helper function?

    #A function called inside another function to complete a portion of that function's task

# 2. What is the purpose of a helper function?
    # To make an individual function simpler.
def check_input(user_txt): 
    return not any(char.isdigit() for char in user_txt)
    

def hello(name):
    if check_input(name):
        print(f'Hello, {name}. Your end approaches rapidly.')
    else:
        print("Only input letters. >:(")
        user = input('What is your name:\n').strip().capitalize()
        # 8. What is recursion?
            #Calling a function inside of itself to reduce redundent loops.
        hello(user)
        # 9. How does recursion work?
            #Have a line that tells the function to call itself again.
user = input('What is your name:\n').strip().capitalize()
hello(user)




# 3. What is an inner function?

    # A function defined inside another function.
    # Wrapper functions mostly exist to keep the inner function safe from the remainder of the code

def fun_one(): # Wrapper function
    msg = 'this is the outer function'
    def fun_two():
        print(msg)
    fun_two()

# 4. What is the scope of a variable in a function WITH an inner function?

    # Local, including the inner function

# 5. Why do we use inner functions?

    # To use less parameters while still having access to local variables, or if there are tasks that need to be accomplished inside the function.

# 6. What is a closure function?
def fun(a):
    #outer/wrapper function, remembers the value of 'a'

    #closure function
    def adder(b):
        return a+b
    return adder #returns the closure function

#calls outer function with a = 10, which returns adder
val = fun(10)

#when calling a closure, give it the value of b, and it remebers a as 10
print(val(5))

# 7. Why do we write closure functions?

    # Decrease the amount of unnesecary parameters.

def end(income):
    def calc(cost, type):
        percent = cost/income * 100
        print(f'Your {type} is ${cost:.2f} and that is {percent:.0f}% of your income.')
    return calc
def user_input(type):
    return input(f"What is your monthly {type}:\n$")
income = int(user_input('Income'))
rent = int(user_input('Rent'))
utilities = int(user_input('Utilities'))
transportation = int(user_input('Transportation'))

ready = end(income)

ready(rent, 'Rent')
ready(utilities, 'Utilities')
ready(transportation, 'Transportation')