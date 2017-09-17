## IMPORTS ##
from base.game import Game

## CLASS ##
class SixNimmt(Game):
  """
  Here, we define the class for the 6 Nimmt! game
  """

  def __init__(self, name="Unamed", equipments=None, winConditions=[], history=None):
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

  def prepare(self):
    """
    Abstract method that prepare the game 
    
    Args:
        self: the Game object
    
    Returns:
        None
    
    Raises:
        None
    """
    pass

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
