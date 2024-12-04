# import player
# import cards

import random as r
class Cards:
    def __init__(self):

        self.list_cards_to_player = ["ACE" , "2", "3" ,"4" , "5", "6", "7", "8" , "9" , "10", "Jack", "Queen", "King"]
        self.list_categories = ["Hearts" , "Diamonts", "Clubs" , "Spodes"]

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
        This function is resposible to chek each value tha was drawn and retorned it
        
        '''
        card = self.draw_cart()

        if card == "Jack" or card == "Queen" or card == "King":
            return 10
        elif card == "Ace":
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
        card_drawn = self.check_card()
        categories_drawn = self.draw_categories()

        players_hand = [
            ["Cards: "], ["Categories"]
        ]

    

        players_hand[0].append(card_drawn)
        players_hand[1].append(categories_drawn)

        return players_hand
    
        

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
        while True:
            response = input("Do you wanna buy a card?  Answer with Y or Yes").upper()
            if response == "Y" or response == "YES":
                card = self.hand_cards_player.cards_played()
            print(card)


teste = Game("Kauan")
teste.response_player()


    

    
    
    




teste = Game(input('Digite seu nome: '))
print(teste.get_name())
