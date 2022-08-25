# Imports necessary packages
import random
from threading import Event

# Defines starting variables
questionDone = 0
gameFinished = 0
counter = 0
stockList = ["NFLX", "MSFT", "TSLA", "AMZN", "AAPL", "META", "GOOG", "INTC", "NVDA", "DJI", "DIS"]
randStockList = []
priceList = []
stockAmount = 0
walletBalance = 100

# Chooses 5 random stocks from the stockList
while counter <= 4:
    randomInt = random.randint(0,(len(stockList)- 1))
    randStock = stockList[randomInt]
    if randStock not in randStockList:
        randStockList.append(stockList[randomInt])
        counter += 1
counter = 0

# Chooses a random price for each stock
while counter != (len(randStockList)):
    randomPrice = random.randrange(1, 101)
    priceList.append(randomPrice)
    counter += 1
counter = 0

# Sets out the rules
print("\n * Hello and welcome to Finn's Stock Picker! You have $100 and you can pick any",len(randStockList),"stocks, after each turn the stocks will change in value randomly and you can sell your stock and buy more if you want. See how much you can earn! *\n")
Event().wait(4)

# Displays the stock options and values
print(" * The stocks you can choose from are: *")
while counter != (len(randStockList)):
    print(randStockList[counter],": $",priceList[counter],"\n")
    counter += 1
counter = 0

# Asks user what stock they want
while questionDone == 0:
    stockPick = str(input(" * What stock do you wish to buy? *\n")).upper()
    if stockPick in randStockList:
        stockNumber = randStockList.index(stockPick)
        stockAmount = round(walletBalance / priceList[stockNumber],4)
        print("\nYou have bought:",stockAmount,"Shares in",stockPick,"\n")
        questionDone += 1
    else:
        # Displays error
        print("\n* ",stockPick," Is not a valid answer *\n")
questionDone = 0

while gameFinished == 0:
    # Changes stock values
    Event().wait(2)
    while counter != (len(randStockList)):
        randomChange = round(random.uniform(-0.20, 2.50),2)
        priceList[counter] = priceList[counter] * randomChange
        counter += 1
    counter = 0

    # Displays the new stock values
    print(" * The new stock values are: *")
    while counter != (len(randStockList)):
        print(randStockList[counter],": $",priceList[counter],"\n")
        counter += 1
    counter = 0

    # Displays current portfolio value
    Event().wait(2)
    portfolio = round(stockAmount * priceList[stockNumber],4)
    print("You have",stockAmount,"Shares in",stockPick,", Which are now worth: $",portfolio,"\n")

    if portfolio <= 0:
        print("\n * Oh no! It looks like you have gone bankrupt! *\n")
        Event().wait(2)
        quit()

    # Asks user if they want to sell?
    while questionDone == 0:
        Event().wait(1.5)
        yesOrNo = str(input(" * Would you like to sell your shares and buy different ones? Y/N *\n")).upper()
        if yesOrNo == "Y":
            # Sells current stock
            walletBalance = portfolio
            stockAmount = 0
        
            question2Done = 0
            while question2Done == 0:
                # Asks user for new stock input
                print(" * You have: $",walletBalance," *\n")
                stockPick = str(input(" * What stock would you like to buy? *\n")).upper()
                if stockPick in randStockList:
                    stockNumber = randStockList.index(stockPick)
                    if priceList[stockNumber] >= 0:
                        stockAmount = round(walletBalance / priceList[stockNumber],4)
                        print("\nYou have bought:",stockAmount,"Shares in",stockPick,"\n")
                        question2Done += 1
                    else:
                        # Displays error
                        print("\n * This stock's value is too low to buy, please choose another *\n")

                else:
                    # Displays error
                    print("\n* ",stockPick," Is not a valid answer *\n")
            question2Done = 0
            questionDone = 1

        elif yesOrNo =="N":
            # Asks user if they want to end the game
            question2Done = 0
            while question2Done == 0:
                gameEnd = str(input(" * Would you like to close the game? Y/N *\n")).upper()
                if gameEnd == "Y":
                    # Quits game
                    print(" * You had : $",portfolio,"! *")
                    Event().wait(2)
                    quit()

                elif gameEnd == "N":
                    question2Done = 1

                else:
                    # Displays error
                    print("\n* ",gameEnd," Is not a valid answer *\n")
            question2Done = 0
            questionDone = 1
    
        else:
            # Displays error
            print("\n* ",yesOrNo," Is not a valid answer *\n")
    questionDone = 0
