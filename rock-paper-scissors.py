#Rock Paper Scissors!
#8KY for noobs
#https://www.codewars.com/kata/rock-paper-scissors/

def rps(p1, p2):
    beats = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    if p1 == p2:
        return 'Draw!'
    elif beats[p1] == p2:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'

rps('rock', 'scissors') # "Player 1 won!"
rps('scissors', 'paper') # "Player 1 won!"
rps('paper', 'rock') # "Player 1 won!"

rps('scissors', 'rock') # "Player 2 won!"
rps('paper', 'scissors') # "Player 2 won!"
rps('rock', 'paper') # "Player 2 won!"