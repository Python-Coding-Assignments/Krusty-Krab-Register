def amountOwed(profile, item):
    """This function calculates the amount the user owes based on what the user purchased.  This function takes in two arguments as parameters: profile which is a dictionary and item which is a tuple."""\
    
    #declarations and initializations of variables
    amounts = (3.5, 1.5, 1, 5)
    total = 0

    #for loop which iterates over the length of the dictionary
    for i in range(0, len(profile)):
        #conditional statement which runs if a value to a dictionary's key is greater than zero
        if profile[item[i]] > 0:
            #incrementing the total amount the user owes
            total += profile[item[i]] * amounts[i]

    #returning the total amount the user owes as a string
    return str("{:.2f}".format(total))