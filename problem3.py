# 3. テストを作ろう
# problem1をテストする関数を完成させる

import unittest
import problem1

class Problem1(unittest.TestCase):
    def test_problem1(self):
        with self.assertRaises(IndentationError):
            problem1.main()
        # 以下の記述を削除してここに処理を追加する
        # テストの中で「problem1.main()」を実行すること

if __name__ == '__main__':
    unittest.main()
