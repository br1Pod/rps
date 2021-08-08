from models.player import *

def play(p1, p2):
# case p1 rock
    if p1.choice == self.player.choice[0]:
        if p2.choice == Player.choice[1]:
            return win(p2)
        elif p2.choice == Player.choice[2]:
            return win(p1)
        else:
            return draw()
# case p1 paper
    elif p1.choice == Player.choice[1]:
        if p2.choice == Player.choice[0]:
            return win(p1)
        elif p2.choice == Player.choice[2]:
            return win(p2)
        else:
            return draw()
# case p1 scissors
    elif p1.choice == Player.choice[2]:
        if p2.choice == Player.choice[0]:
            return win(p2)
        elif p2.choice == Player.choice[1]:
            return win(p1)
        else:
            return draw()
# case p1 no choice yet
    else:
        return "Please choose Rock, Paper or Scissors"

def win(player):
    return f"{player.name} Wins"

def draw():
    return f"It's a Draw"