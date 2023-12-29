from Functions import menuKK

def userOrder(item):
    """This function will get the entire order from the user.  After the user's order is taken, the function will return a dictionary containing the user's order.  This function also takes in a tuple as an argument."""

    #declarations and initializations of variables
    profile = {}
    orderNum = orderAmount = -1

    #for loop initializing the local dictionary
    for i in range(0, len(item)):
        profile[item[i]] = 0

    print("Welcome to the Krusty Krab!")

    #while loop which runs until order number is equal to zero
    while orderNum != 0:
        #calling menuKK function
        menuKK()
        #getting order number from the user
        orderNum = int(input("What would you like? (Enter 0 to finish order!): "))

        #conditional statement which runs if the user's order is less than zero or if the user's order is greater than four
        if orderNum < 0 or orderNum > 4:
            print("That is not on the menu! Try again.")
        
        #conditional statement which runs if the user's order is equal to zero
        elif orderNum == 0:
            continue
                
        #conditional statement which runs if the user's order is valid        
        else:
            #getting order amount from the user
            orderAmount = int(input("How many: "))
            #while loop which runs until order amount is valid
            while orderAmount < 0:
                print("You cannot order a negative amount of food!")
                orderAmount = int(input("Try Again: "))
            #adding user's order to local dictionary    
            profile[item[orderNum - 1]] += orderAmount

    #returning dictionary
    return profile                 