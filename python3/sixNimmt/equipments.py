## IMPORTS ##
from base.equipments import Equipments
from sixNimmt.equipment.card import SixNimmtCard

## CLASS ##
class SixNimmtEquipments(Equipments):
  """
  Define an Equipments class for the game "6 Nimmt!"
  """

  def __init__(self):
    """
    Default constructor that instanciates a SixNimmtEquipments class
    In the 6 Nimmt! game, there are 104 cards with a number and several bull heads
    
    Args:
        self: The current object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "cards" or "dices" is not a list (respectively of Card objects and Dice objects) or if "board" is not a Board object
    """
    cards = []
    value = -1
    # Initiate all cards, the name is a number and the value is the associated bull heads number
    for i in range(1,105):
      if i in [5,15,25,35,45,65,75,85,95]:
        value = 2
      elif i in [10,20,30,40,50,60,70,80,90,100]:
        value = 3
      elif i in [11,22,33,44,66,77,88,99]:
        value = 5
      elif i == 55:
        value = 7
      else:
        value = 1
      cards.append(SixNimmtCard(i,value))
    super().__init__(cards=[cards])
    # There is no board in this game, but we need a table to know what cards are played
    # We declare 4 lists that will contain the 4 columns of the game
    _table = [[],[],[],[]]

  def getTable(self):
    """
    Get the table of the current object SixNimmtEquipements
    
    Args:
        self: The current object
    
    Returns:
        The associated table that contains the 4 columns on the table
    
    Raises:
        None
    """
    return self._table
