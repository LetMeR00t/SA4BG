## IMPORTS ##
from base.equipments import Equipments

## CLASS ##
class SixNimmtPlayerEquipments(Equipments):
  """
  Define a player Equipments class for the game "6 Nimmt!"
  """

  def __init__(self):
    """
    Default constructor that instanciates a SixNimmtPlayerEquipments class
    In the 6 Nimmt! game, each player has a list of cards
    
    Args:
        self: The current object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "cards" or "dices" is not a list (respectively of Card objects and Dice objects) or if "board" is not a Board object
    """
    super().__init__(dices=None)

