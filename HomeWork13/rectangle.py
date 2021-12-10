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
class Rectangle(Point):
    def rect(self, high, width):
        self.high = high
        self.width = width
        self.point_first = self.x, self.y
        self.point_second = self.x + width, self.y
        self.point_third = self.x + width, self.y + high
        self.point_fourth = self.x, self.y + high
    def m(self, point_first, point_second, point_third, point_fourth):
        self.point_first = point_first.move
        self.point_second = point_second.move
        self.point_third = point_third.move
        self.point_fourth = point_fourth.move
    def current_coord(self):
        return (self.point_first, self.point_second, self.point_third, self.point_fourth)



