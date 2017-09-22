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
        None
    """
    # Set the name of the game
    self.setName(name)

    # Set the Equipments for this game
    self.setEquipments(equipments)

    # Set all of the WinConditions for this game
    self.setWinConditions(winConditions)

    # Set a History for the game
    self.setHistory(history)

    # Define a number of rounds equals to 1
    self.setNumberOfRounds(1)

    # Define a variable that will contain the win condition(s) when a game is finished
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

  @abstractmethod
  def reset(self):
    """
    This method reset the game for a new party
    This abstract method defines how the game is reset
    
    Args:
        self: the Game object
    
    Returns:
        None
    
    Raises:
        None
    """
    pass

  def getVictoryCondition(self):
    """
    Get all the WinConditions in the victory conditions list 
    
    Args:
        self: the Game object
    
    Returns:
        A list of all WinConditions that matched 
    
    Raises:
        None
    """
    return self._victoryConditions

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
    return self.getVictoryConditions().append(wc)

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

  def setNumberOfRounds(self,newNumberOfRounds):
    """
    Set the number of rounds 
    
    Args:
        self: the Game object
        newNumberOfRounds: an integer that represent the number of rounds to update
    
    Returns:
        None
    
    Raises:
        TypeError: Raise a TypeError if "newNumberOfRounds" is not an integer
    """
    if isinstance(newNumberOfRounds, int):
      self._numberOfRounds = newNumberOfRounds
    else:
      raise TypeError('"numberOfRounds" attribute for a Game object must be an integer')

  def getName(self):
    """
    Get the name of the Game object
    
    Args:
        self: the Game object
    
    Returns:
        A string that represents the name
    
    Raises:
        None
    """
    return self._name
 
  def setName(self,newName):
    """
    Set the name of the Game object
    
    Args:
        self: the Game object
        newName: A string that represents the name
    
    Returns:
        None
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(newName, str):
      self._name = newName
    else:
      raise TypeError('"name" attribute for a Game object must be a string')

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

  def setEquipments(self,newEquipments):
    """
    Set the Equipments object of the current game 
    
    Args:
        self: the Game object
        newEquipments: An Equipments object that represent all the private equipments of this player
    
    Returns:
        The Equipments object
    
    Raises:
        TypeError: Raise a TypeError if "newEquipments" is not an Equipments object
    """
    if isinstance(newEquipments, Equipments) or newEquipments is None:
      self._equipments = newEquipments
    else:
      raise TypeError('"equipments" attribute for a Game object must be a list')
 
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

  def setWinConditions(self,newWinConditions):
    """
    Set the WinConditions list of the current game 
    
    Args:
        self: the Game object
        newWinConditions: An WinConditions object that represent all the winConditions of this game
    
    Returns:
        The WinConditions object
    
    Raises:
        TypeError: Raise a TypeError if "newWinConditions" is not a list of WinCondition objects
    """
    if isinstance(newWinConditions, list) or newWinConditions is None:
      for wc in newWinConditions:
        if not isinstance(newWinConditions, WinCondition):
          raise TypeError('"winConditions" attribute for a Game object must be list of a WinCondition object')
      self._winConditions = newWinConditions
    else:
      raise TypeError('"winConditions" attribute for a Game object must be a list')
 
  def getHistory(self):
    """
    Get the History objects
    
    Args:
        self: the Game object
    
    Returns:
        the History object
    
    Raises:
        None
    """ 
    return self._history

  def setHistory(self,newHistory):
    """
    Set the History object of the current game 
    
    Args:
        self: the Game object
        newHistory: An History object that represent all the history of this game
    
    Returns:
        The History object
    
    Raises:
        TypeError: Raise a TypeError if "newHistory" is not a History object
    """
    if isinstance(newHistory, History) or newHistory is None:
      self._history = newHistory
    else:
      raise TypeError('"history" attribute for a Game object must be a History object')
 
 
