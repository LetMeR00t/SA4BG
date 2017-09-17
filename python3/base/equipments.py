## IMPORTS ##
from base.equipment.dice import Dice
from base.equipment.card import Card
from base.equipment.board import Board

## CLASS ##
class Equipments():
  """
  Define an Equipments class
  """

  def __init__(self, cards=[], dices=[], board=None):
    """
    Default constructor that instanciates an Equipments class
    
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
          raise TypeError('"cards" attribute for an Equipments object must be a list of Card objects')
      self._cards = cards
    else:
      raise TypeError('"cards" attribute for an Equipments object must be a list')
    if isinstance(dices, list):
      for d in dices:
        if not isinstance(d, Dice):
          raise TypeError('"dices" attribute for an Equipments object must be a list of Dice objects')
      self._dices = dices
    else:
      raise TypeError('"dices" attribute for an Equipments object must be a list')
    if isinstance(board, Board) or board is None:
      self._board = board
    else:
      raise TypeError('"board" attribute for an Equipments object must be a Board object')

  def __str__(self):
    """
    Define the string represention of an Equipments object
    
    Args:
        self: the Equipments object
    
    Returns:
        A string that represents the Equipments object
    
    Raises:
        None
    """
    return "Equipments: \"Cards -> "+str(self._cards)+"\", \"Dices -> "+str(self._dices)+"\", \"Board -> "+str(self._board)+"\""

  def getCards(self):
    """
    Get the cards 
    
    Args:
        self: the Equipments object
    
    Returns:
        A list that contains all Card objects
    
    Raises:
        None
    """
    return self._cards

  def addCard(self, card):
    """
    Add a new card in the list of cards 
    
    Args:
        self: the Equipments object
        card: the new Card object to add
    
    Returns:
        None
    
    Raises:
        TypeError: Raise a TypeError if "card" is not a Card object

    """
    if isinstance(card, Card):
      self._cards.append(card)
    else:
      raise TypeError('"card" parameter must be a Card object')

  def getDices(self):
    """
    Get the dices 
    
    Args:
        self: the Equipments object
    
    Returns:
        A list that contains all Dice objects
    
    Raises:
        None
    """
    return self._dices

  def addDice(self, dice):
    """
    Add a new dice in the list of dices 
    
    Args:
        self: the Equipments object
        dice: the new Dice object to add
    
    Returns:
        None
    
    Raises:
        TypeError: Raise a TypeError if "dice" is not a Dice object

    """
    if isinstance(dice, Dice):
      self._dices.append(dice)
    else:
      raise TypeError('"dice" parameter must be a Dice object')

  def getBoard(self):
    """
    Get the board 
    
    Args:
        self: the Equipments object
    
    Returns:
        the Board object
    
    Raises:
        None
    """
    return self._board
