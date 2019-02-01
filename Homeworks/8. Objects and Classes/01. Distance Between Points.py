import math


class Point:
    __x: float
    __y: float

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def set_x(self, x):
        if not isinstance(x, float):
            raise Exception
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        if not isinstance(y, float):
            raise Exception
        self.__y = y

    def get_y(self):
        return self.__y


def get_distance(point_a: Point, point_b: Point):
    side_x = abs(point_a.get_x() - point_b.get_x())
    side_y = abs(point_a.get_y() - point_b.get_y())
    side_z = math.sqrt(pow(side_x, 2) + side_y ** 2)
    return side_z


first_point = list(map(float, input().split()))
second_point = list(map(float, input().split()))

first_point = Point(first_point[0], first_point[1])
second_point = Point(second_point[0], second_point[1])

distance = get_distance(first_point, second_point)

print(f'{distance:.3f}')
