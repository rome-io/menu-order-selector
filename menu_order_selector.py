print("Welcome to the Moocow Creamery!")
orderName = input("Please enter a name for the order: ")
flavorNames = ["Chocolate", "Vanilla", "Strawberry", "Moose Tracks", "Pistachio", "Peanut Butter"]
flavorNames.append("Not Sewage")
flavorNames[2] = "Mystery"
flavorCount = len(flavorNames)
print("Happy you're here,", orderName + ".", "We have", flavorCount, "flavors available.", "Here's a list of our current flavors:")
number = 1
for number, flavor in enumerate(flavorNames):
    number = number + 1
    print(number, flavor)
flavorNames.sort()
dictionaries = input("Would you like to review our sizes? ")
dictionaries = dictionaries.lower()


conePrices = "Small: $1.50", "Medium: $2.35", "Large: $3.25"
coneSizeDesc = "Small: Approx 3in.", "Medium: Approx. 4in", "Large: Approx. 5in"


if dictionaries == "yes":
    print(conePrices, coneSizeDesc)
    selectedSize = input("What size cone would you like? ")
else:
    selectedSize = input("What size cone would you like? ")
    selectedSize = selectedSize.lower()

if selectedSize == "small":
    conePrice = True
    conePrice = "$1.50"
elif selectedSize == "medium":
    conePrice = True
    conePrice = "$2.35"
elif selectedSize == "large":
    conePrice = True
    conePrice = "$3.25"
else:
    conePrice = False
    print("Sorry! That size was invalid. Please try again.")
    selectedSize = input("What size cone would you like? ").lower()

while conePrice == False:
    if selectedSize == "small":
        conePrice = True
        conePrice = "$1.50"
    elif selectedSize == "medium":
        conePrice = True
        conePrice = "$2.35"
    elif selectedSize == "large":
        conePrice = True
        conePrice = "$3.25"
    else:
        conePrice = False
        print("Sorry! That size was invalid. Please try again.")
        selectedSize = input("What size cone would you like? ").lower()



selectedFlavor = input("Which number flavor would you like? ")

if selectedFlavor == "1":
    finalFlavor = flavorNames[0]
if selectedFlavor == "2":
    finalFlavor = flavorNames[6]
if selectedFlavor == "3":
    finalFlavor = flavorNames[2]
if selectedFlavor == "4":
    finalFlavor = flavorNames[1]
if selectedFlavor == "5":
    finalFlavor = flavorNames[5]
if selectedFlavor == "6":
    finalFlavor = flavorNames[4]
if selectedFlavor == "7":
    finalFlavor = flavorNames[3]


print("Great! Thanks for ordering,", orderName + ".", "Your", selectedSize, "size", finalFlavor, "cone will be ready soon. Please pay", conePrice, "at the counter.")

