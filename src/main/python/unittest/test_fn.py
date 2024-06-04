import sys
import os
import pytest
sys.path.append(os.getcwd())
from unittest.mock import patch
from src.main.python.strategy.testSum import weightingSum


# define the test case
tasks = [(1, 2, 3), (0, 0, 2)]
# mock the sequence task
@pytest.mark.parametrize("input1, input2, ans", tasks)
# mock function
@patch('src.main.python.strategy.testSum.weight2', return_value=2)
def test_mock_functions(mock_weight2, input1, input2, ans):
    result = weightingSum(input1, input2)
    assert result == ans

