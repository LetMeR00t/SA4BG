## IMPORTS ##

## CLASS ##
class Card():
  """
  Define a Card class
  """

  def __init__(self, name="Unknown", value=0):
    """
    Default constructor that instanciates a Card class
    
    Args:
        name: A string that represents the name of the new Card
        value: An integer that represents the value of the new Card
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string or "value" is not 
        an integer
    """
    if isinstance(name, str):
      self._name =  name
    else:
      raise TypeError('"name" attribute for a Card object must be a string')
    if isinstance(value, int):
      self._value =  value
    else:
      raise TypeError('"value" attribute for a Card object must be an integer')

  def getName(self):
    """
    Get the name of the Card object
    
    Args:
        self: the object
    
    Returns:
        A string that represents the name of this Card
    
    Raises:
        None
    """
    return self._name

  def getValue(self):
    """
    Get the value of the Card object
    
    Args:
        self: the object
    
    Returns:
        An integer that represents the value of this Card
    
    Raises:
        None
    """
    return self._value
