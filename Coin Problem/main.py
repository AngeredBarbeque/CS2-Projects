from InquirerPy import inquirer
import pandas

#Obtains an amount of money
def get_amount(country):
    while True:
        if country == 'USA':
            unit = 'pennies'
        elif country == 'Eurozone':
            unit = 'cents'
        elif country == 'Türkiye':
            unit = 'kuruş'
        else:
            unit = 'cents'
        amount =  input(f'How much do you have based in {unit}?')
        try:
            amount = int(amount)
        except:
            print("Please enter only numbers.")
            continue
        if amount <= 0:
            print("Please enter a positive number.")
            continue
        else:
            return amount

#calculates the amount of coins
def calculate(coins,country):
    amount = get_amount(country)
    coins.pop(0)
    #Assigns the coins and their values to list containing the name, value, and amount
    smallest = [coins[0][0],int(coins[0][1]),0]
    smallest_two = [coins[1][0],int(coins[1][1]),0]
    smallest_three = [coins[2][0],int(coins[2][1]),0]
    smallest_four = [coins[3][0],int(coins[3][1]),0]
    middle = [coins[4][0],int(coins[4][1]),0]
    biggest_four = [coins[5][0],int(coins[5][1]),0]
    biggest_three = [coins[6][0],int(coins[6][1]),0]
    biggest_two = [coins[7][0],int(coins[7][1]),0]
    biggest = [coins[8][0],int(coins[8][1]),0]

    #Inner function to check if a coin should be subtracted from the total amount 
    def check_less(coin):
        nonlocal amount
        while amount >= coin[1]:
                amount -= coin[1]
                coin[2] += 1
        return coin
    
    #Actual logic, checks each coin in descending order
    while amount > 0:
        biggest = check_less(biggest)
        biggest_two = check_less(biggest_two)
        biggest_three = check_less(biggest_three)
        biggest_four = check_less(biggest_four)
        middle = check_less(middle)
        smallest_four = check_less(smallest_four)
        smallest_three = check_less(smallest_three)
        smallest_two = check_less(smallest_two)
        smallest = check_less(smallest)
    used_coins = [biggest,biggest_two,biggest_three,biggest_four,middle,smallest_four,smallest_three,smallest_two,smallest]
    for i in used_coins:
        print(f"{i[0]}:{i[2]}")
    return


def main():

    #Splits items of a list into lists of coins and coin values
    def split_list(unsplit):
        split = []
        for i in unsplit:
            split.append(i.split('-'))
        return split
    while True:
        all_coins = pandas.read_csv('Coin Problem/coins.csv')
        usa = split_list(list(all_coins.iloc[0]))
        eurozone = split_list(list(all_coins.iloc[1]))
        turkey = split_list(list(all_coins.iloc[2]))
        barbados = split_list(list(all_coins.iloc[3]))

        country = inquirer.select(
            message="Select a country to use currency from:",
            choices=[
                "USA",
                "Eurozone",
                "Türkiye",
                "Barbados",
                "Exit",
            ],
            default=None,
            ).execute()
        if country == 'USA':
            calculate(usa,country)
        elif country == 'Eurozone':
            calculate(eurozone,country)
        elif country == 'Türkiye':
            calculate(turkey,country)
        elif country == 'Barbados':
            calculate(barbados,country)
        elif country == 'Exit':
            exit()
main()
    