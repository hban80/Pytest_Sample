
# https://www.tutorialspoint.com/pytest/pytest_grouping_the_tests.htm
import pytest
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 100

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 60
   assert num < 200