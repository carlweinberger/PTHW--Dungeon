###########  Exercise 36: Designing and Debugging

class Room():
    ''' Room Class: This defines the room instances in the game. It defines the ways in and out of a room, the description, of the room
descriptions of the possible user choices in the room, and The behavior of the room'''

    def __init__(self):
        self.roomName = "Unspecified Name"
        self.roomDescription = "Unspecified Description"


 class Player():
    '''Player Class: This class defines: The player object.'''
    def __init__(self):
        self.playerName = "Unspecified Name"


class Monster():
    '''Monster Class: This class defines the monster object.'''
    def __init__(self):
        self.monsterName = "Unspecified Name"
        self.monsterDescription = "Unspecified Description"

#### Game Object Instances
lobby = Room()


### Main Loop
Dead = True # Stubbing the code.
While not dead do: 
    # move