## IMPORTS ##
from abc import ABCMeta, abstractmethod

## CLASS ##
class WinCondition(metaclass=ABCMeta):
  """
  Define a Win_Condition class
  """

  def __init__(self, name="Unamed"):
    """
    Default constructor that instanciates a Win_Condition class
    
    Args:
        name: A string that represents the Win_Condition object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(name, str):
      self._name =  name
    else:
      raise TypeError('"name" attribute for a Win_Condition object must be a string')

  def getName(self):
    """
    Get the name of the WinCondition object
    
    Args:
        self: the WinCondition object
    
    Returns:
        A string that represents the name
    
    Raises:
        None
    """
    return self._name

  def setName(self,newName):
    """
    Set the name of the WinCondition object
    
    Args:
        self: the WinCondition object
        newName: A string that represents the name
    
    Returns:
        None
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(newName, str):
      self._name = newName
    else:
      raise TypeError('"name" attribute for a WinCondition object must be a string')

  def __str__(self):
    """
    Define the string represention of a Win_Condition object
    
    Args:
        self: the Win_Condition object
    
    Returns:
        A string that represents the Win_Condition object
    
    Raises:
        None
    """
    return "Win_Condition \""+self._name+"\""

  @abstractmethod
  def checkCondition(self, game):
    """
    Abstract method that details when the win condition is True
    
    Args:
        self: the Win_Condition object
        game: the Game object that represents the game
    
    Returns:
        None
    
    Raises:
        None
    """
    pass
