{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Bold;\f1\froman\fcharset0 Times-Roman;\f2\fnil\fcharset0 Menlo-Regular;
\f3\fnil\fcharset0 LucidaGrande;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid201\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid3}
{\list\listtemplateid4\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid301\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid302\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid4}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}{\listoverride\listid4\listoverridecount0\ls4}}
\margl1440\margr1440\vieww20760\viewh18280\viewkind0
\deftab720
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 \expnd0\expndtw0\kerning0
Monthly Food Calculator for Friendly Paws Dog Shelter\
Description\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf2 This program uses input data via questionnaire-style prompts for the number of dogs/respective sizes and leftover food from the previous month to calculate the food requirements in lbs. which needs to be ordered for sustaining the animals in the shelter.\
The previous months leftover food should be deducted from the total required and then 20% added to calculate the grand total.\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 My Story Writeup, Analysis and Approach for the Project\
Story:\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf2 As a dog shelter operator, I need be able to accurately calculate the dog food requirements each month so that I can order the proper amount of food each month in order to operate the shelter in a costly and efficient manner.\
\pard\pardeftab720\sa240\partightenfactor0

\f0\b \cf2 AC:
\f1\b0 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\cf2 \kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Dog shelter can hold a maximum of 30 dogs at any given time.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Small dogs require 10lbs. of food.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Medium dogs require 20lbs. of food.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Large dogs require 30lbs. of food.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Remaining dog food from the previous month if any, should be deducted from the total required before the 20% is added.\
\kerning1\expnd0\expndtw0 \'95	When ordering food always add at least \expnd0\expndtw0\kerning0
20% more than the minimum needed to feed all dogs currently in your shelter for the month.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Acceptable values should positive integers.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Formula to order dog food. (small dogs x 10) + (medium dogs x 20) + (large dogs x 30) - (leftover food from previous month) x 1.20 = Grand total of dog food in lbs. that needs to be ordered.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Program should be written in Java or Python.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Function will take the number of each size of dog currently in the shelter and remaining food from last month then return a total to order.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Project should exist in GitHub.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
Unit test should cover the function.\
\kerning1\expnd0\expndtw0 \'95	\expnd0\expndtw0\kerning0
A README.md should be attached, which includes instructions on how to run the tests, any prerequisites, and any other information that is helpful.\
\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 My Analysis and Approach for the Project\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf2 Given the hypothetical example of operating a dog shelter, I put my thinking cap on and read through the project carefully several times to make sure I understood the ask? typing some rough notes along the way as I formulated some ideas on the what, why and the how for running the dog shelter and food requirements.\
After reading and understanding the example I wrote down the formula to calculate the dog food: (small dogs x 10) + (medium dogs x 20) + (large dogs x 30) - (leftover food from previous month) x 1.20 = Grand total of dog food in lbs. that needs to be ordered.\
Considering that I\'92ve never run a dog shelter I tried to put myself into the shoes of a dog shelter operator, how I would want to calculate the food requirements to be flexible and some of the challenges that I would encounter with the variables that are out of my control.\
I took the approach of creating a program that could take inputs from prompts which could be run many times during the month to handle multiple orders considering that the number of dogs starting at the beginning of the month to the end of the month could fluctuate.\
Some lines of codes were purposely left in place and commented out to show some of the refactoring that transpired.\
As a quality engineer, one our most difficult tasks is to know when-to-say-when while satisfying our testing requirements and level of confidence. Given the time and recommendations of the projects I kept things simple and concise. \
\pard\pardeftab720\sa240\partightenfactor0

\f0\b \cf2 Some edge cases would be:\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0 \cf2 We can\'92t control or predict how many and what size dogs could arrive at the shelter.\
Dogs can be adopted or orphaned during any day of the month.\
Some months have 28, 30 or even 31 days, therefore some months will require slightly less food or slightly more food.\
We don\'92t know how long the dogs may stay at the shelter before being adopted.\
The formula assumes that the number/size of dogs will be persistent the whole month.\
The number of dogs could increase from 5 \'97> 30 very quickly causing a shortage in food until extra food is ordered, which then may create a surplus if the dogs are cycled quickly.\
Some dogs may eat more or less of their allotment, therefore skewing the leftover food amount.
\f0\b \

\f1\b0 The dog feeder may not be accurate or inconsistent when portioning the food.\
Since the previous months food is used, there may be spoilage, which can\'92t be calculated accurately.\
\
\pard\pardeftab720\sa240\partightenfactor0

