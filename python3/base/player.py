## IMPORTS ##
from base.equipments import Equipments

## CLASS ##
class Player():
  """
  Define a Player class
  """

  def __init__(self, name="Unamed", equipments=None):
    """
    Default constructor that instanciates a Player class
    
    Args:
        name: A string that represents the Player object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(name, str):
      self._name =  name
    else:
      raise TypeError('"name" attribute for a Player object must be a string')
    # Define a private empty Equipments object
    if isinstance(equipments, Equipments) or equipments is None:
      self._equipments = equipments
    else:
      raise TypeError('"equipments" attribute for a Player object must be a Equipments object')
    # Define a score equals to 0
    self._score = 0

  def __str__(self):
    """
    Define the string represention of a Player object
    
    Args:
        self: the Player object
    
    Returns:
        A string that represents the Player object
    
    Raises:
        None
    """
    return "Player -> Name: \""+self._name+"\", "+str(self._equipments)

  def getName(self):
    """
    Get the name of the Player object
    
    Args:
        self: the Player object
    
    Returns:
        A string that represents the name
    
    Raises:
        None
    """
    return self._name

  def getScore(self):
    """
    Get the score of the Player object
    
    Args:
        self: the Player object
    
    Returns:
        An integer that represents the score
    
    Raises:
        None
    """
    return self._score

  def setScore(self, newScore):
    """
    Set the score of the Player object
    
    Args:
        self: the Player object
        newScore: the new score to set
    
    Returns:
        None
    
    Raises:
        None
    """
    self._score = newScore

  def getEquipments(self):
    """
    Get the private Equipments object of the Player object
    
    Args:
        self: the Player object
    
    Returns:
        An Equipments object that represent all the private equipments of this player
    
    Raises:
        None
    """
    return self._equipments
