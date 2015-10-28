import heapify
import unittest
import random
import math

class TestHeapify(unittest.TestCase):
    def setUp(self):
        self.heap = heapify.Heap(random.sample(range(100), 10))


class TestHeapify(unittest.TestCase):
    def setUp(self):
        self.heap = heapify.Heap(random.sample(range(10000), 1000))



    def test_heapsort(self):
        '''Тестирование метода heapsort'''
        self.heap.heapsort()
        for i in range(self.heap.size-1, 2, -1):
            self.assertGreater(self.heap.heap_list[self.heap.parent(i)], self.heap.heap_list[i])


if __name__ == '__main__':
	unittest.main()

