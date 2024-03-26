import sys

def getPlayerChoice():
    return input("Rock(1), paper(2), Scissors(3) or 'q' to quit \n")

def getStr(num):
    if num == 1:
        return 'rock'
    if num == 2:
        return 'paper'
    if num == 3:
        return 'scissors'

def getComputerChoice():
    import random
    number = random.randint(1, 3)
    return number

def determineWinner(computerChoice, playerChoice):
    cwin = 'Computer wins!'
    pwin = 'Player wins!'
    if computerChoice == 1:
        if playerChoice == 2:
            return pwin
        if playerChoice == 3:
            return cwin
    if computerChoice == 2:
        if playerChoice == 1:
            return cwin
        if playerChoice == 3:
            return pwin
    if computerChoice == 3:
        if playerChoice == 1:
            return pwin
        if playerChoice == 2:
            return cwin
    return 'Tie!'

def main():
    playerChoice = getPlayerChoice()
    computerChoice = getComputerChoice()
  
    while playerChoice != '4':
        print('Player:', getStr(playerChoice))
        print('Computer:', getStr(computerChoice))
        print(determineWinner(computerChoice, playerChoice))
        playerChoice = getPlayerChoice()
        computerChoice = getComputerChoice()

if __name__ == '__main__':
    main()

