import math


class Point:
    __x: float
    __y: float

    def __init__(self, x: float, y: float):
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


class Points:
    __points: list = []

    def add_point(self, p: Point):
        self.__points.append(p)

    def get_distance(self, point_a: Point, point_b: Point):
        side_x = abs(point_a.get_x() - point_b.get_x())
        side_y = abs(point_a.get_y() - point_b.get_y())
        side_z = math.sqrt(pow(side_x, 2) + side_y ** 2)
        return side_z

    def get_closest_distance(self):
        distances = {}
        for r1 in self.__points:
            for r2 in self.__points:
                if r1 != r2:
                    distance = self.get_distance(r1, r2)
                    if distance not in distances:
                        distances[distance] = [r1, r2]

        short = sorted(distances.keys())[0]
        print(f'{short:.3f}')
        p1, p2 = distances[short]
        print(f'({p1.get_x():.3g}, {p1.get_y():.3g})')
        print(f'({p2.get_x():.3g}, {p2.get_y():.3g})')


num_points = int(input())
points = Points()

while num_points > 0:
    num_points -= 1
    x, y = list(map(float, input().split()))
    points.add_point(Point(x, y))


points.get_closest_distance()
