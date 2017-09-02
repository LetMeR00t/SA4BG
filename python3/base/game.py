## IMPORTS ##
from abc import ABCMeta

## CLASS ##
class Game(metaclass=ABCMeta):
  """
  Define a Game class
  """

  def __init__(self, name="Unamed"):
    """
    Default constructor that instanciates a Game class
    
    Args:
        name: A string that represents the Game object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(name, str):
      self._name =  name
    else:
      raise TypeError('"name" attribute for a Game object must be a string')

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
    self.init()
    self.start()

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

  @abstractmethod
  def start(self):
    """
    Abstract method that start the game
    
    Args:
        self: the Game object
    
    Returns:
        None
    
    Raises:
        None
    """
    pass
