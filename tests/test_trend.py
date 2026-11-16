import unittest

from mathtools.trend import trend_report


class TestTrend(unittest.TestCase):
    def test_linear_trend(self):
        report = trend_report([-1, 0, 1], [1, 3, 5], next_x=2, max_degree=1)
        self.assertEqual(report["degree"], 1)
        self.assertAlmostEqual(report["forecast"], 7)
        self.assertAlmostEqual(report["r_squared"], 1.0)


if __name__ == "__main__":
    unittest.main()
