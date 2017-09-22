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
        None
    """
    # Set the name of the player
    self.setName(name)

    # Define an empty Equipments object
    self.setEquipments(equipments)

    # Define a score equals to 0
    self.setScore(0)

  def reset(self):
    """
    Reset a player for a new game
    
    Args:
        self: the Player object
    
    Returns:
        None
    
    Raises:
        None
    """
    # Define a new empty Equipments object
    self.getEquipments().reset()

    # Define a new score equals to 0
    self.setScore(0)

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

  def setName(self,newName):
    """
    Set the name of the Player object
    
    Args:
        self: the Player object
        newName: A string that represents the name
    
    Returns:
        None
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(newName, str):
      self._name = newName
    else:
      raise TypeError('"name" attribute for a Player object must be a string')
 
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
        TypeError: Raise a TypeError if "newScore" is not an integer

    """
    if isinstance(newScore, int):
      self._score = newScore
    else:
      raise TypeError('"score" attribute for a Player object must be an integer')

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

  def setEquipments(self,newEquipments):
    """
    Set the private Equipments object of the Player object
    
    Args:
        self: the Player object
        newEquipments: An Equipments object that represent all the private equipments of this player
    
    Returns:
        None
            
    Raises:
        TypeError: Raise a TypeError if "newEquipments" is not an Equipments object
    """
    if isinstance(newEquipments, Equipments) or newEquipments is None:
      self._equipments = newEquipments
    else:
      raise TypeError('"equipments" attribute for a Player object must be a Equipments object')
 

