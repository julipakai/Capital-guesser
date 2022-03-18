#import modules
from re import A
from tkinter import W
import requests
import random
#import api
countries_call = "https://restcountries.com/v3.1/all?fields=name,capital"
response = requests.get(countries_call)
#print(response.status_code)

#get user's name
countries = response.json()
def intro():
    uinput = input("Welcome to capital-guesser!\nWhat's your name? ")
    return str(uinput)

#selectring wrong answers
def wcountries(countrylength):
    caplist = []
    wrongcountries = random.sample(range(countrylength), 3)
    for i in range (0, 3):
        wcountry = wrongcountries[i]
        caplist.append(countries[wcountry]["capital"][0])
    return caplist

#the game itself
def startgame(name):
    print(f"Hello {name}")
    countrylength = len(countries)
    randomcountry = random.randint(0, countrylength)
    i=0
    points = 0
    caplist = []
    for i in range (0, 5):
        randomcountry = random.randint(0, countrylength)
        rcountry = countries[randomcountry]["name"]["common"]
        rcapital = countries[randomcountry]["capital"][0]
        randomcountry = random.randint(0, countrylength)
        capl = wcountries(countrylength)
        capl.append(rcapital)
        random.shuffle(capl)
        corrindex = capl.index(rcapital)
        corranswer = capl[corrindex]
        a = capl[0]
        b = capl[1]
        c = capl[2]
        d = capl[3]
        print(corranswer)
        user_input = int(input(f"What is the capital city of {rcountry}?\n1: {a}   2: {b}\n3: {c}   4: {d}\n"))-1
        if user_input == corrindex:
            points += 1
            print(f"Correct! You have {points} points.")
        elif user_input != corrindex:
            print(f"Incorrect. The correct answer is {rcapital}. You have {points} points.")
    return points 

#leaderboard
def leaderboard(points, name):
    with open('countryguesserleaderboard.txt', 'a') as lboard:
        scoredict = { 'username' : name, 'score' : str(points)}
        text = scoredict.get('username') + ' - ' +  scoredict.get('score')
        lboard.write(f'\n {text}')

#start game
while input("would you like to play capital guesser?") != "no":
    name = intro()
    points = startgame(name)
    leaderboard(points, name)