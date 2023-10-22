class Side:
    def __set_name__(self, owner, name):
        self.param_name = "_"+name

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

    def __repr__(self) -> str:
        return f"Rect({self._l}, {self._w})"

    # @property
    # def l(self):
    #     return self._l

    # @l.setter
    # def l(self, value):
    #     if value > 0:
    #         self._l = value
    #     else:
    #         raise ValueError

    # @property
    # def w(self):
    #     return self._w

    # @w.setter
    # def w(self, value):
    #     if value > 0:
    #         self._w = value
    #     else:
    #         raise ValueError
x1 = Rect(3, 2)
x2 = Rect(3, 5)
print(x1)
print(x2)
x2._w = -3
print(x2)