from cards import Cards
from player import Player    

class Game: #Class to contoller the game 

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
    







