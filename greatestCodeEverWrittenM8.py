import math
from math import sin
from math import cos
from math import tan
import urllib.request
import random


r1 = urllib.request.urlopen("https://api.gouv.fr/les-api/api-geo")
r2 = urllib.request.urlopen("http://calapi.inadiutorium.cz/")
r3 = urllib.request.urlopen("https://lyricsovh.docs.apiary.io/")

flub = ["£","£","£","£","£","£","£","£","£","£"]
flui = ["₹","₹","₹","₹","₹","₹","₹","₹","₹","₹"]
flubr = ["R$£","R$£","R$£","R$£","R$£","R$£","R$£","R$£"]
fluusd = ["$","$","$","$","$","$","$","$","$","$","$"]
flup = ["₱","₱","₱","₱","₱","₱","₱","₱","₱","₱"]

the_array = ["i", "!", "u", "k", "h", "¿", "q","j","?","e","y","o","a","z",
"r","s","l","g","d","?", "w","f","z","m","t", "(", ")", "g","p",":", "n", " "]

def even_or_not(num):
    if (num % 2) == 0:
       print('even')
    else:
       print('odd')


def fakeStripFunction(string="", char=""):
    if char == "":
        regex = re.compile(r'( *)([a-zA-Z0-9]*)( *)')
        mo = regex.search(string)
        print(mo.group(2))
    else:
        regex = re.compile(r'[^'+char+'].*[^'+char+']')
        mo = regex.search(string)
        print(mo.group())

ctb = []
ctb.append(the_array[12])
ctb.append(the_array[16])
ctb.append(the_array[len(flub) - 10])
ctb.append(the_array[len(the_array) - 2])
ctb.append(the_array[(2*2*2)+1])
ctb.append(the_array[len(the_array) - 1])
ctb.append(the_array[15])
ctb.append(the_array[23])
ctb.append(the_array[(2*2*2)+1])
ctb.append(the_array[16])
ctb.append(the_array[16])
ctb.append(the_array[15])
ctb.append(the_array[len(the_array) - 1])
ctb.append(the_array[29])
ctb.append(the_array[26])

ctb_final="".join(ctb)
print(ctb_final.capitalize())


def infinite(i):
    while true:
        i + 1

albums = [
    "Showbiz",
    "Origin of Symmetry",
    "Absolution",
    "Black Holes and Revelations",
    "The Resistance",
    "The 2nd Law",
    "Drones",
    "Simulation Theory"
    ]

colours = [
    "red",
    "blue",
    "green",
    "yellow",
    "lilac",
    "black",
    "white",
    "purple",
    "indigo",
    "violet",
    "maroon",
    ]

scg = [
    "Self-titled",
    "Pandora Tomorrow",
    "Chaos Theory",
    "Double Agent",
    "Conviction",
    "Blacklist",
    ]

def collatz(number):
    try:
        number = int(number)
        while (number) != 1:
            if (number) % 2 == 0:
                number = int((number/2))
                print(number)
            elif int(number) % 2 == 1:
                number = int((number * 3) + 1)
                print(number)
        print("1")
        print("We'll end it here so the cycle doesn't continue forever!")
    except ValueError:
        print("please enter a correct value")

def fizzbuzz():      
    for i in range (0, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
def magic8ball():
    magic_8_ball_options = [
    "You will guess coin tosses .38% more accurately",
    "Your wife is cheating on you. Even if you don't have a wife, she still is.",
    "You sill struggle to open every 3rd packet of bread that you open",
    "Help, I'm stuck in a magic 8 ball factory!",
    "Try again, idiot",
    "Yes",
    "Ut oh"]


    print(magic_8_ball_options[random.randint(0, (len(magic_8_ball_options) - 1))])

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for j in range(len(tableData[i])):
            if len(tableData[i][j]) > colWidths[i]:
                colWidths[i] = len(tableData[i][j])
            
    for x in range(len(tableData[0])):   
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidths[y]), end =" ")

import sys

deck = [  # one full deck (no jokers)
    "ace",
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    "jack",
    "queen",
    "king",
]


