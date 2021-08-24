# This program calculates the number of dogs, their size and the food required for each dog to for the month.
# The previous month's leftover food should be deducted from the total and 20% added to calculate the grand total

# enter the number of small dogs in your shelter
sdog = input('Enter the number of small dogs in your shelter: ')
# print ('Enter the number of small dogs in your shelter')

# enter the number of medium dogs in your shelter
mdog = input('Enter the number of medium dogs in your shelter: ')
# print ('Enter the number of medium dogs in your shelter')

# enter the number of large dogs in your shelter
# print ('Enter the number of large dogs in your shelter')
ldog = input('Enter the number of large dogs in your shelter: ')

# enter the number of lbs of dog food leftover from the previous month
# print ('Enter the number of lbs of dog food leftover from the previous month')
lfood = input('Enter the number in lbs. of dog food leftover from the previous month: ')

# dog food requirements
# sdog = 10lbs
# mdog = 20lbs
# ldog = 30lbs
# lfood = 25lbs1

def calculatedogfood(sd, md, ld, lf):
# add number of dogs times the food required
    sum = int(sd)*10 + int(md)*20 + int(ld)*30 - int(lf)
    return sum * 1.20

# Display the sum
print('Current inventory of dogs and food in your shelter: {0} small dog(s), {1} medium dog(s), {2} large dog(s), and {3} lb(s) of leftover food.'.format(sdog, mdog, ldog, lfood))
print('The grand total of dog food to order this month is: {0} lb(s).'.format(calculatedogfood(sdog, mdog, ldog, lfood)))

#test my function
print ("UNIT TEST: 1 sd, 1 md, 1 ld, 1 lf, results should be 70.8")
print (70.8 == calculatedogfood(1,1,1,1))
#print(calculatedogfood(1,1,1,1))