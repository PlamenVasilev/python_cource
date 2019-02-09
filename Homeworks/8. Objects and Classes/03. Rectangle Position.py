class Rectangle:
    __x: float
    __y: float
    __width: float
    __height: float

    def __init__(self, x, y, w, h):
        self.set_x(x)
        self.set_y(y)
        self.set_width(w)
        self.set_height(h)

    def set_x(self, x):
        if not isinstance(x, float):
            raise Exception
        self.__x = x

    def set_y(self, y):
        if not isinstance(y, float):
            raise Exception
        self.__y = y

    def set_width(self, w):
        if not isinstance(w, float):
            raise Exception
        self.__width = w

    def set_height(self, h):
        if not isinstance(h, float):
            raise Exception
        self.__height = h

    def get_x1(self):
        return self.__x

    def get_y1(self):
        return self.__y

    def get_x2(self):
        return self.__x + self.__width

    def get_y2(self):
        return self.__y + self.__height


def check_inside(point_1, point_2):
    if point_1.get_x1() >= point_2.get_x1() and point_1.get_y1() >= point_2.get_y1() and point_1.get_x2() <= point_2.get_x2() and point_1.get_y2() <= point_2.get_y2():
        print('Inside')
    else:
        print('Not inside')


x, y, w, h = list(map(float, input().split()))
point_1 = Rectangle(x, y, w, h)

x, y, w, h = list(map(float, input().split()))
point_2 = Rectangle(x, y, w, h)

check_inside(point_1, point_2)
