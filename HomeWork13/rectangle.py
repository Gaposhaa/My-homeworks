class Rectangle:
    def __init__(self, x, y, high, width):
        self.x = x
        self.y = y
        self.high = high
        self.width = width
        self.Point_first = x, y
        self.Point_second = x + width, y
        self.Point_third = x, y + high
        self.Point_fourth = x + width, y + high
    def move(self, distance, direction):
        if direction == "left":
            self.Point_first = self.x -distance, self.y
            self.Point_second = self.x - distance, self.y
            self.Point_third = self.x - distance, self.y
            self.Point_fourth = (self.x + self.width) - distance, self.y
        elif direction == "right":
            self.Point_first = self.x + distance, self.y
            self.Point_second = self.x + distance, self.y
            self.Point_third = self.x + distance, self.y
            self.Point_fourth = (self.x + self.width) + distance, self.y
        elif direction == "up":
            self.Point_first = self.x, self.y + distance
            self.Point_second = self.x, self.y + distance
            self.Point_third = self.x, self.y + distance
            self.Point_fourth = self.x, (self.y + self.high) + distance
        elif direction == "down":
            self.Point_first = self.x, self.y - distance
            self.Point_second = self.x, self.y - distance
            self.Point_third = self.x, self.y - distance
            self.Point_fourth = self.x, (self.y + self.high) - distance
    def current_coord(self):
        return (self.Point_first, self.Point_second, self.Point_third, self.Point_fourth)



