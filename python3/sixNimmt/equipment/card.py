## IMPORTS ##
from base.equipment.card import Card

## CLASS ##
class SixNimmtCard(Card):
  """
  Define a SixNimmtCard class
  """

  def __init__(self, number=-1, bullHeadsNumber=0):
    """
    Default constructor that instanciates a SixNimmtCard class
    
    Args:
        number: This is the number specified on the card and used for order cards during the game
        bullHeadsNumber: This is the number of bull heads based on the number, it will be used for the score at the end of each turn
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string or "value" is not 
        an integer
    """
    if not isinstance(number, int):
      raise TypeError('"number" attribute for a SixNimmtCard object must be an integer')
    if not isinstance(bullHeadsNumber, int):
      raise TypeError('"bullHeadsNumber" attribute for a SixNimmtCard object must be an integer')
    super().__init__(str(number),bullHeadsNumber)

  def getNumber(self):
    """
    Get the number of the SixNimmtCard object
    
    Args:
        self: the object
    
    Returns:
        An integer that represents the number of this Card
    
    Raises:
        None
    """
    return int(self.getName())

  def getBullHeadsNumber(self):
    """
    Get the number of bull heads of the SixNimmtCard object
    
    Args:
        self: the object
    
    Returns:
        An integer that represents the number of bull heads of this Card
    
    Raises:
        None
    """
    return self.getValue()

  def __str__(self):
    """
    Define the string represention of a SixNimmtCard object
    
    Args:
        self: the SixNimmtCard object
    
    Returns:
        A string that represents the SixNimmtCard object
    
    Raises:
        None
    """
    return "SixNimmtCard -> Number: "+str(self.getNumber())+", Bull heads number: "+str(self.getBullHeadsNumber())

