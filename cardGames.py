# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:23:15 2022

@author: mwnew
"""
from random import * #fetches random number commands
import numpy as np
import random 
# psudocode 
# need 3 objects card deck and hand(deck)
# card (object)- suit and number 
#   string output of card and suit 
#   __lt__  less than function to compare the cards so we can order the cards 
# deck made up of cards 
#   addCard(card)
#   popCard()
#   shuffle()
# Hand (subclass of deck) need cards lable and win count 
#   string of hand
#   getLabel()- lable of the hand 
#   roundWinner()
#   getWinCount()

class Card:
    suites = [' of hearts ',' of spades ',' of clubs ',' of diamonds ']
    ranks = [' 2',' 3',' 4',' 5',' 6', ' 7',' 8',' 9',' 10',' J',' Q',' K',' A']
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    # turns suit and card into a readable string and returns it
    def __str__(self):
        return f"{Card.ranks[self.rank]}{Card.suites[self.suit]}"
    
    # create a comparator less than comparator 
    #
    def __lt__(self, other): 
        if self.rank == other.rank:
            return self.suit < other.suit 
        else:
            return self.rank < other.rank 
 
class Deck:
    # deck class creates a deck of 52 cards with no duplicates
    def __init__(self): 
        # Initialises deck class deck is an array of cards 
        self.deck = []
        
        # for loop adds cards to the deck and makes sure there are no duplicates
        for suit in range(4): 
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle() # shuffles the deck automatically when its created
        
    def __len__(self): 
        # gets the length of the deck array 
        return len(self.deck)
    
    def addCard(self, card):
        # adds card objects to the deck array 
        self.deck.append(card)
    
    def popCard(self): 
        # takes a card out of the deck array 
        return self.deck.pop()
    
    def shuffle(self):
        # shuffles cards into random order 
        random.shuffle(self.deck)

class Hand(Deck):
    #Hand is a subclass of Deck which means it gets all of the same attributes as Deck
    
    def __init__(self, label):
        #need to overide the for loops in deck so we dont get 52 cards in our hand
        self.deck = []
        self.label = label
        self.winCount = 0
    def __str__(self):
        return self.label + ': ' + ''.join([str(card) for card in self.deck])

    def getLabel(self):
        return self.label 
    
    def getWinCount(self):
        return self.winCount
    
    def roundWinner(self):
        self.winCount = self.winCount + 1
        
        
        
# Card game 1
#   create deck of cards
#   get 4 players (p1,p2,p3,p4)
#   divide all cards to 4 players 
#   the user is p1,print p1's hand
#   13 rounds 
#       each player plays one card
#       player with highest card wins 
#       update score for the winning hand
#       print cards played in round and the winner 
#   after the rounds print scores for all the players 
        
playing = True
round == 1
 

while playing:
    deck = Deck()
#create array of hands to keep track of our players 
    hands = []
    # create 4 players 
    for i in range(1,5):
        hands.append(Hand(f'P{i}'))
    # distributes cards to players 
    while len(deck) > 0:
        for hand in hands:
            hand.addCard(deck.popCard())
    print(hands[0])
    #13 rounds and then it stops 
    for i in range(13):
        input()
        cardsPlayed = []
        winnerHands = []
        for hand in hands:
            cardsPlayed.append(hand.popCard())
        
            
        roundWinner= max(cardsPlayed)
        winnerHands = hands[cardsPlayed.index(roundWinner)]
        winnerHands.roundWinner()
        
        print(f"R{i}: " + ' ' .join([str(card) for card in cardsPlayed]) + f' Winner:{winnerHands.getLabel()} {str(roundWinner)}')
            
        
        round = 1 + i
    for hand in hands:
        print(f"Score for {hand.getLabel()}: {hand.getWinCount()}")
    if round == 14:
        
        
        playing == False 
    
    




 