import unittest

from mathtools.matrix import determinant, multiply, solve, transpose


class TestMatrix(unittest.TestCase):
    def test_transpose(self):
        self.assertEqual(transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_multiply(self):
        self.assertEqual(multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]])

    def test_multiply_invalid(self):
        with self.assertRaises(ValueError):
            multiply([[1, 2]], [[1, 2]])

    def test_determinant(self):
        self.assertAlmostEqual(determinant([[2, 0], [0, 3]]), 6)
        self.assertAlmostEqual(determinant([[4, 3], [2, 1]]), -2)

    def test_determinant_singular(self):
        self.assertEqual(determinant([[1, 2], [2, 4]]), 0)

    def test_solve(self):
        solution = solve([[4, 1], [1, 3]], [9, 5])
        self.assertAlmostEqual(solution[0], 2)
        self.assertAlmostEqual(solution[1], 1)

    def test_solve_singular(self):
        with self.assertRaises(ValueError):
            solve([[1, 2], [2, 4]], [1, 2])


if __name__ == "__main__":
    unittest.main()
