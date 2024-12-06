# import player
# import cards

import random as r
class Cards:
    def __init__(self):

        self.list_cards_to_player = ["ACE" , "2", "3" ,"4" , "5", "6", "7", "8" , "9" , "10", "Jack", "Queen", "King"]
        self.list_categories = ["Hearts" , "Diamonts", "Clubs" , "Spodes"]
        self.value =0

    def draw_cart(self):
        '''
        This function is resposible to draw a card from card`s deck

        '''
        card = r.randint(0,12)
        card_drawn = self.list_cards_to_player[card]

        return card_drawn
    
    def cut_card_deck(self, list_cards_to_player):
        '''
        This function is resposible to take out cards that alreary were drawn

        '''
        length_list_cards_to_player = len(list_cards_to_player)
        cuted_list_cards_to_player = list_cards_to_player.pop([0, length_list_cards_to_player -1])

        return cuted_list_cards_to_player



    def check_card(self):
        '''
        This function is resposible to check each value tha was drawn and retorned it
        
        '''
        card = self.draw_cart()

        if card == "Jack" or card == "Queen" or card == "King":
            return 10
        elif card == "ACE":
            return 11
        else:
            return int(card)
        
    def draw_categories(self):
        '''
        This function is resposible to draw a categories 
        
        '''
        categories_drawn = r.randint(0,3)
        return self.list_categories[categories_drawn]

    def cards_played(self):
        '''
        This function makes a card`s hand of player and return this
        
        '''

        players_hand = [
            ["Cards: "], 
            ["Categories:"]
        ]

        accumulate = 0

        while True:

            '''
            
            Here, we are using our functions ago , and it doing the hand's value
            
            '''
            

            card_drawn = self.check_card()
            categories_drawn = self.draw_categories()
            

            response = input("Do you wanna buy a card?  Answer with y or n:").upper()

            if response == "Y" or response == "YES":

                players_hand[0].append(card_drawn)
                players_hand[1].append(categories_drawn)
                accumulate += card_drawn
                
                print(players_hand)
                print(accumulate)


                if accumulate > 21:
                    return accumulate
                    
            else:
                break

        return accumulate
    
        

class Player:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name



class Game:

    def __init__(self, name):
        self.player = Player(name)
        self.hand_cards_player = Cards()

    def get_name(self):
        return self.player.get_name()
    
    def response_player(self):
       
        '''
        This function will returned the hand's value 
        after the player have choesen to stop

        '''
        
        value = self.hand_cards_player.cards_played()            
        return value
    

player = Game(input("Put your name here: "))
player2 = Game(input("Put your name here 2: "))

name1 = player.get_name()
name2 = player2.get_name()

print(f"Turn to {name1} play: ")
value1 = player.response_player()

print(f"Turn to {name2} play")
value2 = player2.response_player()

    
def find_winner(name1, name2, value1, value2):

    if value1 <=21 and value1 > value2:
        print(f"{name1} won!")
    elif value1 == value2:
        print(f"Draw")
    else:
        print(f"{name2} won!")

find_winner(name1,name2,value1,value2)
