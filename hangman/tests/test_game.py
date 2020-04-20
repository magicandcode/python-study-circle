import pytest

import game_helpers


@pytest.mark.parametrize('guess', [
    'a', 'A', 'z', 'Z'
])
def test_valid_guess(guess):
    assert game_helpers.guess_is_valid(guess) is True


@pytest.mark.parametrize('guess', [
    'Å', 'ö', '8', 'hi', '[]', '{}', '*', 11, 
])
def test_invalid_guess(guess):
    assert game_helpers.guess_is_valid(guess) is False


@pytest.mark.parametrize('guess',
                         list('apple'))
def test_correct_guess(guess):
    solution: str = 'APPLE'
    assert game_helpers.guess_is_correct(guess, solution)


@pytest.mark.parametrize('guess',
                         list('circus'))
def test_incorrect_guess(guess):
    solution: str = 'APPLE'
    assert not game_helpers.guess_is_correct(guess, solution)


def test_player_wins():
    solution: str = 'APPLE'
    assert game_helpers.player_wins(solution, solution)


def test_player_does_not_win():
    solution: str = 'APPLE'
    assert game_helpers.player_wins(solution, 'APP_E') is False


def test_player_loses():
    assert game_helpers.player_loses(6)


def test_player_has_one_guess_left():
    assert game_helpers.player_loses(5) is False
