from rover.obstacles import Obstacle


class TestObstacle:
    def test_obstacle_init(self):
        rock = Obstacle(x=5, y=7)
        assert rock.x == 5
        assert rock.y == 7