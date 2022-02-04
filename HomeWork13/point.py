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




