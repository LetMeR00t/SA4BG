## IMPORTS ##

## CLASSES ##
class Board():
  """
  Define an abstract Board class
  """

  def __init__(self, squares=[]):
    """
    Default constructor that instanciates a Board class
    
    Args:
        squares: A list of Square objects that represents the Board object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError : Raise a TypeError if name is not a string or value is not 
        an integer
    """
    if isinstance(squares, list):
      for o in squares:
        if not isinstance(o, Square):
          raise TypeError('"squares" list attribute for a Board object must contains "Square" objects')
      self._squares =  squares
    else:
      raise TypeError('"squares" attribute for a Board object must be a list')

  def getSquares(self):
    """
    Get the squares of the Board object
    
    Args:
        self: the object
    
    Returns:
        A list that represents all the squares
    
    Raises:
        None
    """
    return self._squares

class Square():
  """
  Define a Square class
  """

  def __init__(self, name="Unknown", value="Unknown"):
    """
    Default constructor that instanciates a Square class
    
    Args:
        name: A string that represents the name of the square
        value: A string that represents the value of the square
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError : Raise a TypeError if name is not a string or value is not 
        an integer
    """
    if isinstance(name, str):
      self._name =  name
    else:
      raise TypeError('"name" attribute for a Square object must be a string')
    if isinstance(value, str):
      self._value =  value
    else:
      raise TypeError('"value" attribute for a Square object must be a string')

  def getName(self):
    """
    Get the name of the Square object
    
    Args:
        self: the object
    
    Returns:
        A string that represents the name of the Square object
    
    Raises:
        None
    """
    return self._name

  def getValue(self):
    """
    Get the value of the Square object
    
    Args:
        self: the object
    
    Returns:
        A string that represents the value of the Square object
    
    Raises:
        None
    """
    return self._value
