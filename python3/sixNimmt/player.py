## IMPORTS ##
from base.player import Player
from sixNimmt.playerEquipments import SixNimmtPlayerEquipments

## CLASS ##
class SixNimmtPlayer(Player):
  """
  Define a SixNimmtPlayer class
  """

  def __init__(self, name="Unamed", equipments=SixNimmtPlayerEquipments()):
    """
    Default constructor that instanciates a Player class
    
    Args:
        name: A string that represents the Player object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    super().__init__(name, equipments)

