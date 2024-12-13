from game import Game
from functions import *

player = Game(input("Put your name here: "))
player2 = Game(input("Put your name here 2: "))

name1 = player.get_name()
name2 = player2.get_name()

print(f"----------Turn to {name1} play -------------")
value1 = player.response_player()

print(f"------------Turn to {name2} play---------------")
value2 = player2.response_player()

find_winner(name1,name2,value1,value2)