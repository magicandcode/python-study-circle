from typing import Any, Callable, Dict, List, Optional
import random


# Seed to make our randomness more predictable during development.
random.seed(42)


def get_words(word_count: Optional[int] = None,
              filename: str = './words.txt') -> List[str]:
    """Return list with unique upper case words from text file.
    
    Number of words can be less but never greater than word_count. 
    """
    try:
        # Open file in reading mode to read each line and save as a list.
        with open(filename, 'r') as f:
            words = f.readlines()
        
        # Each word ends with a newline character (\n) and could be in any case. 
        #   To normalise the words we remove trailing whitespace and convert to
        #   upper case.  Normally one would choose lowercase but we want the
        #   answer in upper case anyway for a prettier output.
        normalised_words = [word.strip().upper() for word in words]
        
        # Remove duplicate words.
        normalised_words = list(set(normalised_words))

        # Randomise words before slicing.
        random.shuffle(normalised_words)
        
        # If word_count is not set, return all words.
        if word_count is None:
            return sorted(normalised_words)

        # Sort after slicing; we want randomised words in our slice.
        return sorted(normalised_words[:word_count])
    except FileNotFoundError:
        raise ValueError(f'Invalid file path: {filename}')


def get_game_solution(words: List[str]):
    """Get random word from list of words to use as game solution.
    
    Remove word from list to ensure that each solution is unique
      during a game session.
    """
    solution = random.choice(words)
    
    # Remove any duplicates of solution.
    while solution in words:
        words.remove(solution)

    return solution


def guess_is_valid(guess: str) -> bool:
    """Checks if guess is valid.
    
    Not the same as guess being correct.
    A guess can be a lower or upper case string with a letter A-Za-z.
    Normalise guess by converting to lower case and check if its ASCII
      number is in the range of 97-122 (a-z).
    Any string with more than one character will throw an exception
      that is caught and returns False.
    """
    try:
        return 97 <= ord(guess.lower()) <= 122
    except (AttributeError, TypeError):
        return False


def get_valid_guess() -> str:
    """Get valid guess, reprompting player until guess is valid.

    Note that validity is not same as guess being correct and present
      in the solution string.
    """
    guess: str = input('Guess a letter A-Z: ').upper()
    if not guess_is_valid(guess):
        print(f'Invalid guess: {guess}, please try again.')
        guess = get_valid_guess()
    return guess


def guess_is_correct(guess: str, solution: str) -> bool:
    """Check if guess is in solution string."""
    return guess.upper() in solution.upper()


def player_wins(result: str, solution: str) -> bool:
    """Check if player wins by comparing result with solution."""
    return result == solution


def player_loses(guess_count: int, max_guess_count: int = 5) -> bool:
    """Check if player loses; the number of incorrect guesses is
      greater than the max number allowed guesses.
    """
    return guess_count > max_guess_count


def play(game: Callable[[Any], None], *args, **kwargs):
    """Start new game session and loop game until user quits.
    
    As long as the game session is running, each new solution is removed from
      the list of words and reset if words is empty.  This ensures that the user
      gets non-repeated solutions as far as possible.
    """
    # Get initial list of words from which to pick game solutions.
    words: List[str] = get_words()
    
    game_count: int = 1

    # Start game session.
    print("Get ready to play Hangman's Game!")
    while True:  # Warning, infinte loop!
        
        # Reset words if each words has been selected as solution at least once.
        if not words:
            print('\nGenerating new words...\n')  # Debugging only
            words = get_words()

        # Start new game.
        game(*args, words=words, game_count=game_count, **kwargs)

        # Ask user if they want to play again or quit.
        play_again: bool = input('Do you want to play again? Y/n ').lower()

        # Start another game if user answers yes.
        if play_again in ('y', 'yes'):
            game_count += 1
            continue

        # Else quit the game session by breaking out of the loop and returning to
        #   the console prompt.
        print("\nThank's for playing, bye!")
        break


# Set initial game state.
initial_game_state: Dict[str, Any] = {
    'words': [],
    'answer': '',
    'max_attempts': 5,
    'remaining_attempts': 5,
    'result': '',
    'win': None,
    'loss': None,  
}


if __name__ == '__main__':
    pass
