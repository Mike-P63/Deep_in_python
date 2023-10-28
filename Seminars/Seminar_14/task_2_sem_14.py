

class Side:
    def __set_name__(self, owner, name):
        self.param_name = ' ' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError


class Rect:
    _l = Side()
    _w = Side()

    def __init__(self, lenght, width=None):
        self._l = lenght
        if width:
            self._w = width
        else:
            self._w = lenght

    # @property
    # def l(self):
    #     return self._l
    #
    # @l.setter
    # def l(self, value):
    #     if value > 0:
    #         self._l = value
    #     else:
    #         raise ValueError
    #
    # @property
    # def w(self):
    #     return self._w
    #
    # @w.setter
    # def w(self, value):
    #     if value > 0:
    #         self._w = value
    #     else:
    #         raise ValueError

    def per(self):
        return 2 * (self._l + self._w)

    def sq(self):
        return self._l * self._w

    def __add__(self, other: "Rect"):
        if self._w == other._w:
            sum_per = self.per() + other.per()
            new_len = sum_per / 2 - self._w
            return Rect(new_len, self._w)
        else:
            raise ValueError

    def __sub__(self, other: "Rect"):
        if self._w == other._w:
            sum_per = self.per() - other.per()
            new_len = sum_per / 2 - self._w
            return Rect(new_len, self._w)
        else:
            raise ValueError

    def __eq__(self, other: "Rect"):
        return self.sq() == other.sq()

    def __gt__(self, other: "Rect"):
        return self.sq() > other.sq()

    def __lt__(self, other: "Rect"):
        return self.sq() < other.sq()

    def __repr__(self) -> str:
        return f"Rect({self._l}, {self._w})"