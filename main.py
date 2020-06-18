from rover.obstacles import Obstacle
from rover.rover import Rover

def main():
    rover_active = True
    rock = Obstacle(x=0,y=1)
    # rock2 = Obstacle(x=1,y=0)
    # rock3 = Obstacle(x=0, y=-1)
    # rock4 = Obstacle(x=-1, y=0)
    our_rover = Rover(start_x=0, start_y=0, start_bearing=0)
    our_rover.add_obstacle(rock)
    while rover_active:
        print(our_rover.state_position())
        command = input("Enter a command")
        if command == 'L':
            our_rover.turn_left()
        elif command == 'R':
            our_rover.turn_right()
        elif command == 'F':
            our_rover.move()
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
