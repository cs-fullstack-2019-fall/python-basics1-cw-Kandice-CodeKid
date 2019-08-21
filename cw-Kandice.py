# ### Problem 1:
# Create two variables. One should equal “My name is: “ and the other should equal your actual name. Print the two variables in one print message.
# 
# 
nameIs = "My name is "
enterName = "Kandice"
print(nameIs+enterName)

# ### Problem 2:
# Ask the user to enter the extra credit they earned. If they entered less than 5 print “That’s not enough extra credit.” If they entered more than 20 print “That’s too much extra credit”.
# 
extraCredit = int(input("enter extra credit earned"))
if extraCredit <5:
    print("That’s not enough extra credit.")
elif extraCredit >20:
    print("That’s too much extra credit.")
else:
    print("Kudos on the extra credit")
    

# ### Problem 3:
# Ask a user to enter a password. Enter a password. Ask user to reenter password. Check to see if they are correct.
# 
userPass = input("Enter password")
userPass2 = input("Enter password again")
if userPass == userPass2:
    print("Password Matches")
else:
    print("Passwords do not match")


# ### Problem 4:
# Ask for two card numbers. If it equals 21 print BLACKJACK!, if it’s greater than 21 print BUST!, if it’s less than 21 print “The total is [THE TOTAL]”

cardNum1 = int(input("enter a number 1-11   "))
cardNum2 = int(input("enter a number 1-11   "))
sum = cardNum1 +cardNum2

if sum>21:
    print("Bust")
elif sum==21:
    print("BlackJack!!")
else:
    print(sum)