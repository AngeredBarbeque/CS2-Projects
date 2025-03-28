from InquirerPy import inquirer
import pandas
from calcs import *
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
    