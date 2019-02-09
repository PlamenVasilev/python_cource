import math


class Point:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    @staticmethod
    def calculate_distance(point_a, point_b):
        side_x = abs(point_a.get_x() - point_b.get_x())
        side_y = abs(point_a.get_y() - point_b.get_y())
        side_z = math.sqrt(pow(side_x, 2) + side_y ** 2)
        return side_z


class Box:
    __upper_left: Point
    __upper_right: Point
    __bottom_left: Point
    __bottom_right: Point

    def __init__(self, ul:Point, ur:Point, bl:Point, br:Point):
        self.__upper_left = ul
        self.__upper_right = ur
        self.__bottom_left = bl
        self.__bottom_right = br

    def get_width(self):
        return Point.calculate_distance(self.__upper_left, self.__upper_right)

    def get_height(self):
        return Point.calculate_distance(self.__upper_left, self.__bottom_left)

    def calculate_perimeter(self):
        return 2 * self.get_width() + 2 * self.get_height()

    def calculate_area(self):
        return self.get_width() * self.get_height()

    def __str__(self):
        return f"Box: {self.get_width():g}, {self.get_height():g}\n" \
            f"Perimeter: {self.calculate_perimeter():g}\n" \
            f"Area: {self.calculate_area():g}"


boxes = []
while True:
    data = input()
    if data == 'end':
        for box in boxes:
            print(box)
        break
    ul, ur, bl, br = data.split(' | ')
    ulp = ul.split(':')
    urp = ur.split(':')
    blp = bl.split(':')
    brp = br.split(':')
    boxes.append(Box(Point(ulp[0], ulp[1]), Point(urp[0], urp[1]), Point(blp[0], blp[1]), Point(brp[0], brp[1])))


