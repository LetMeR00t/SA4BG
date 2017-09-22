## IMPORTS ##
from base.game import Game
from sixNimmt.equipments import SixNimmtEquipments

## CLASS ##
class SixNimmt(Game):
  """
  Here, we define the class for the 6 Nimmt! game
  """

  def __init__(self, name="6 Nimmt!", equipments=SixNimmtEquipments(), winConditions=[], history=None):
    """
    Default constructor that instanciates a Game class
    
    Args:
        name: A string that represents the Game object
        equipments: An Equipment object that represents all the equipments
        winConditions: A list that represents all the WinCondition objects
        history: A History object that represents all actions realized during the game
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    super().__init__(name,equipments,winConditions,history)

  def prepare(self, players):
    """
    Prepare the game 
    
    Args:
        self: the Game object
        players: a list of SixNimmtPlayer objects
    
    Returns:
        None
    
    Raises:
        None
    """
    # Get the Equipments object
    equipments = self.getEquipments()

    # Shuffle the cards, there is only one stack in this game so the index is 0
    equipments.shuffleTheCards(0)

    # Distribute cards to each player
    for p in players:
      for i in range(0,10):
        p.getEquipments().addCard(0,equipments.popCard(0))
      print(p)

  def playTurnForPlayer(self,player):
    """
    Play a turn for a Player object given in parameter
    
    Args:
        self: the Game object
        player: the Player object that represents the player who plays his round
    
    Returns:
        None
    
    Raises:
        None
    """
    pass

  def reset(self):
    """
    This method reset the game for a new party
    
    Args:
        self: the Game object
    
    Returns:
        None
    
    Raises:
        None
    """
    pass
 
