Monthly Food Calculator for Friendly Paws Dog Shelter
Description
This program uses input data via questionnaire-style prompts for the number of dogs/respective sizes and leftover food from the previous month to calculate the food requirements in lbs. which needs to be ordered for sustaining the animals in the shelter.
The previous months leftover food should be deducted from the total required and then 20% added to calculate the grand total.
My Story Writeup, Analysis and Approach for the Project
Story:
As a dog shelter operator, I need to be able to accurately calculate the dog food requirements each month so that I can order the proper amount of food each month in order to operate the shelter in a costly and efficient manner.
AC:
•	Dog shelter can hold a maximum of 30 dogs at any given time.
•	Small dogs require 10lbs. of food.
•	Medium dogs require 20lbs. of food.
•	Large dogs require 30lbs. of food.
•	Remaining dog food from the previous month if any, should be deducted from the total required before the 20% is added.
•	When ordering food always add at least 20% more than the minimum needed to feed all dogs currently in your shelter for the month.
•	Acceptable values should be positive integers.
•	Formula to order dog food. (small dogs x 10) + (medium dogs x 20) + (large dogs x 30) - (leftover food from previous month) x 1.20 = Grand total of dog food in lbs. that needs to be ordered.
•	Program should be written in Java or Python.
•	Function will take the number of each size of dogs currently in the shelter and remaining food from the last month then return a grand total to order.
•	Project should exist in GitHub.
•	Unit test should cover the function.
•	A README.md should be attached, which includes instructions on how to run the tests, any prerequisites, and any other information that is helpful.

My Analysis and Approach for the Project
Given the hypothetical example of operating a dog shelter, I put my thinking cap on and read through the project carefully several times to make sure I understood the ask? typing some rough notes along the way as I formulated some ideas on the what, why and the how for running the dog shelter and food requirements.
After reading and understanding the example I wrote down the formula to calculate the dog food: (small dogs x 10) + (medium dogs x 20) + (large dogs x 30) - (leftover food from previous month) x 1.20 = Grand total of dog food in lbs. that needs to be ordered.
Considering that I’ve never run a dog shelter I tried to put myself into the shoes of a dog shelter operator, how I would want to calculate the food requirements to be flexible and some of the challenges that I would encounter with the variables that are out of my control.
I took the approach of creating a program that could take inputs from prompts, which could be run many times during the month to handle multiple orders considering that the number of dogs starting at the beginning of the month to the end of the month could fluctuate.
Some lines of codes were purposely left in place and commented out to show some of the refactoring that transpired.
As a quality engineer, one our most difficult tasks is to know when-to-say-when while satisfying our testing requirements and levels of confidence. Given the time frame and recommendations of the projects I kept things simple and concise. 
Some edge cases would be:
We can’t control or predict how many and what size dogs could arrive at the shelter.
Dogs can be adopted or orphaned during any day of the month.
Some months have 28, 30 or even 31 days, therefore, some months will require slightly less food or slightly more food.
We don’t know how long the dogs may stay at the shelter before being adopted.
The formula assumes that the number/size of dogs will be persistent the whole month.
The number of dogs could increase from 5 —> 30 very quickly causing a shortage in food until extra food is ordered, which then may create a surplus if the dogs are cycled quickly.
Some dogs may eat more or less of their allotment, therefore skewing the leftover food amount.
The dog feeder may not be accurate or may be inconsistent when portioning the food.
Since the previous months food is used, there may be spoilage, which can’t be calculated accurately.

Some error cases:
The user may enter non-positive integers.
Someone may enter a number totaling greater than 30 for the number of total dogs (You are attempting to hold more than 30 dogs in your shelter).
The program should give an error when an alpha character is entered (Might be a method or function that could be easily referenced or called when needed for consistency and efficiency for these assertions).
The application should produce errors for special characters (e.g., please enter a number).
There could be a counter that counts the number of dogs being entered and give a warning e.g., (you have 10 out of 30 dogs occupied in your shelter)
1,080 lbs. of food is the maximum food that could be ordered based on a formula using 20% additional, all 30 dogs being large, with no leftover food from the previous month (30 x 30lbs) x 1.20 = 1,080. An error could be displayed when a number is greater than this amount.
An error should be displayed when the amount of dog food to order is zero, but it’s possible that the shelter may not have any dogs and the previous month had no leftover food.
When a multiplier percent is 30% or greater there should be an error or warning asking if they are sure they want to order this much extra food?

Cases not covered in the AC:
Is this a perpetual dog food ordering system? Meaning, can more food be ordered as dogs come and go in the current month?
20% extra is the recommended minimum, does this apply to a range of dog sizes or should there be different percentages based on the size of the dog?
Is there a maximum or minimum for each dog size out of the 30?
The previous months leftover food is not specified nor is the percentage extra used.
How quickly are the dog food orders fulfilled?
How much and how often are the dogs fed?
Are new arrivals able to be adopted on the same day? 
Should the food in lbs. be rounded up to a whole number e.g., should 363.6 lbs be rounded up to 364 lbs.?

Getting Started
Dependencies
	•	PyCharm. install 
	•	Download dogshelter.py file

Installing
	•	Where to download your program: https://www.jetbrains.com/pycharm/download/
	•	Installation requirements: https://www.jetbrains.com/help/pycharm/installation-guide.html#requirements
	•	Any modifications needed to be made to files/folders: Accept defaults
Executing program
	•	Open dogshelter.py
	•	Right click in coding dialog and select “Run ‘dogshelter’”
	•	Answers prompts when displayed:
	“Enter the number of small dogs in your shelter:”
	“Enter the number of medium dogs in your shelter:”
	“Enter the number of large dogs in your shelter:”
	“Enter the number in lbs. of dog food leftover from the previous month:”
	•	When successfully run the current inventory with the number of each dog size and the leftover food should be displayed
	•	20% extra is the default added to the total to calculate the grand total.
	•	The grand total of dog food that should be ordered will be displayed.

Help
Any advise for common problems or issues.
Enter positive integers only
Total number of dogs should be <= 30
Modify line 29 to change the percentage. Example change 1.20 to 1.30 if you want to add 30% additional
Authors
Jonathan Kang
Version History
	•	1.0
	◦	Initial Release
License
This project is licensed under the GPL and free to use and distribute.	 


