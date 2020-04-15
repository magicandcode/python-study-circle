from typing import List, Optional
import random

from game_utils import get_words, get_game_solution, play

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

    # Game settings.
    MAX_GUESS_COUNT: int = 5
    guess_count: int = 0

    # Get a solution to match player's guesses against.
    solution: str = get_game_solution(words)
    solution_chars: List[str] = []
    result_chars: List[str] = []
    result: str = ''

    # Loop game until player wins or loses.

    # Ask user to guess a letter.  Guess must be converted to upper to
    #  match against solution.
    # guess = input('Guess a letter (A-Z): ').upper()


    # Check if guess is in solution.

    # If guess is correct, replace empty slots with correct guess in
    #   result and result_chars and display message.

    # If guess is wrong, decrement guess_count and display message.

    # Has player won or lost?

    # Break out of game loop if player wins or loses.


if __name__ == '__main__':
    play(game)
