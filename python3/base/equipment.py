## IMPORTS ##
from equipments.dice import Dice
from equipments.card import Card
from equipments.board import Board

## CLASS ##
class Equipment():
  """
  Define an Equipment class
  """

  def __init__(self, cards=[], dices=[], board=None):
    """
    Default constructor that instanciates an Equipment class
    
    Args:
        cards: A list of Card objects
        dices: A list of Dice objects
        board: A Board object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "cards" or "dices" is not a list (respectively of Card objects and Dice objects) or if "board" is not a Board object
    """
    if isinstance(cards, list):
      for c in cards:
        if not isinstance(c, Card):
          raise TypeError('"cards" attribute for an Equipment object must be a list of Card objects')
      self._cards = cards
    else:
      raise TypeError('"cards" attribute for an Equipment object must be a list')
    if isinstance(dices, list):
      for d in dices:
        if not isinstance(d, Dice):
          raise TypeError('"dices" attribute for an Equipment object must be a list of Dice objects')
      self._dices = dices
    else:
      raise TypeError('"dices" attribute for an Equipment object must be a list')
    if isinstance(board, Board) or board is None:
      self._board = board
    else:
      raise TypeError('"board" attribute for an Equipment object must be a Board object')

  def __str__(self):
    """
    Define the string represention of an Equipment object
    
    Args:
        self: the Equipment object
    
    Returns:
        A string that represents the Equipment object
    
    Raises:
        None
    """
    return "Equipments: \"Cards -> "+str(self._cards)+"\", \"Dices -> "+str(self._dices)+"\", \"Board -> "+str(self._board)+"\""
