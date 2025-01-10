#Nicholas Larsen 2nd Period Financial Calculator

#turns a percent into a decimal

def percentify(num):
    return num/100

#calculates compound interest

def interest(deposit, rate, often, time):
    return deposit*(1+rate/often)**(often*time)

#discount by a percentage

def discount_per(cost, per):
    return cost*(1-per)

#Adds a percentage

def increase_per(cost, per):
    return cost*(1+per)

#Budget allocation

def budget():
    #how much do you make per week?
    income = float(input("What is your weekly income:\n"))
    #How much do you spend on food per week?
    food = percentify(int(input("What percent of your income do you want to spend on food?\n(Type percentages as whole numbers, e.g. for 80% type 80):\n")))
    #How much do you spend on entertainment per week?
    entertain = percentify(int(input("What percent of your income do you want to spend on entertainment?:\n")))
    #How much do you spend on home expenses per week?
    housing = percentify(int(input("What percent of your income do you want to spend on housing?:\n")))
    #How much do you save per week?
    savings = percentify(int(input("What percent of your income do you want to save weekly?:\n")))
    #Calculate amounts
    if food+entertain+housing+savings > 1:
        print("Sorry, that's more than 100%% of your income!\n")
        budget()
    else:
        print("You will spend", income*food, "on food per week.\n")
        print("You will spend", income*entertain, "on entertainment per week.\n")
        print("You will spend", income*housing, "on housing per week.\n")
        print("You will save", income*savings, "per week.\n")

#Calculate compound interest
def compound():
    #What is your original deposit?
    deposit = float(input("What amount did you start with?:\n"))
    #What is your yearly interest rate?
    rate = percentify(int(input("What percent does your deposit increase by yearly?\n(Type percentages as whole numbers, e.g. for 80% type 80):\n")))
    #How often is your interest compounded per year?
    often = float(input("How many times is your interest compounded per year?:\n"))
    #How long do you want to wait?
    time = float(input("How many years do you plan to wait?:\n"))
    #Print final
    print("You will have", interest(deposit, rate, often, time), "by the end of your waiting period.\n")
    
#How long will it take to save?
def saving():
    #How much do you save weekly?
    savings = float(input("How much do you save weekly?\n"))
    #How much does what you're saving for cost?
    goal = float(input("How much do you want to save?\n"))
    time = goal/savings
    #print time
    print("You will take", time, "weeks to save enough.\n")

#Calculate sales prices
def sales():
    #How much does the item usually cost?
    price = float(input("How much does the item originally cost?:\n"))
    #What is the sales tax in your area?
    tax = percentify(float(input("What is the sales tax in your area?\n(Type percentages as whole numbers, e.g. for 80% type 80):\n")))
    #How many discounts do you have?
    disc_amount = int(input("How many discounts do you have? (e.g. if you had 2 coupons and one online deal, enter 3.):\n"))
    for i in range(disc_amount):
        #How much is it discounted?
        price = discount_per(price, percentify(float(input("What percent is it discounted by?\n(Type percentages as whole numbers, e.g. for 80% type 80):\n"))))
    #Apply sales tax
    price = increase_per(price, tax)
    #Print final price
    print("The final price will be", price, "\n")

#Calculate a tip
def tips():
    #How much is the original cost?
    price = float(input("What is the cost of the service?\n"))
    #What percentage do you want to tip?
    tip = percentify(float(input("What percent would you like to tip?\n(Type percentages as whole numbers, e.g. for 80% type 80):\n")))
    #print final price
    print("The final price is", increase_per(price, tip))


#What do you want to do?
def main():
    while True:
        choice = input("Hello! Welcome to your financial calculator!\nWhat would you like to do?\n1:Budget allocator\n2:Compound interest calculator\n3:Saving calculator\n4:Sales prices\n5:Tip calculator\n6:Exit\nChoose:\n")
        if choice == "1":
            budget()
        elif choice == "2":
            compound()
        elif choice == "3":
            saving()
        elif choice == '4':
            sales()
        elif choice == '5':
            tips()
        elif choice == '6':
            exit()
        else:
            print("Sorry, didn't catch that. try again.\n")

main()


