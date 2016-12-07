#Factorial Program

#User inputs a number
number = int(input("Enter the number that you would like to factorial of: "))

#Set the conditions
count = 1
lowestValue = 1

#while loop logic
while count <=number: #Checks to see if the number of times the loop has run (distance up the number sequence 1,2,3 etc) has reached the number.
    lowestValue = lowestValue * count #Starts at the base unit of 1, and multiplies it by the number of times the loop has run
    count = count+1 #brings the count closer to the number.
    
print (str(number)+" ! is " +str(lowestValue)) #prints the result to the terminal. #final result
