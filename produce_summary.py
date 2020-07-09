
def deliveries(day, file): #Defining a function with two parameters

    delivery_files = open(file) #Variable that opens the external files

    print("Day", day) #prints what day it is

    for line in delivery_files: #for loop going through each line of each file
        line = line.rstrip() # removes characters from line
        words = line.split('|') # splits each line where there is a "|" into a word

        melon = words[0] # melon is a variable for the first word in words
        count = words[1] #count is a variable for the second word in words 
        amount = words[2] #amount is a variable for the third word in words

        print("Delivered {} {}s for total of ${}".format(count, melon, amount))
        #print statement that is formatted 

    delivery_files.close() #closing file

deliveries(1, "um-deliveries-20140519.txt") #calling the function with both arguments
deliveries(2, "um-deliveries-20140520.txt") #calling the function with both arguments
deliveries(3, "um-deliveries-20140521.txt") #calling the function with both arguments
