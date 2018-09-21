import countryList
import random, re, os, time

os.system("clear")
Country = countryList.country[random.randrange(len(countryList.country))]
randomCountry = Country.lower()
hiddenCountry = list(randomCountry)
noOfChars = len(randomCountry)

spaces = list()
for i in range(len(randomCountry)):
	if randomCountry[i] == ' ':
		spaces.append(i)

country = str('-'*len(randomCountry))
country = list(country)

if spaces != []:
	for space in spaces:
		country[space] = ' '

hiddenCountryName = ''.join(country)
print ("Guess the country\n")
print (hiddenCountryName)
hiddenCountryList = list(hiddenCountryName)

playChances = 3
flag = flag1 = 0
x = 1

lines = '-'*80
leftmargin = '|' + ' '*30
rightmargin = ' '*32 + '|'
spaces = 16*' '

incorrectLetters = list()
correctLetters = list()

while 1:
	#os.system('clear')
	print ('_'*90)
	flag = 0
	inputChar = str(input("Enter a letter: "))
	
	if inputChar in incorrectLetters or inputChar in correctLetters:
		print ("Letter already used")
		continue
		
	for i in range(len(randomCountry)):
		if hiddenCountry[i] == inputChar:
			hiddenCountryList[i] = inputChar
			correctLetters.append(inputChar)
			flag = 1
			
	if flag == 1:
		print (lines)
		print (leftmargin + "Current Progress" + rightmargin)
		print (leftmargin + spaces + rightmargin)
		currentProgress = ''.join(hiddenCountryList)
		print (leftmargin + currentProgress + (80-32-len(currentProgress))*' ' + '|')
		print (leftmargin + spaces + rightmargin)
		print (leftmargin + "CHANCES LEFT - ", playChances, (80-35-len('CHANCES LEFT - '))*' ' + '|')
		print (leftmargin + spaces + rightmargin)
		print (lines)
	elif flag == 0:
		print ("Letter " + inputChar.upper() + " not in the country name")
		print ("You have ", playChances, " chances left")
		incorrectLetters.append(inputChar)
		playChances -= 1
	
	if playChances < 0:
		print ("\nYou failed to identify the country")
		break

	print (spaces + "INCORRECT LETTERS: ", incorrectLetters)
	if '-' in hiddenCountryList:
		continue
	else:
		print ("CONGRATS, YOU WON")
		break

print ("The country is " + randomCountry.upper())