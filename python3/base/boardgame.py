## IMPORTS ##
from game import Game
from player import Player

## CLASS ##
class BoardGame():
  """
  Define a BoardGame class
  """

  def __init__(self, game=None, players=[]):
    """
    Default constructor that instanciates a BoardGame class
    
    Args:
        game: A Game object that represents the current game
        players: A list of Player objects that represents all players
    
    Returns:
        The new object that was instanciated
    
    Raises:
        TypeError: Raise a TypeError if "name" is not a string
    """
    if isinstance(game, Game):
      self._game =  game
    else:
      raise TypeError('"game" attribute for a BoardGame object must be a Game object')
    if isinstance(players, list):
      for p in players:
        if isinstance(p, Player):
          raise TypeError('Each object of the "players" attribute must be a Player object')
      self._players = player
    else:
      raise TypeError('"players" attribute for a WinCondition object must be a list')

  def __str__(self):
    """
    Define the string representation of a BoardGame object
    
    Args:
        self: the BoardGame object
    
    Returns:
        A string that represents the BoardGame object
    
    Raises:
        None
    """
    return "BoardGame:\n\""+str(self._game)+"\"\n\""+str(self._players)+"\""

  def play(self):
    """
    Play a complete game (initiate, start the game and end when a win condition happens)
    
    Args:
        self: the BoardGame object
    
    Returns:
        None
    
    Raises:
        None
    """
    end = False
    i = 0
    numberOfPlayers = len(self._players)

    # Initialize the game
    self._game.prepare()

    # Play the game while no win condition happens
    while (end == False):
      # Play a turn for a player
      self._game.playTurnForPlayer(self._players[i%numberOfPlayers])
      i += 1
      # Check the win conditions
      for wc in self._game.getWinConditions():
        if wc.checkCondition(self):
          self._game.addVictoryCondition(wc)
          end = True
      if (end == False and i%numberOfPlayers == 0):
        self._game.increaseNumberOfRounds()


  def getPlayers(self):
    """
    Get the players of the game
    
    Args:
        self: the BoardGame object
    
    Returns:
        A list of Player objects
    
    Raises:
        None
    """
    return self._players
