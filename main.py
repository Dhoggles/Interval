class Interval:

    # когда ты пишешь self ты просишь класс переменную с каким-то именем
    # если ты указала self - то менять перемнную можно в любом методе
    def __init__(self, first_point, last_point):
        self.first_point = first_point
        self.last_point = last_point

    def empty(self):
        return self.first_point is None and self.last_point is None

    def cross(self, other):
        left_point = max(self.first_point, other.first_point)
        right_point = min(self.last_point, other.last_point)
        if left_point > right_point:
            left_point, right_point = None, None
        return Interval(left_point, right_point)

    def __eq__(self, other):
        return self.first_point == other.first_point and self.last_point == other.last_point

    def point_in_interval(self, point):
        for i in range(self.first_point, self.last_point + 1):
            if point == i:
                return True
        return False
