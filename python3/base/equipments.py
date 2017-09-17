## IMPORTS ##
from base.equipment.dice import Dice
from base.equipment.card import Card
from base.equipment.board import Board
from random import shuffle

## CLASS ##
class Equipments():
  """
  Define an Equipments class
  """

  def __init__(self, cards=[[]], dices=[], board=None):
    """
    Default constructor that instanciates an Equipments class
    
    Args:
        cards: A list of Card objects list, we can have multiple type of cards in different stacks
        dices: A list of Dice objects
        board: A Board object
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "cards" or "dices" is not a list (respectively of Card objects and Dice objects) or if "board" is not a Board object
    """
    if isinstance(cards, list):
      for l in cards:
        if isinstance(l, list):
          for c in l:
            if not isinstance(c, Card):
              raise TypeError('"cards" attribute for an Equipments object must be a list of Card objects list')
        else:
          raise TypeError('"cards" attribute for an Equipments object must be a list of Card objects list')
      self._cards = cards
    else:
      raise TypeError('"cards" attribute for an Equipments object must be a list')
    if isinstance(dices, list) or dices is None:
      if dices is None:
        self._dices = None
      else:
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
    result = "Equipments:\nCards -> [\n"
    for l in self._cards:
      result += "\t[\n"
      for c in l:
        result += "\t\t"+str(c)+",\n"
      result += "\t]\n"
    if self._dices is not None:
      result += "], \nDices -> [\n"
      for d in self._dices:
        result += "\t"+str(d)+",\n"
    if self._board is not None:
      result += "], \nBoard -> \""+str(self._board)+"\""
    return result

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

  def addCard(self, i, card):
    """
    Add a new card in the list of cards at the index i 
    
    Args:
        self: the Equipments object
        card: the new Card object to add
        i: Integer that represents the index of the concerned list
    
    Returns:
        None
    
    Raises:
        TypeError: Raise a TypeError if "card" is not a Card object

    """
    if isinstance(card, Card):
      self._cards[i].append(card)
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

  def shuffleTheCards(self, i):
    """
    Shuffle all the cards 
        
    Args:
        self: The current object
        i: Integer that represents the index of the concerned list
    
    Returns:
        None, but cards are shuffled
    
    Raises:
        None
    """
    shuffle(self._cards[i])

  def pushCard(self, i, newCard):
    """
    Push a card to the list at index i
        
    Args:
        self: The current object
        newCard: The Card object to push
        i: Integer that represents the index of the concerned list
    
    Returns:
        None    

    Raises:
        None
    """
    if isinstance(newCard, Card):
      self._cards.push(newCard)
    else:
      raise TypeError('"newCard" attribute must be a Card object')

  def popCard(self, i):
    """
    Pop a card from the list at index i
        
    Args:
        self: The current object
        i: Integer that represents the index of the concerned list
    
    Returns:
        None    

    Raises:
        None
    """
    if i < len(self._cards):
      return self._cards[i].pop()
    else:
      return None


