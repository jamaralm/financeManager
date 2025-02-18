from modules.revenue import addRevenue
from modules.resume import showBalance, showAll, showNegativeRevenues,showPositiveRevenues
from datetime import date

def getDate():
    actualDate = date.today().strftime('%d-%m-%y')
    return actualDate

def returnRevenues():
    revenueName = input('Type the Name:')
    revenueValue = float(input('Type the Value:'))
    revenueCategory  = input('Type the category:')
    actualDate = getDate()
    addRevenue(revenueName, revenueValue, actualDate, revenueCategory)

possibleActions = ['Add Revenue', 'Show All', 'Show Negative Revenues', 'Show Positive Revenues', 'Show Balance','Leave :(']

def main():
    while True:
        for index, action in enumerate(possibleActions):
            print(f'{index+1}|{action}')
        
        userChoice = int(input('Type the operation index: '))

        if userChoice == 1:
            returnRevenues()
        elif userChoice == 2:
            showAll()
        elif userChoice == 3:
            showNegativeRevenues()
        elif userChoice == 4:
            showPositiveRevenues()
        elif userChoice == 5:
            showBalance()
        elif userChoice == 6:
            print('Exiting...')
            break

if __name__ == '__main__':
    main()