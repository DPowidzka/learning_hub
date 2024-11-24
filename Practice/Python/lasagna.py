"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    This function takes the actual minutes the lasagna has been in the oven
    as an argument and returns how many minutes the lasagna still needs to
    bake based on the `EXPECTED_BAKE_TIME`.

    Args:
        elapsed_bake_time: Baking time already elapsed.

    Returns:
        Remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate time needed to prepare lasagna.

    This function takes the number of layers tou want to add to the lasagna
    and calculates preparation time assuming each layer needs 2 minutes to
    prepare.

    Args:
        number_of_layers: The number of layers added to the lasagna.

    Returns:
        Preparation time in minutes.
    """

    return 2 * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate total number of minutes spent on cooking.

    This function takes the number of layers in the lasagna and the actual
    minutes the lasagna has been in the oven as an argument, and returns how
    many minutes you have spent on cooking.

    Args:
        number_of_layers: The number of layers added to the lasagna.
        elapsed_bake_time: Baking time already elapsed.

    Returns:
        The sum of preparation time and the time the lasagna has already spent
        baking in the oven
    """

    return 2 * number_of_layers + elapsed_bake_time
