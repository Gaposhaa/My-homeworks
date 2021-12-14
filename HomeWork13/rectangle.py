class Point:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
    def move(self, distance, direction):
        if direction == "left":
            self.x -= distance
        elif direction == "right":
            self.x += distance
        elif direction == "up":
            self.y += distance
        elif direction == "down":
            self.y -= distance
        else:
            raise ValueError
    def current_coord(self):
        return (self.x, self.y)
class Rectangle:
    def rect(self, high, width, x, y):
        self.high = high
        self.width = width
        self.point_left_down = Point(x, y)
        self.point_left_up = Point(x, y + high)
        self.point_right_up = Point(x + width, y + high)
        self.point_right_down = Point(x + width, y)
        self.coord_list = [self.point_left_down, self.point_left_up, self.point_right_up, self.point_right_down]
    def move(self, distance, direction):
        for i in self.coord_list:
            i.move(distance, direction)
    def current_coord(self):
        return ((self.point_left_down), (self.point_left_up), (self.point_right_up), (self.point_left_down))
    

