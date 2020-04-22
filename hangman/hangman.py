from typing import List, Optional
import random

from game_helpers import (get_words,
                          get_game_solution,
                          get_valid_guess,
                          play,
                          player_wins,
                          guess_is_correct
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
    MAX_guesses_remaining: int = 5
    guesses_remaining: int = 5

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


    print(solution)
    # Greeet player with initial result.
    print(f"Your word:\n\n{' '.join(result)} ({len(solution)} characters)\n")

    # Loop game until player wins or loses.
    # We exit the loop when the player wins, or when the number of
    #   (incorrect) guesses is greater than the max number of guesses.
    # Alternatively, we can run the game loop infintely as long as we
    #   break out of it when the player wins or loses.
    while guesses_remaining:
      # Ask user to guess a letter.  Validate guess.  Reprompt player
      #   until guess is valid.
      guess: str = get_valid_guess()

      # Check if guess is a character in the solution.
      if guess_is_correct(guess, solution):
        # If guess is correct, replace empty slots with correct guess in
        #   result and result_chars and display message.

        for i, char in enumerate(solution):
            if char == guess:
                result_chars[i] = guess

        result = ''.join(result_chars)
        # Compare result to solution.
        if player_wins(result, solution):
            print("")
            break
        print(f'{guess} is correct!')
        print(' '.join(result_chars))

      else:
        # If guess is wrong, increment guesses_remaining and display message.
        guesses_remaining -= 1
        print("incorrect")

      # Has player won or lost?

    # Break out of game loop if player wins or loses.


if __name__ == '__main__':
  play(game)
