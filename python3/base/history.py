## IMPORTS ##
from abc import ABCMeta, abstractmethod

## CLASS ##
class History(metaclass=ABCMeta):
  """
  Define a History class
  """

  def __init__(self):
    """
    Default constructor that instanciates a History class
    
    Args:
        None
    
    Returns:
        The new object that was instanciated
    
    Raises:
        None
    """
    self._entries = []

  def __str__(self):
    """
    Define the string representation of a History object
    
    Args:
        self: the History object
    
    Returns:
        A string that represents the History object
    
    Raises:
        None
    """
    return "History:\n \""+str(self._entries)+"\""

  @abstractmethod
  def addEntry(self, Game, Player):
    """
    Add an entry in the history
    
    Args:
        self: the History object
    
    Returns:
        None
    
    Raises:
        None
    """
    pass

  def getEntry(self, i):
    """
    Get an entry from the history
    
    Args:
        self: the History object
        i: the number for the entry
    
    Returns:
        the concerned entry
    
    Raises:
        None
    """
    return self._entries[i]