full_deck = deck
player_cards = [0]
dealer_cards = [0]
dealer_stand = ""
player_stand = ""

def endgame_call():
    endgame()

def endgame():
    global player_cards
    global dealer_cards
    global player_stand
    global dealer_stand
    endgame = input(
        "Would you like to play again?\nHit 'y' to play again, 'n' to exit\n")
    if endgame == "y":
        player_cards = [0]
        dealer_cards = [0]
        dealer_stand = ""
        player_stand = ""
        ace_question()
        player_hit()
    elif endgame == "n":
        exit()
    else:
        endgame_call()



def endgame_comparison():
    global player_cards
    global dealer_cards
    if player_cards[0] > dealer_cards[0]:
        print("The value of your cards is higher than the house's, you win!")
        endgame()
    elif dealer_cards[0] > player_cards[0]:
        print(
            "The house's cards are greater than yours, the house wins.\nBetter luck next time!")
        endgame()


def hit_or_stand_question_comparison():
    if player_stand == "true" and dealer_stand == "true":
        endgame_comparison()
    else:
        hit_or_stand_question()


def hit_or_stand_question():
    global player_stand
    global dealer_stand
    hit_or_stand = input(
        "Would you like to hit, or stand?\nPress 'h' to hit, 's' to stand\n")
    if hit_or_stand == "h":
        player_hit()
    elif hit_or_stand == "s":
        player_stand = "true"
        if dealer_cards[0] > player_cards[0]:
            print("You lose, better luck next time!")
            endgame()
        dealer_hit()
    else:
        hit_or_stand_question()


def ace_question():
    global full_deck
    ace_answer = input(
        "Would you like aces to be high or low?\nHit 'h' or 'l' and then hit 'enter'\n")
    if ace_answer == "h":
        deck[0] = 11  # turns the ace into an 11
        full_deck = deck * 24
    elif ace_answer == "l":
        deck[0] = 1  # turns the ace into a 1
        full_deck = deck * 24
    else:
        ace_question()


def player_hit():
    global full_deck
    global player_cards
    i = random.randint(0, len(full_deck)-1)
    new_player_card = full_deck[i]
    if new_player_card == "king":
        new_player_card = int(10)
        print("The dealer deals you a king")
    elif new_player_card == "queen":
        new_player_card = int(10)
        print("The dealer deals you a queen")
    elif new_player_card == "jack":
        new_player_card = int(10)
        print("The dealer deals you a jack")
    else:
        new_player_card = int(new_player_card)
        print("The dealer deals you a " + str(new_player_card))
    player_cards[0] += new_player_card
    print("The total value of your cards is " + str(player_cards[0]))
    if player_cards[0] > 21:
        print("You go bust; the house wins.\nBetter luck next time!")
        endgame()
    elif player_cards[0] == 21:
        print("You got Blackjack! You Win!")
        endgame()
    else:
        dealer_hit()


def dealer_hit():
    global full_deck
    global dealer_cards
    global dealer_stand
    j = random.randint(0, len(full_deck)-1)
    while dealer_cards[0] < 17:
        new_dealer_card = full_deck[j]
        if new_dealer_card == "king":
            new_dealer_card = int(10)
            print("The dealer reveals a king")
        elif new_dealer_card == "queen":
            new_dealer_card = int(10)
            print("The dealer reveals a queen")
        elif new_dealer_card == "jack":
            new_dealer_card = int(10)
            print("The dealer reveals a jack")
        else:
            new_dealer_card = int(new_dealer_card)
            print("The dealer reveals a " + str(new_dealer_card))
        dealer_cards[0] += new_dealer_card
        print("The total value of the dealer's cards is " +
              str(dealer_cards[0]))
        if dealer_cards[0] > 21:
            print("The house goes bust, you win!")
            endgame()
        if dealer_cards[0] == 21:
            print("The house got Blackjack.\nBetter luck next time!")
            endgame()
        elif dealer_cards[0] == 17 or dealer_cards[0] > 17:
            print("The dealer stands")
            dealer_stand = "true"
            hit_or_stand_question_comparison()
        else:
            hit_or_stand_question_comparison()


