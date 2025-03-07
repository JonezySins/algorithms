import os
import sys
from typing import List

"""
FIBONACCI SEQUENCE

Description: Print the Fibonacci Sequence on the command
line iterating until a number you specify.

Usage: ITERATIONS=20 venv/bin/python fibonnaci_sequence.py
"""


ITERATIONS = int(os.getenv('ITERATIONS', 20))


def generate_fibonacci_sequence() -> List[int]:
    _validate_iterations()
    print(f'The Fibonacci Sequence to {ITERATIONS} iterations:')
    fibonacci_sequence = _iterate_fibonacci_sequence()

    return fibonacci_sequence


def _validate_iterations():
    """Check if the first parameter exceeds the max iterations allowed."""
    if ITERATIONS >= 94:
        sys.exit(
            'This tool can only print up to 93 iterations before the'
            ' Fibonacci number exceeds the max value allowed.'
            ' Please select a lower number and try again.'
        )
    if ITERATIONS < 1:
        sys.exit('ITERATIONS must be greater than or equal to 1.')


def _iterate_fibonacci_sequence() -> List[int]:
    """Iterate through the Fibonacci Sequence to the desired iteration."""
    new_number = 0
    this_number = 1
    previous_number = 0
    final_list = []
    counter = 1
    while counter < ITERATIONS:
        new_number = previous_number + this_number
        this_number = previous_number
        previous_number = new_number
        final_list.append(new_number)
        counter += 1
    print(final_list)

    return final_list


def main():
    generate_fibonacci_sequence()


if __name__ == '__main__':
    main()
