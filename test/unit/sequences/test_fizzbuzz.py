from unittest.mock import patch

from algorithms.sequences.fizzbuzz import _determine_output, generate_fizzbuzz


@patch('algorithms.sequences.fizzbuzz._determine_output')
def test_fizzbuzz_run(mock_determine_output):
    generate_fizzbuzz()

    assert mock_determine_output.call_count == 15


def test_fizzbuzz_determine_output_fizz():
    output = _determine_output(3)

    assert output == 'Fizz'


def test_fizzbuzz_determine_output_buzz():
    output = _determine_output(5)

    assert output == 'Buzz'


def test_fizzbuzz_determine_output_fizzbuzz():
    output = _determine_output(15)

    assert output == 'FizzBuzz'


def test_fizzbuzz_determine_output_normal():
    output = _determine_output(1)

    assert output == '1'


@patch('algorithms.sequences.fizzbuzz.ITERATIONS', -1)
@patch('sys.exit')
def test_fibonacci_sequence_iteration_less_than_1(mock_sys_exit):
    generate_fizzbuzz()

    mock_sys_exit.assert_called_once()
