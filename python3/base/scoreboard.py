## IMPORTS ##
from player import Player

## CLASS ##
class Scoreboard():
  """
  Define a Scoreboard class
  """

  def __init__(self, players=[]):
    """
    Default constructor that instanciates a Scoreboard class
    
    Args:
        players: A list that contains Player objects
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "players" is not a list of Players objects
    """
    if isinstance(players, list):  
      self._players = {}
      for p in players:
        if not isinstance(p, Player):
          raise TypeError('"players" attribute for a Scoreboard object must be a list of Player objects')
        else:
          self._players[p] = 0
    else:
      raise TypeError('"players" attribute for a Scoreboard object must be a list')

  def getScoreboard(self):
    """
    Get the current scoreboard as a dictionnary
    
    Args:
        self: the Scoreboard object
    
    Returns:
        A dictionnary that details the score of each Player object
    
    Raises:
        None
    """
    return self._players

  def showScoreboard(self):
    """
    Show the current scoreboard as a string representation
    
    Args:
        self: the Scoreboard object
    
    Returns:
        None
    
    Raises:
        None
    """
    for p, s in self._players.items():
      print(str(p)+" has a score equals to "+str(s))
