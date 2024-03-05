import pytest

from program import program

test_cases = [
  pytest.param()
]

@pytest.mark.parametrize('arguments,expected_output,fail_message',test_cases)
def test_template(arguments, expected_output, fail_message):
  actual = program()
  assert actual == expected_output, fail_message
