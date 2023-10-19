import random
import math
import pr1testing
random.seed()


def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1?")
    player2 = input("Name of Player 2?")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def autoplayLoud(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(f"Player 1: {score1}  Player 2: {score2}")
        print("It is Player 1's turn.")
        numDice = strat1(score1, score2, last)
        print((f"{numDice} dice chosen."))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(f"Player 1: {score1}  Player 2: {score2}")
        print("It is PLayer 2's turn.")
        numDice = strat2(score2, score1, last)
        print((f"{numDice} dice chosen."))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True 
    print(f"Player 1: {score1}  Player 2: {score2}")
    if score1 > 100:
        print("Player 2 wins.")
    elif score2 > 100:
        print("Player 1 wins.")
    elif score1 > score2:
        print("Player 1 wins.")
    elif score2 > score1:
        print("Player 2 wins.")
    else:
        print("Tie.")



def autoplay(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:
        numDice = strat1(score1, score2, last)
        diceTotal = 0
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        numDice = strat2(score2, score1, last)
        diceTotal = 0
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            i = i-1
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    if score1 > 100:
        return 2
    elif score2 > 100:
        return 1
    elif score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 3


def manyGames(strat1, strat2, n):
    result = autoplay(strat1, strat2)
    n_times = n // 2
    num = 1
    wins_1 = 0
    wins_2 = 0
    ties_n = 'Ties:'
    ties = 0
    while num <= n_times:
        result = autoplay(strat1, strat2)
        if result == 1:
            wins_1 += 1
        elif result == 2:
            wins_2 += 1
        else:
            ties += 1
        num += 1
    while n_times < n:
        result = autoplay(strat2, strat1)
        if result == 1:
            wins_2 += 1
        elif result == 2:
            wins_1 += 1
        else:
            ties += 1
        n_times += 1
    print(f"Player 1 wins:  {wins_1}")
    print(f"Player 2 wins:  {wins_2}")
    print(f"{ties_n}           {ties}")


def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
        return 12

def sample2(myscore, theirscore, last):
    if myscore <= 50:
        return 30
    elif 51 <= myscore <= 81:
        return 10
    elif myscore > 80:
        return 0

def improve(strategy):
    def another_strat(myscore, theirscore, last):
        if myscore == 100:
            return 0
        else:
            return strategy(myscore, theirscore, last)
    return another_strat
   
def myStrategy(myscore, theirscore, last):
    roll = 0
    if myscore == 0:
        return 33
    elif myscore == 100:
        return 0    
    elif myscore >= 97:
        if theirscore > myscore:
            return (100 - myscore) // 3
        else:
            return 0
    elif myscore >= 90:
        if myscore >= theirscore:
            if (myscore - theirscore) >= 7:
                return (100 - myscore) //4
            elif (myscore - theirscore) >= 3:
                return (100 - myscore) // 3.5
            else:
                roll1 = (100 -myscore) // 3.2
                roll2 = (100 - theirscore) // 3.3
                roll = (roll1 + roll2) //2
        else:
            if (theirscore-myscore) >= 7:
                return (100 - myscore)// 3.3
            elif (theirscore-myscore)>= 4:
                return (100 - myscore) // 3.3
            elif (theirscore -myscore) >= 1:
                return (100 - myscore) //3.5
            else:
                return 3.2
    elif myscore >= 80:
        if myscore >= theirscore:
            if (myscore - theirscore) >= 7:
                return (99 - myscore) //3.3
            elif (myscore - theirscore) >= 4.5:
                 return (100 -myscore) //3
            else:
                return (100 - myscore) // 3.3
        else:
            if (theirscore - myscore) >= 7:
                return (100 - myscore) // 3.2
            elif (theirscore - myscore) >= 3:
                return (100 - myscore) // 3.2
            else:
                return (100 - myscore) // 3.2
    elif myscore >= 70:
        if max(myscore, theirscore) == myscore:
            return (100 - myscore)// 3.5
        else:
            return (100 - myscore) // 3.2
    elif myscore >= 60:
        if max(myscore, theirscore) == myscore:
            return (100 - myscore) // 3.3
        else:
            return (100 - myscore) // 3.3
    elif myscore >= 50:
        if myscore >= theirscore:
            return (100 - myscore) //2.8
        else:
            return (100 - myscore)// 2.8
    else:
        return (100 - myscore) // 2
    return int(roll)   