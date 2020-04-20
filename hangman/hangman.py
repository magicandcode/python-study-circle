from typing import List, Optional
import random

from game_helpers import (get_words,
                          get_game_solution,
                          get_valid_guess,
                          play,
                          player_wins,
                         )


# Seed to make our randomness consistent during development.
random.seed(42)


def game(words: List[str], game_count: int):
    """Start a new Hangman's game.  Take list of words and get a
      solution to match against player's guesses.  Each time a new
      solution is saved, it is removed from words to avoid duplicate
      solutions within the same game session.
    
    Player wins by guessing the solution in less than 5 incorrect
       guesses. If the player makes 5 incorrect guesses without winning
       they lose.
    The game ends when the player wins or loses.
    When game is run in the play function, player can chose to play a
      new game within the same session, keeping the current value of
      words.
    """
    # Print initial game message.
    print(f'\nStarting Game #{game_count}')

    # Initial game settings.
    MAX_GUESS_COUNT: int = 5
    guess_count: int = 0

    # Get a solution to match player's guesses against.
    solution: str = get_game_solution(words)

    # Initial result will be a string with n _ where n is the length
    #   of the solution string.
    # To enable replacing _ with guess when correct, we create a list
    #   with n number of _
    # ['_', '_', '_', '_', '_']
    result_chars: List[str] = ['_' for _ in solution]
    
    # The list can then be joined to create our result string which is
    #   compared to the solution to check if player wins.
    # '_____'
    # '_PP__' == 'APPLE'  # False
    # 'APPLE' == 'APPLE'  # True
    result: str = ''.join(result_chars)


    # Loop game until player wins or loses.
    # We exit the loop when the player wins, or when the number of
    #   (incorrect) guesses is greater than the max number of guesses.
    # Alternatively, we can run the game loop infintely as long as we
    #   break out of it when the player wins or loses.
    # We can also set guess_count to 5 and decrement with each
    #   incorrect guess.  That gives us the more explicit expression:
    #       while guesses_remaining:
    # Once guesses_remaining equals 0 the expression is False and we
    #   exit the loop.
    while guess_count <= MAX_GUESS_COUNT:
      # Ask user to guess a letter.  Validate guess.  Reprompt player
      #   until guess is valid.
      guess: str = get_valid_guess()

      # Check if guess is a character in the solution.
      if guess in solution:
        # If guess is correct, replace empty slots with correct guess in
        #   result and result_chars and display message.
        print("correct")

      else:
        # If guess is wrong, increment guess_count and display message.
        guess_count += 1
        print("incorrect")

      # Has player won or lost?

    # Break out of game loop if player wins or loses.


if __name__ == '__main__':
  play(game)
