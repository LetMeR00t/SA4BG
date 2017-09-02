## IMPORTS ##

## CLASS ##
class Win_Condition():
  """
  Define a Win_Condition class
  """

  def __init__(self, name="Unamed"):
    """
    Default constructor that instanciates a Win_Condition class
    
    Args:
        name: A string that represents the Win_Condition object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(name, str):
      self._name =  name
    else:
      raise TypeError('"name" attribute for a Win_Condition object must be a string')

  def __str__(self):
    """
    Define the string represention of a Win_Condition object
    
    Args:
        self: the Win_Condition object
    
    Returns:
        A string that represents the Win_Condition object
    
    Raises:
        None
    """
    return "Win_Condition \""+self._name+"\""
