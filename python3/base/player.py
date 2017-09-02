## IMPORTS ##

## CLASS ##
class Player():
  """
  Define a Player class
  """

  def __init__(self, name="Unamed"):
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
    return "Player \""+self._name+"\""
