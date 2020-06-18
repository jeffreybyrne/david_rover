import pytest

from rover.rover import Rover


@pytest.fixture
def test_rover():
    rover = Rover(start_x=0, start_y=0, start_bearing=0)
    return rover
