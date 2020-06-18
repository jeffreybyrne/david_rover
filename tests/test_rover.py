from rover.obstacles import Obstacle
from rover.rover import Rover


class TestRover:
    def assert_position(self, rover, x, y, bearing):
        assert rover.x == x
        assert rover.y == y
        assert rover.bearing == bearing
        # assert rover.state_position() == f"Rover is at position ({x}, {y}) and facing {rover.DIRECTIONS[self.bearing]}"

    def test_rover_init(self):
        test_rover = Rover(start_x=5, start_y=4, start_bearing= 0)
        self.assert_position(rover=test_rover, x=5, y=4, bearing=0)

    def test_turn_left(self, test_rover):
        self.assert_position(test_rover, 0, 0, 0)
        assert test_rover.bearing == 0
        assert test_rover.state_position() == "Rover is at position (0, 0) and facing N"
        test_rover.turn_left()
        assert test_rover.bearing == 3
        assert test_rover.state_position() == "Rover is at position (0, 0) and facing W"

    def test_turn_right(self, test_rover):
        assert test_rover.bearing == 0
        assert test_rover.state_position() == "Rover is at position (0, 0) and facing N"
        test_rover.turn_right()
        assert test_rover.bearing == 1
        assert test_rover.state_position() == "Rover is at position (0, 0) and facing E"

    def test_move(self, test_rover):
        assert test_rover.y == 0
        assert test_rover.state_position() == "Rover is at position (0, 0) and facing N"
        test_rover.move()
        assert test_rover.y == 1
        assert test_rover.state_position() == "Rover is at position (0, 1) and facing N"
        test_rover.move()
        test_rover.move()
        assert test_rover.y == 3
        assert test_rover.state_position() == "Rover is at position (0, 3) and facing N"

    def test_turn_and_move(self, test_rover):
        assert test_rover.y == 0
        assert test_rover.state_position() == "Rover is at position (0, 0) and facing N"

    # def test_move_rejected_if_obstructed(self, test_rover):
    #     rock = Obstacle(x=0, y=1)
    #     test_rover.obstacles = [rock]
    #     self.assert_position(rover=test_rover, x=0, y=0, bearing=0)
    #     test_rover.move()
    #     self.assert_position(rover=test_rover, x=0, y=0, bearing=0)

    def test_add_obstacle(self, test_rover):
        rock = Obstacle(3,4)
        test_rover.add_obstacle(rock)
        assert test_rover.obstacles.get("3,4") is not None
