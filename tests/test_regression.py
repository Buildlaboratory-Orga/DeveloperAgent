import unittest

from mathtools.regression import polynomial_fit, predict, r_squared


class TestRegression(unittest.TestCase):
    def test_linear_fit(self):
        coefficients = polynomial_fit([-1, 0, 1], [1, 3, 5], 1)
        self.assertAlmostEqual(coefficients[0], 3)
        self.assertAlmostEqual(coefficients[1], 2)

    def test_predict(self):
        self.assertEqual(predict([3, 2], 4), 11)
        self.assertEqual(predict([1, 0, 2], 3), 19)

    def test_r_squared_perfect_fit(self):
        self.assertAlmostEqual(r_squared([-1, 0, 1], [1, 3, 5], [3, 2]), 1.0)

    def test_not_enough_points(self):
        with self.assertRaises(ValueError):
            polynomial_fit([1, 2], [1, 2], 2)


if __name__ == "__main__":
    unittest.main()
