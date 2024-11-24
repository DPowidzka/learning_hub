from Powidzka_Dominika_lasagna import elapsed_time_in_minutes
import numpy as np


EXPECTED_BAKE_TIME = 40
NUMBER_OF_LAYERS = 3


def test_elapsed_time_in_minutes_list():
    """Test elapsed_time_in_minutes using predefined list of bake times.

    This function uses a list of elapsed bake times and for each bake time and
    constant NUMBER_OF_LAYERS, it prints the result of cooking_time to the
    console.
    """

    elapsed_bake_times = [5, 8, 13, 24, 32]
    for time in elapsed_bake_times:
        cooking_time = elapsed_time_in_minutes(NUMBER_OF_LAYERS, time)
        print(f'Elapsed cooking time {cooking_time}') 


def test_elapsed_time_in_minutes_range():
    """Test elapsed_time_in_minutes using a range of bake times.

    This function generates a range of elapsed_bake_times and stores 
    cooking_times values for each bake time and constant NUMBER_OF_LAYERS in
    a list, printing the result to the console.
    """

    elapsed_bake_times = range(2, 10, 2)
    cooking_times = [elapsed_time_in_minutes(NUMBER_OF_LAYERS, time) for time in elapsed_bake_times]
    print(f'Elapsed cooking times: {cooking_times}')


def test_elapsed_time_in_minutes_linspace():
    """Test elapsed_time_in_minutes using an array of bake times generated
    by numpy.

    The function uses numpy's linspace method to generate an array of bake
    times. It stores results in dictionary where key is elapsed_bake_time and
    the value is elapsed_time_in_minutes. The result is printed to the console.
    """

    elapsed_bake_times = np.linspace(5, 15, 10) 
    results = {round(time): elapsed_time_in_minutes(NUMBER_OF_LAYERS, int(time)) for time in elapsed_bake_times}    # linspace returns floats. Round and convert to avoid floating point
    print(f'{results}')


def combinations_of_layers_and_bake_times():
    """Generate combinations of number of layers and bake times.

    This function generates all combinations of number of layers
    (from predefined list) and elapsed bake times (generated as a numpy's
    array of evenly spaced values between 5 and 15 minutes). It iterates
    through all the combinations, and stores the result in nested dictionary
    where key for outer dictionary is number of iteration and keys for inner
    dictionary are number_of_layers, elapsed_bake_time, elapsed_time_in_minutes.
    It prints the result to the console.
    """

    result = {}
    number_of_layers_list = [3, 4, 5, 6, 7, 8]
    elapsed_bake_times = np.linspace(5, 15, 10)
    iteration = 1   # counter for iteration

    for layer in number_of_layers_list:
        for time in elapsed_bake_times:
            result[f'iteration_{iteration}'] = {'number_of_layers': layer,
                                                'elapsed_bake_time': int(time),
                                                'elapsed_time_in_minutes': elapsed_time_in_minutes(layer, int(time))
                                                }
            iteration += 1  # increment for next iteration

    print(result)


def main():
    """Main function to run all test cases.

    This function calls all test functions to control the
    elapsed_time_in_minutes() with different inputs.
    """
    test_elapsed_time_in_minutes_list()
    test_elapsed_time_in_minutes_range()
    test_elapsed_time_in_minutes_linspace()
    combinations_of_layers_and_bake_times()


if __name__ == '__main__':
    main()