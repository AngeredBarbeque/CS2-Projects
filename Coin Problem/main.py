from InquirerPy import inquirer
import pandas

def calculate(coins,country):
    coins.pop(0)
    
    print(coins)

def get_amount(country):
    if country == 'USA':
        unit = 'pennies'
    elif country == 'Eurozone':
        unit = 'cents'
    elif country == 'Türkiye':
        unit = 'kuruş'
    else:
        unit = 'cents'
    amount =  input(f'How much do you have based in {unit}?')
    #FINISH THIS

def main():

    #Splits items of a list into lists of coins and coin values
    def split_list(unsplit):
        split = []
        for i in unsplit:
            print(i)
            split.append(i.split('-'))
        return split
    
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
main()
    