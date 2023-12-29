from Functions import amountOwed, menuKK, userOrder

#declarations and initializations of variables
profile = {}
value = False
item = ("krabby patty", "barnicle fry", "kelp shake", "krusty krab pizza")
items = ("krabby patties", "barnicle fries", "kelp shakes", "krusty krab pizzas")
numPurchases = 0

#getting total order from user
profile = userOrder(item)

#finding the total number of items the user purchased
for i in range(0, len(profile)):
    #conditional statement checking each menu item in dictionary to see if it was purchased
    if profile[item[i]] > 0:
        #incrementing numPurchases if dictionary value is greater than zero
        numPurchases += profile[item[i]]

#conditional statement which runs if the user purchased more than one item
if numPurchases > 0:
    #printing user's order
    print("\nYour order:")
    #for loop which runs through all the keys and values in the dictionary
    for i in range(0, len(profile)):
        #conditional statement which runs code if specified menu item has one single purchase
        if profile[item[i]] == 1:
            print(str(profile[item[i]]) + " " + item[i])
        #conditional statement which runs code if specified menu item has at least two or more purchases    
        elif profile[item[i]] > 1:
            print(str(profile[item[i]]) + " " + items[i])

    #printing total owed by user
    print("\nYour total is: $" + amountOwed(profile, item) + "\nEnjoy the food!")   

#conditional statement which will run if the user ordered nothing
else:
    print("Guess you are not hungry.")                