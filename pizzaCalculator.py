#99059050, Sam Fortuin, pizzaCalculator

def main():
    #vars
    smallPizzaAmount = float(input("How many small pizza's do you want?\n"))
    mediumPizzaAmount = float(input("How many medium pizza's do you want?\n"))
    largePizzaAmount = float(input("How many large pizza's do you want?\n"))
    #prices in €, based on NYPizza
    pizzaPrices = [11.99, 13.99, 16.99]
    smallPizzaPrice, mediumPizzaPrice, largePizzaPrice = pizzaPrices

    #sum for price
    totalPrice = (smallPizzaAmount * smallPizzaPrice) + (mediumPizzaAmount * mediumPizzaPrice) + (largePizzaAmount * largePizzaPrice)
    
    #print final calculator line
    print("Your order of",int(smallPizzaAmount),"small pizza's,",int(mediumPizzaAmount),"medium pizza's, and",int(largePizzaAmount),"large pizza's costs €"+str(round(totalPrice,2)),"in total")
    
    #asks if another order & lowers it
    restart = input("Do you want to buy more pizza's? Y/N\n")
    restart = restart.lower()

    #if yes is typed program restarts itself
    if restart == "y" or restart == "yes":
        main()
    #if no is typed exits with ty msg
    elif restart == "n" or restart == "no":
        print("thank you for using the calculator. program will now exit")
        exit()
    else:
        print("input not regonized as any form of yes or no. program will now exit")
        exit()

main()
