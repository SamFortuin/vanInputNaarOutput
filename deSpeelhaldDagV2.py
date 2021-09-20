#99059050, Sam Fortuin

#vars
entreeCost = 7.45
print("Entree cost is",entreeCost,"per person")
amountOfBoys = input("How many boys are going? ")
vrGameSeatMin = input("How many minutes in the VR GameSeat? ")

#str to float
amountOfBoys = float(amountOfBoys) 
vrGameSeatPrice = float(vrGameSeatMin) * 0.074

#total cost calc
totalCost = (entreeCost * amountOfBoys) + (vrGameSeatPrice * amountOfBoys)

#float to int & euro to cent conversion
amountOfBoys = int(amountOfBoys)
vrGameSeatPrice = round(vrGameSeatPrice,2) * 100
vrGameSeatPrice = int(vrGameSeatPrice)
totalCost = round(totalCost,2) * 100
totalCost = int(totalCost)

print("Dit geweldige dagje-uit met",amountOfBoys,"mensen in de Speelhal met",vrGameSeatMin,"minuten VR kost je maar",totalCost,"cent")