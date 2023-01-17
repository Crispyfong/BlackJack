import random
game = True
cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]

while game == True:
    print("**********************")
    print("*Welcome to blackjack*")
    print("**********************")
    print("\n******************")
    print("*Rules are simple*")
    print("*FaceCards are 10*")
    print("*Ace can be  1/11*")
    print("*Don't go over 21*")
    print("******************")
    enter = input("\nUnderstand? (y/n):")
    if enter == "y":
        print("\n********************")
        print("*Alright lets begin*")
        print("********************")
        print("\nYour hand:")
        print("********************")
        cardOne = random.choice(cards)
        cardTwo = random.choice(cards)
        botCard1 = random.choice(cards)
        botCard2 = random.choice(cards)
        print(cardOne, cardTwo)
        print("\nBots hand:")
        print("********************")
        print(botCard1, botCard2)
        print("Would you like to hit or miss")
        hitORmiss = input("(h/m)")
        if hitORmiss == "h":
            if (botCard1 + botCard2) < 21 and (botCard1 + botCard2) > 15:
                cardThree = random.choice(cards)
                print(cardOne, cardTwo, cardThree)
                print("\nBots hand:")
                print("********************")
                print(cardOne, cardTwo)
                print("Would you like to hit or miss")
                hitORmiss1 = input("(h/m)")
                if hitORmiss1 == "h":
                    cardFour = random.choice(cards)
                    print(cardOne, cardTwo, cardThree, cardFour)
                    print("Would you like to hit or miss")
                    hitORmiss2 = input("(h/m)")
                    if hitORmiss2 == "h":
                        cardFive = random.choice(cards)
                        print(cardOne, cardTwo, cardThree, cardFour, cardFive)
                    if hitORmiss2 == "m":
                        result = cardOne + cardTwo + cardThree + cardFour
                        botResult = botCard1 + botCard2
                        print("You got:\n")
                        print(result)
                        print("The bot got:\n")
                        print(botResult)
                        if (botResult > result) and (botResult and result <= 21):
                            print("***********")
                            print("*YOU LOST!*")
                            print("***********")
                            break
                        if (result > botResult) and (botResult and result <= 21):
                            print("***********")
                            print("*YOU  WON!*")
                            print("***********")
                            break
                        if (botResult > result) and (botResult > 21):
                            print("***********")
                            print("*YOU  WON!*")
                            print("***********")
                            break
                        if (result > botResult) and (result > 21):
                            print("***********")
                            print("*YOU LOST!*")
                            print("***********")
                            break
            if (botCard1 + botCard2) < 21 and (botCard1 + botCard2) < 15:
                    botCard3 = random.choice(cards)
                    cardThree = random.choice(cards)
                    print("\nYour hand:")
                    print("********************")
                    print(cardOne, cardTwo, cardThree)
                    print("\nBots hand:")
                    print("********************")
                    print(botCard1, botCard2, botCard3)
                    print("Would you like to hit or miss")
                    hitORmiss1 = input("(h/m)")
                    if hitORmiss1 == "h":
                        cardFour = random.choice(cards)
                        print(cardOne, cardTwo, cardThree, cardFour)
                        print("Would you like to hit or miss")
                        hitORmiss2 = input("(h/m)")
                        if hitORmiss2 == "h":
                            cardFive = random.choice(cards)
                            print(cardOne, cardTwo, cardThree, cardFour, cardFive)
                        if hitORmiss2 == "m":
                            result = cardOne + cardTwo + cardThree + cardFour
                            botResult = botCard1 + botCard2
                            print("You got:\n")
                            print(result)
                            print("The bot got:\n")
                            print(botResult)
                            if (botResult > result) and (botResult and result <= 21):
                                print("***********")
                                print("*YOU LOST!*")
                                print("***********")
                                break
                            if (result > botResult) and (botResult and result <= 21):
                                print("***********")
                                print("*YOU  WON!*")
                                print("***********")
                                break
                            if (botResult > result) and (botResult > 21):
                                print("***********")
                                print("*YOU  WON!*")
                                print("***********")
                                break
                            if (result > botResult) and (result > 21):
                                print("***********")
                                print("*YOU LOST!*")
                                print("***********")
                                break
                    if hitORmiss1 == "m":
                        result = cardOne + cardTwo + cardThree 
                        botResult = botCard1 + botCard2
                        print("You got:\n")
                        print(result)
                        print("The bot got:\n")
                        print(botResult)
                        if (botResult > result) and (botResult and result <= 21):
                            print("***********")
                            print("*YOU LOST!*")
                            print("***********")
                            break
                        if (result > botResult) and (botResult and result <= 21):
                            print("***********")
                            print("*YOU  WON!*")
                            print("***********")
                            break
                        if (botResult > result) and (botResult > 21):
                            print("***********")
                            print("*YOU  WON!*")
                            print("***********")
                            break
                        if (result > botResult) and (result > 21):
                            print("***********")
                            print("*YOU LOST!*")
                            print("***********")
                            break
        if hitORmiss == "m":
            result = cardOne + cardTwo
            botResult = botCard1 + botCard2
            print("You got:\n")
            print(result)
            print("The bot got:\n")
            print(botResult)
            if (botResult > result) and (botResult and result <= 21):
                print("***********")
                print("*YOU LOST!*")
                print("***********")
                break
            if (result > botResult) and (botResult and result <= 21):
                print("***********")
                print("*YOU  WON!*")
                print("***********")
                break
            if (botResult > result) and (botResult > 21):
                print("***********")
                print("*YOU  WON!*")
                print("***********")
                break
            if (result > botResult) and (result > 21):
                print("***********")
                print("*YOU LOST!*")
                print("***********")
                break

    if enter == "n":
        print("**********************")
        print("*Welcome to blackjack*")
        print("**********************")
        print("\n******************")
        print("*Rules are simple*")
        print("*FaceCards are 10*")
        print("*Ace can be  1/11*")
        print("*Don't go over 21*")
        print("******************")
        enter = input("\nUnderstand? (y/n)")
    else:
        print("\nthanks for coming!")
        break
       
    