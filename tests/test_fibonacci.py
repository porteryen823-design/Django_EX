

import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import fibonacci

class TestFibonacci(unittest.TestCase):
    """測試斐波那契函數的正確性與邊界條件"""
    
    def test_base_cases(self):
        """驗證基本案例（n = 0 和 n = 1）"""
        self.assertEqual(fibonacci(0), 0, "F(0) 應該是 0")
        self.assertEqual(fibonacci(1), 1, "F(1) 應該是 1")
    
    def test_known_values(self):
        """驗證已知的斐波那契數字（0 <= n <= 10）"""
        test_data = [
            (2, 1), (3, 2), (4, 3), (5, 5), (6, 8),
            (7, 13), (8, 21), (9, 34), (10, 55)
        ]
        for n, expected in test_data:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)
    
    def test_negative_input(self):
        """驗證負數輸入時的錯誤處理"""
        with self.assertRaises(RecursionError):
            fibonacci(-1)
    
    def test_invalid_input_type(self):
        """驗證非整數輸入時的錯誤處理"""
        # 字串型別
        with self.assertRaises(TypeError):
            fibonacci("3")
        # 浮點數型別
        with self.assertRaises(TypeError):
            fibonacci(3.5)
        # None 值
        with self.assertRaises(TypeError):
            fibonacci(None)

if __name__ == '__main__':
    unittest.main()
