class Building:
    def __init__(self):
        self.rooms = {
            'a': 'safe', 'b': 'safe', 'c': 'fire',
            'd': 'safe', 'e': 'fire', 'f': 'safe',
            'g': 'safe', 'h': 'safe', 'j': 'fire'
        }

    def status(self, room):
        return self.rooms[room]

    def put_out_fire(self, room):
        if self.rooms[room] == 'fire':
            self.rooms[room] = 'safe'

    def show(self, robot_position=None):
        symbols = {'safe': 'S', 'fire': 'F'}
        layout = [['a','b','c'], ['d','e','f'], ['g','h','j']]
        for row in layout:
            row_display = ""
            for room in row:
                if robot_position == room:
                    row_display += "R"
                else:
                    row_display += symbols[self.rooms[room]]
                row_display += " "
            print(row_display)
            print()


class FireRobot:
    def __init__(self, route):
        self.route = route
        self.current = route[0]

    def move_and_extinguish(self, building):
        for room in self.route:
            self.current = room
            print(f"Robot moving to room '{room}'...")
            if building.status(room) == 'fire':
                print(f"F: Fire detected in room '{room}'! Extinguishing...")
                building.put_out_fire(room)
                print(f"S: Fire in room '{room}' extinguished.")
            else:
                print(f"Room '{room}' is safe. Moving on.")
            building.show(robot_position=self.current)

        print("All rooms have been visited.")
        print("Final building status:")
        building.show()


route = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
building = Building()
robot = FireRobot(route)
robot.move_and_extinguish(building)
