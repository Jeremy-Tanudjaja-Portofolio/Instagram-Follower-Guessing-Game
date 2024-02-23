from data import ACCOUNT
from art import *
import random as rand
import os

score = 0

def gameStart():
    global score
    game = True
    account_1 = rand.choice(ACCOUNT)
    account_temp = account_1
    while game:
        account_2 = rand.choice(ACCOUNT)
        while account_2 == account_temp:
            account_2 = rand.choice(ACCOUNT)
        print(logo)
        print(f"compare A {account_temp['name']}, {account_temp['description']} from {account_temp['country']}")
        print(vs)
        print(f"with B {account_2['name']}, {account_2['description']} from {account_2['country']}")
        choice = input("Which has more instagram follower? A|B\n").lower()
        if choice == "a" and account_temp['follower_count']>account_2['follower_count']:
            score += 1
            account_temp = account_1
            print(f"that was correct, your score is now {score}")
        elif choice == "b" and account_temp['follower_count']>account_2['follower_count']:
            game = False
            print(f"That was wrong, your final score is {score}")
        elif choice == "a" and account_2['follower_count'] > account_temp['follower_count']:
            game = False
            print(f"That was wrong, your final score is {score}")
        elif choice == "b" and account_2['follower_count']>account_temp['follower_count']:
            account_temp = account_2
            score += 1
            print(f"that was correct, your score is now {score}")
        input("")
        os.system("cls")

gameStart()