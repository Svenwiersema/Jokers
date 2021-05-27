from datetime import date
import pickle



# to do:
# 1. check how long since last joker V
# 2. check how long using this app V
# 3. achievments V
# 

info = {"jokers" : 0, "mJokers": 0, "sMonth" : 0, "sDay" : 0, "sYear" : 0, "oMonth" : 0, "nMonth" : 0, "name" : "name", "nJoker" : 0, "nJokerA" : 0, "lJDay" : 0, "lJMonth" : 0, "lJYear" : 0}
achievments = {"begin" : 0, "spentJoker" : 0, "negative" : 0, "weekU" : 0, "monthU" : 0, "yearU" : 0, "weekNJ" : 0, "monthNJ" : 0, "yearNJ" : 0}
filename = "info.save"
filename2 = "achievments.save"

def beginText(i, a):
	print("Hello and welcome to the addiction coach.")
	print("Please enter your first name down below.\n")
	i["name"] = input()
	print("Hello "+ i["name"])
	i["sDay"] = date.today().day
	i["sMonth"] = date.today().month
	i["sYear"] = date.today().year
	i["nMonth"] = date.today().month
	print("How many jokers do you want on a monthly basis?\n")
	i["mJokers"] = int(input())
	i["jokers"] = i["mJokers"]

	a["begin"] = 1

	startScreen(i, a)

def welcomeBack(i, ni, a, na):
	i = ni
	a = na
	print("Welcome back "+ i["name"])

	i["nMonth"] = date.today().month
	if i["nMonth"] != i["oMonth"]:
		i["jokers"] = i["mJokers"]
		if i["nJoker"] == 1:
			if i["nJokerA"] > i["jokers"]:
				i["jokers"] = 0
				i["nJokerA"] = i["nJokerA"] - i["jokers"]
			else:
				i["jokers"] = i["jokers"] - i["nJokersA"]
				i["nJoker"] = 0



	startScreen(i, a)

def startScreen(i, a):
	print("What do you want to do "+ i["name"] +"?")
	print("1. Check jokers")
	print("2. Check start date")
	print("3. Check days since start")
	print("4. Check when spent last joker")
	print("5. Spent joker")
	print("6. Show achievments")
	print("7. Save & Exit")
	answer = int(input())
	if answer == 1:
		printJokers(i, a)
	elif answer == 2:
		startDate(i, a)
	elif answer == 3:
		CheckDaysSinceStart(i, a)
	elif answer == 4:
		checkLastJoker(i, a)
	elif answer == 5:
		spentJoker(i, a)
	elif answer == 6:
		showAchievments(i, a)
	elif answer == 7:
		saveAndExit(i, a)
	else:
		startScreen(i, a)

def printJokers(i, a):
	if i["nJoker"] == 1:
		print("You have no more jokers, you have "+ str(i["nJokerA"]) +" negative jokers.")
	else:
		print("You have "+ str(i["jokers"]) +" jokers")
	print("press enter to continue")
	input()
	startScreen(i, a)

def startDate(i, a):
	date = str(i["sDay"]) +"-"+ str(i["sMonth"]) +"-"+ str(i["sYear"])
	print(date)
	print("press enter to continue")
	input()
	startScreen(i, a)

def spentJoker(i, a):
	print("Are you sure you want to spent a joker? (y/n)")
	answer = input()

	if answer == "y":
		if i["jokers"] < 1:
			a["negative"] = 1
			i["nJoker"] = 1
			i["nJokerA"] = i["nJokerA"] + 1
		else:
			i["jokers"] = i["jokers"] - 1

		if i["nJoker"] == 1:
			print("You currently have no jokers, but you have "+ str(i["nJokerA"]) +" negative jokers")
		else:
			print("You currently have "+ str(i["jokers"]) +" jokers")

		i["lJDay"] = date.today().day
		i["lJMonth"] = date.today().month
		i["lJYear"] = date.today().year
		i["spentJoker"] = 1

		if a["spentJoker"] == 0:
			a["spentJoker"] = 1

		print("press enter to continue")
		input()
		startScreen(i, a)
	elif answer == "n":
		startScreen(i, a)
	else:
		spentJoker(i, a)

def saveAndExit(i, a):
	print("Are you sure you want to quit? (y/n)")
	answer = input()
	if answer == "y":
		i["oMonth"] = i["nMonth"]
		outfile = open(filename, "wb")
		pickle.dump(i, outfile)
		outfile.close()
		outfile = open(filename2, "wb")
		pickle.dump(a, outfile)
		outfile.close()
		exit()
	elif answer == "n":
		startScreen(i, a)
	else:
		saveAndExit(i, a)

def checkLastJoker(i, a):
	if a["spentJoker"] == 1:
		today = date(date.today().year, date.today().month, date.today().day)
		lJokerDate = date(i["lJYear"], i["lJMonth"], i["lJDay"])
		between = today - lJokerDate
		print(str(between.days) +" days since last joker")

		if between.days >= 7:
			a["weekNJ"] = 1
		elif between.days >= 30:
			a["monthNJ"] = 1
		elif between.days >= 365:
			a["yearNJ"] = 1

	else:
		print("You haven't spent any jokers")

	print("press enter to continue")
	input()
	startScreen(i, a);

def CheckDaysSinceStart(i, a):
	today = date(date.today().year, date.today().month, date.today().day)
	sDate = date(i["sYear"], i["sMonth"], i["sDay"])
	between = today - sDate
	print(str(between.days) +" days since you started with the app")

	if between.days >= 7:
		a["weekU"] = 1
	elif between.days >= 30:
		a["monthU"] = 1
	elif between.days >= 365:
		a["yearU"] = 1

	print("press enter to continue")
	input()
	startScreen(i, a);

def showAchievments(i, a):
	number = 1
	if a["begin"] == 1:
		print(str(number) +". Start the app")
		number += 1
	if a["spentJoker"] == 1:
		print(str(number) +". Spent one joker")
		number += 1
	if a["negative"] == 1:
		print(str(number) +". Have a negative joker")
		number += 1
	if a["weekU"] == 1:
		print(str(number) +". Use the app for a week")
		number += 1
	if a["monthU"] == 1:
		print(str(number) +". Use the app for a month")
		number += 1
	if a["yearU"] == 1:
		print(str(number) +". Use the app for a year")
		number += 1
	if a["weekNJ"] == 1:
		print(str(number) +". Use no joker for a week")
		number += 1
	if a["monthNJ"] == 1:
		print(str(number) +". Use no joker for a month")
		number += 1
	if a["yearNJ"] == 1:
		print(str(number) +". Use no joker for a year")

	print("press enter to continue")
	input()
	startScreen(i, a);

try:
	infile = open(filename, "rb")
	nInfo = pickle.load(infile)
	infile.close()

	infile = open(filename2, "rb")
	nAchievments = pickle.load(infile)
	infile.close()

	welcomeBack(info, nInfo, achievments, nAchievments)
except (OSError, IOError) as e:
	beginText(info, achievments)