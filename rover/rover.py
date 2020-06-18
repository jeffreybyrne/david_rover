class Rover:

    DIRECTIONS = {
        0: 'N',
        1: 'E',
        2: 'S',
        3: 'W',
    }

    def __init__(self, start_x, start_y, start_bearing, obstacles={}):
        self.x = start_x
        self.y = start_y
        self.bearing = start_bearing
        self.obstacles = obstacles

    def state_position(self):
        return f"Rover is at position ({self.x}, {self.y}) and facing {self.DIRECTIONS[self.bearing]}"

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def move(self):
        if self.bearing == 0:
            potential_position = f"{self.x},{self.y + 1}"
            if self.move_obstructed(potential_position):
                print(f"There is an obstacle at {potential_position}")
            else:
                self.y += 1
        elif self.bearing == 1:
            potential_position = (self.x + 1, self.y)
            if self.move_obstructed(potential_position):
                print(f"There is an obstacle at {potential_position}")
            else:
                self.x += 1
        elif self.bearing == 2:
            potential_position = (self.x, self.y - 1)
            if self.move_obstructed(potential_position):
                print(f"There is an obstacle at {potential_position}")
            else:
                self.y -= 1
        elif self.bearing == 3:
            potential_position = (self.x -1 , self.y)
            if self.move_obstructed(potential_position):
                print(f"There is an obstacle at {potential_position}")
            else:
                self.x -= 1

    def add_obstacle(self, obstacle):
        key = f"{obstacle.x},{obstacle.y}"
        value = (obstacle.x, obstacle.y)
        self.obstacles[key] = value

    def move_obstructed(self, potential_position):
        if self.obstacles.get(potential_position, None) is not None:
            return True


# {
#     "1,2": (1,2)
# }