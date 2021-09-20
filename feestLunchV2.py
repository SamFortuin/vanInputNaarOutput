#99059050, Sam Fortuin
#vars for calculations
amountOfCroissants = input("How many croissants\n")
croissantsPrice = input("How much per croissant?\n")
amountOfBaguette = input("how many baguette's?\n")
baguettePrice = input("Price per baguette?\n")
couponSavings = input("How much are your coupons worth?\n")
couponAmount = input("How many coupons you got?\n")

amountOfCroissants = float(amountOfCroissants)
croissantsPrice = float(croissantsPrice)
amountOfBaguette = float(amountOfBaguette)
baguettePrice = float(baguettePrice)
couponSavings = float(couponSavings)
couponAmount = float(couponAmount)

lunchPrice = (amountOfCroissants * croissantsPrice) + (amountOfBaguette * baguettePrice) - (couponSavings * couponAmount)
lunchPrice = round(lunchPrice,2)
lunchPrice = lunchPrice * 100
lunchPrice = int(lunchPrice)
amountOfCroissants = int(amountOfCroissants)
amountOfBaguette = int(amountOfBaguette)
couponAmount = int(couponAmount)
#print("Total price for the lunch is €",lunchPrice)
print("De feestlunch kost je bij de bakker",lunchPrice,"cent voor de",amountOfCroissants,"croissantjes en de",amountOfBaguette,"stokbroden als de",couponAmount,"kortingsbonnen ter waarde van €"+couponSavings,"nog geldig zijn!")