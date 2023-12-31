import unittest

from task_2_sem_14 import Rect

# class TestRect(unittest.TestCase):
    
#     def test_raise_valueerror(self):
#         with self.assertRaises(ValueError):
#             Rect(4 -3)

#     def test_is_rect(self):
#         self.assertIsInstance(Rect(3,3) + Rect(3, 3), Rect)

#     def test_per(self):
#         self.assertEqual(Rect(3,2).per(), 10)

# if __name__ == "__main__":
#     unittest.main(verbosity=1)


# import unittest
# from control_num import Rect


class TestRect(unittest.TestCase):
    def setUp(self):
        self.r1 = Rect(3,3)
        self.r2 = Rect(4,3)

    def test_raise_valueerror(self):
        with self.assertRaises(ValueError):
            Rect(3, -4)

    def test_is_rect(self):
        self.assertIsInstance(self.r1 + self.r2, Rect)

    def test_per(self):
        self.assertEqual(self.r1.per(), 12)


if __name__ == '__main__':
    unittest.main(verbosity=3)