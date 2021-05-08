print("Welcome to Band Name Generator")
yourName = input("What's your name?\n")
cityName = input("What's the name of the city you grew up in?\n")
carCompany = input("What's the name of your car company? \n")
birthMonth = input("What's your birth month? \n")
nameGenerator = cityName + yourName[4] + carCompany + birthMonth[1]
print(f"Your band name could be  {nameGenerator}")