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
        point_left_down = Point(x, y)
        point_left_up = Point(x, y + high)
        point_right_up = Point(x + width, y + high)
        point_right_down = Point(x + width, y)
        self.coord_list = [point_left_down, point_left_up, point_right_up, point_right_down]
    def move(self, distance, direction):
        for i in self.coord_list:
            i.move(distance, direction)
    def current_coord(self):
        new_list = []
        for i in self.coord_list:
            new_list.appened(i)
        new_list = tuple(new_list)
        return new_list
    
        
            
            
        
 
    

