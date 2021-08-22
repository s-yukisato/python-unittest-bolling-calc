import unittest
from bolling_game import bolling_game


class TestBollingGame(unittest.TestCase):

    # 全てのスコアが0の時
    def test_all_0(self):
        excepted = 0
        scoreList = [0 for _ in range(20)]
        actual = bolling_game(scoreList)
        self.assertEqual(excepted, actual)

    # 全てのスコアが１
    def test_all_1(self):
        excepted = 20
        scoreList = [1 for _ in range(20)]
        actual = bolling_game(scoreList)
        self.assertEqual(excepted, actual)

    # 1回ストライク
    def test_1_strike(self):
        excepted = 45
        scoreList = [3, 6, 10, 8, 5]
        actual = bolling_game(scoreList)
        self.assertEqual(excepted, actual)

    # 全てストライク
    def test_all_strike(self):
        excepted = 300
        scoreList = [10 for _ in range(11)]
        actual = bolling_game(scoreList)
        self.assertEqual(excepted, actual)


if __name__ == "__main__":
    unittest.main()