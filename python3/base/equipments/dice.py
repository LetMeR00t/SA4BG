## IMPORTS ##
import random

## CLASS ##
class Dice():
  """
  Define a Dice class
  """

  def __init__(self, values=['1','2','3','4','5','6']):
    """
    Default constructor that instanciates a Dice class
    
    Args:
        values: A list that define each possible value for the new Dice
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "values" is not a list
    """
    if isinstance(values, list):
      self._values =  values
    else:
      raise TypeError('"values" attribute for a Dice object must be a list')

  def throwTheDice(self):
    """
    Throw the dice and give the result
    
    Args:
        self: the object
    
    Returns:
        A string that represents the result
    
    Raises:
        None
    """
    return self._values[random.randint(0,len(self._values)-1)]
