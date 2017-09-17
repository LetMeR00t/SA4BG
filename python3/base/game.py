## IMPORTS ##
from abc import ABCMeta, abstractmethod
from base.equipments import Equipments
from base.wincondition import WinCondition
from base.player import Player
from base.history import History


## CLASS ##
class Game(metaclass=ABCMeta):
  """
  Define a Game class
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
    if isinstance(history, History) or history is None:
      self._history = history
    else:
      raise TypeError('"history" attribute for a Game object must be a History object')
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
  def prepare(self,players):
    """
    Abstract method that prepare the game 
    
    Args:
        self: the Game object
        players: a list of Players objects
    
    Returns:
        None
    
    Raises:
        None
    """
    pass

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

  def getWinConditions(self):
    """
    Get the list of WinCondition objects 
    
    Args:
        self: the Game object
    
    Returns:
        the list of WinCondition objects
    
    Raises:
        None
    """ 
    return self._winConditions

  def addVictoryCondition(self,wc):
    """
    Add a win condition in the victory condition list 
    
    Args:
        self: the Game object
        wc: the WinCondition object to add
    
    Returns:
        None
    
    Raises:
        None
    """
    return self._victoryConditions.append(wc)

  def getNumberOfRounds(self):
    """
    Simply get the number of rounds 
    
    Args:
        self: the Game object
    
    Returns:
        an integer that represents the number of rounds
    
    Raises:
        None
    """
    return self._numberOfRounds

  def increaseNumberOfRounds(self):
    """
    Simply increase the number of rounds 
    
    Args:
        self: the Game object
    
    Returns:
        None
    
    Raises:
        None
    """
    self._numberOfRounds += 1

  def getEquipments(self):
    """
    Get the Equipments object of the current game 
    
    Args:
        self: the Game object
    
    Returns:
        The Equipments object
    
    Raises:
        None
    """
    return self._equipments
