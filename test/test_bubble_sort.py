from unittest import TestCase
import src.algo.sort
from src.algo.sort.bubble_sort import bubble_sort


class TestBubbleSort(TestCase):
    def test_bubble_sort(self):
        import sys
        a = []
        out = bubble_sort(a)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, 'hello')
