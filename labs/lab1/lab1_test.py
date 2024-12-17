import unittest
from unittest.mock import patch
import math
import sys

# Импортируем функции, которые будем тестировать
from main import get_coef, get_roots, main


class TestQuadraticEquation(unittest.TestCase):

    def test_get_coef_from_argv(self):
        """Тестируем получение коэффициента из аргументов командной строки"""
        sys.argv = ['script_name', '1.0', '2.0', '3.0']
        self.assertEqual(get_coef(1, "Введите коэффициент A:"), 1.0)
        self.assertEqual(get_coef(2, "Введите коэффициент B:"), 2.0)
        self.assertEqual(get_coef(3, "Введите коэффициент C:"), 3.0)

    @patch('builtins.input', side_effect=['4.0'])
    def test_get_coef_from_input(self, mock_input):
        """Тестируем получение коэффициента через ввод, если аргумента нет"""
        sys.argv = ['script_name']
        self.assertEqual(get_coef(1, "Введите коэффициент A:"), 4.0)

    def test_get_roots_two_roots(self):
        """Тестируем получение двух корней"""
        self.assertEqual(get_roots(1, -3, 2), [2.0, 1.0])

    def test_get_roots_one_root(self):
        """Тестируем получение одного корня"""
        self.assertEqual(get_roots(1, 2, 1), [-1.0])

    def test_get_roots_no_roots(self):
        """Тестируем случай без вещественных корней"""
        self.assertEqual(get_roots(1, 0, 1), [])




if __name__ == "__main__":
    unittest.main()



if __name__ == '__main__':
    unittest.main()
