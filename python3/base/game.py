## IMPORTS ##
from abc import ABCMeta, abstractmethod
from equipments import Equipments
from wincondition import WinCondition
from player import Player

## CLASS ##
class Game(metaclass=ABCMeta):
  """
  Define a Game class
  """

  def __init__(self, name="Unamed", equipments=None, winConditions=[], players=[]):
    """
    Default constructor that instanciates a Game class
    
    Args:
        name: A string that represents the Game object
        equipments: An Equipment object that represents all the equipments
        winConditions: A list that represents all the WinCondition objects
        players: A list that represents all the Player objects, the order of the list will be used as order of the game
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(name, str):
      self._name =  name
    else:
      raise TypeError('"name" attribute for a Game object must be a string')
    if isinstance(equipments, Equipments) or equipments is None:
      self._equipments = equipments
    else:
      raise TypeError('"equipments" attribute for a Game object must be a list')
    if isinstance(winConditions, list):
      for w in winConditions:
        if isinstance(w, WinCondition):
          raise TypeError('Each object of the "winConditions" attribute must be a WinCondition object')
      self._winConditions = winConditions
    else:
      raise TypeError('"winConditions" attribute for a WinCondition object must be a list')
    if isinstance(players, list):
      for p in players:
        if not isinstance(p, Player):
          raise TypeError('"players" attribute for a Game object must be a list of Player objects')
      self._players = players
    else:
      raise TypeError('"players" attribute for a Game object must be a list')
    # Define a number of rounds equals to 1
    self._numberOfRounds = 1
    # Define a variable that will contain the win condition(s)
    self._victoryConditions = []

  def __str__(self):
    """
    Define the string representation of a Game object
    
    Args:
        self: the Game object
    
    Returns:
        A string that represents the Game object
    
    Raises:
        None
    """
    return "Game \""+self._name+"\""

  @abstractmethod
  def init(self):
    """
    Abstract method that initiate the game 
    
    Args:
        self: the Game object
    
    Returns:
        None
    
    Raises:
        None
    """
    pass

  def play(self):
    """
    Play a complete game (initiate, start the game and end when a win condition happens)
    
    Args:
        self: the Game object
    
    Returns:
        None
    
    Raises:
        None
    """
    end = False
    i = 0
    numberOfPlayers = len(self._players)

    # Initialize the game
    self.init() 
   
    # Play the game while no win condition happens
    while (end == False):
      # Play a turn for a player
      self.playTurnForPlayer(self._players[i%numberOfPlayers])
      i += 1
      # Check the win conditions
      for wc in self._winConditions:
        if wc.checkCondition(self):
          self._victoryConditions.append(wc)
          end = True
      if (end == False and i%numberOfPlayers == 0):
        self._numberOfRounds += 1
        

  @abstractmethod
  def playTurnForPlayer(self,player):
    """
    Play a turn for a Player object given in parameter
    This abstract method defines the way how the player plays at his round
    
    Args:
        self: the Game object
        player: the Player object that represents the player who plays his round
    
    Returns:
        None
    
    Raises:
        None
    """
    pass

  def getPlayers(self):
    """
    Get the players of the game
    
    Args:
        self: the Game object
    
    Returns:
        A list of Player objects
    
    Raises:
        None
    """
    return self._players