\f0\b \cf2 Some error cases:\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0 \cf2 The user may enter non-positive integers.\
Someone may enter a number totaling greater than 30 for the number of total dogs (You are attempting to hold more than 30 dogs in your shelter).\
The program should give an error when an alpha character is entered (Might be a method or function that could be easily referenced or called when needed for consistency and efficiency).\
The application should produce errors for special characters (e.g., please enter a number).\
There could be a counter that counts the number of dogs being entered and give a warning e.g., (you have 10 out of 30 dogs occupied in your shelter)\
1,080 lbs. of food is the maximum food that could be ordered based on a formula using 20% additional, all 30 dogs being large, with no leftover food from the previous month (30 x 30lbs) x 1.20 = 1,080. An error could be displayed when a number is greater than this amount.\
An error should be displayed when the amount of dog food to order is zero, but it\'92s possible that the shelter may not have any dogs and the previous month had no leftover food.\
When a multiplier percent is 30% or greater there should be an error asking if they are sure they want to order this much extra food?
\f0\b \
\
Cases not covered in the AC:\

\f1\b0 Is this a perpetual dog food ordering system, meaning can more food be ordered as dogs come and go in the current month?\
20% extra is the recommended minimum, does this apply to a range of dog sizes or should there be different percentages based on the size of the dog?\
Is there a maximum or minimum for each dog size?\
The previous months leftover food is not specified nor is the percentage extra used.\
How quickly are the dog food orders fulfilled?\
How much and how often are the dogs fed?\
Are new arrivals able to be adopted on the same day? \
Should the food in lbs. be rounded up to a whole number e.g., should 363.6 lbs be rounded up to 364 lbs.?\
\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 Getting Started\
\pard\pardeftab720\sa280\partightenfactor0

\fs28 \cf2 Dependencies\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f1\b0\fs24 \cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
PyCharm. install \
\ls1\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}Download \expnd0\expndtw0\kerning0
dogshelter.py file\
\pard\tx720\pardeftab720\partightenfactor0
\cf2 \
\pard\pardeftab720\sa280\partightenfactor0

\f0\b\fs28 \cf2 Installing\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls2\ilvl0
\f1\b0\fs24 \cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Where to download your program: https://www.jetbrains.com/pycharm/download/\
\ls2\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}Installation requirements: \expnd0\expndtw0\kerning0
https://www.jetbrains.com/help/pycharm/installation-guide.html#requirements\
\ls2\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Any modifications needed to be made to files/folders: Accept defaults\
\pard\pardeftab720\sa280\partightenfactor0

\f0\b\fs28 \cf2 Executing program\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls3\ilvl0
\f1\b0\fs24 \cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Open dogshelter.py\
\ls3\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Right click in coding dialog and select \'93Run \'91dogshelter\'92\'94\
\ls3\ilvl0\kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
Answers prompts when displayed:\
\pard\tx720\pardeftab720\partightenfactor0

\f2 \cf2 	\'93
\f1 Enter the number of small dogs in your shelter:\'94\
	
\f2 \'93
\f1 Enter the number of medium dogs in your shelter:\'94\
	
\f2 \'93
\f1 Enter the number of large dogs in your shelter:\'94\
	\'93Enter the number in lbs. of dog food leftover from the previous month:\'94\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\cf2 \kerning1\expnd0\expndtw0 	\'95	\expnd0\expndtw0\kerning0
When successfully run the current inventory with the number of each dog size and the leftover food should be displayed\
\kerning1\expnd0\expndtw0 	\'95	\expnd0\expndtw0\kerning0
20% extra is the default added to the total to calculate the grand total.\
\kerning1\expnd0\expndtw0 	\'95	\expnd0\expndtw0\kerning0
The grand total of dog food that should be ordered will be displayed.
\f2 \
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 \
Help\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf2 Any advise for common problems or issues.
\f2 \

\f1 Enter positive integers only\
Total number of dogs should be <= 30\
Modify line 29 to change the percentage. Example change 1.20 to 1.30 if you want to add 30% additional
\f2 \
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 Authors\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf2 Jonathan Kang\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 Version History
\f1\b0\fs24 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls4\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
1.0\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\partightenfactor0
\ls4\ilvl1\cf2 \kerning1\expnd0\expndtw0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
Initial Release\
\pard\pardeftab720\sa298\partightenfactor0

\f0\b\fs36 \cf2 License\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf2 This project is licensed under the GPL and free to use and distribute.	 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \
}